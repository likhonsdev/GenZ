import torch
from datasets import load_dataset
from transformers import AutoImageProcessor, AutoModelForImageClassification, TrainingArguments, Trainer
from torchvision.transforms import Compose, ToTensor, Resize, Normalize
import numpy as np
import evaluate

# 1. Load CUB-200-2011 dataset
# Using a version of the dataset prepared for Hugging Face datasets library
dataset = load_dataset("conan94/cub200-2011")

# 2. Create label mappings
labels = dataset["train"].features["label"].names
id2label = {i: label for i, label in enumerate(labels)}
label2id = {label: i for i, label in enumerate(labels)}

# 3. Load pre-trained model and image processor
model_checkpoint = "google/vit-base-patch16-224-in21k"
image_processor = AutoImageProcessor.from_pretrained(model_checkpoint)
model = AutoModelForImageClassification.from_pretrained(
    model_checkpoint,
    num_labels=len(labels),
    id2label=id2label,
    label2id=label2id,
    ignore_mismatched_sizes=True, # To replace the classifier head
)

# 4. Preprocess dataset
# Define the transformations
normalize = Normalize(mean=image_processor.image_mean, std=image_processor.image_std)
transform = Compose([
    Resize(tuple(image_processor.size.values())),
    ToTensor(),
    normalize,
])

def preprocess_function(examples):
    # Apply the transformations to all images in the batch
    examples['pixel_values'] = [transform(image.convert("RGB")) for image in examples['image']]
    return examples

# Apply the preprocessing to the dataset
processed_ds = dataset.with_transform(preprocess_function)

# 5. Define evaluation metric
metric = evaluate.load("accuracy")
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return metric.compute(predictions=predictions, references=labels)

# 6. Training Arguments
training_args = TrainingArguments(
    output_dir="./cub-classifier-checkpoints",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=4,
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    remove_unused_columns=False, # Important for this dataset
    fp16=torch.cuda.is_available(),
)

# 7. Trainer Setup
def collate_fn(batch):
    return {
        'pixel_values': torch.stack([x['pixel_values'] for x in batch]),
        'labels': torch.tensor([x['label'] for x in batch])
    }

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=processed_ds["train"],
    eval_dataset=processed_ds["test"],
    tokenizer=image_processor,
    compute_metrics=compute_metrics,
    data_collator=collate_fn,
)

# 8. Train the model
print("Starting model training...")
trainer.train()

# 9. Evaluate the model
print("Evaluating the final model...")
eval_results = trainer.evaluate()
print(f"Evaluation results: {eval_results}")

# 10. Save the final model and processor
print("Saving the fine-tuned model...")
trainer.save_model("./cub-200-2011-vit-classifier")
image_processor.save_pretrained("./cub-200-2011-vit-classifier")

print("Script finished.")
