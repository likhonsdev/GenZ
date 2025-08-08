from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from peft import get_peft_model, LoraConfig, TaskType
import torch

# 1. Load Bengali Chat dataset
dataset = load_dataset("rishiraj/bengalichat", split="train")

# 2. Load tokenizer and base model
model_name = "bigscience/bloom-560m"  # Lightweight and multilingual
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 3. Preprocess text (convert to tokens)
def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=256)

tokenized_ds = dataset.map(tokenize, batched=True)
tokenized_ds.set_format("torch", columns=["input_ids", "attention_mask"])

# 4. LoRA config for parameter-efficient tuning
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["query_key_value"],
    lora_dropout=0.1,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)

model = get_peft_model(model, lora_config)

# 5. Training args
training_args = TrainingArguments(
    output_dir="./GenZ-checkpoints",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=100,
    fp16=True,
    save_strategy="epoch",
    push_to_hub=True,
    hub_model_id="likhonsheikh/GenZ",
)

# 6. Trainer setup
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds,
    data_collator=data_collator,
)

# 7. Train the model
trainer.train()
