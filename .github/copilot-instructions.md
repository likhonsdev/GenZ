# GenZ Development Guide: Bangla AGI Model Project

This guide outlines the core architecture and workflows for developing GenZ - the first-ever Bangla AGI model project, focusing on complex computer-based tasks. Each section provides actionable steps and key reference points.

## Core Components and Data Flow

### Training Pipeline
- **Primary Scripts**: 
  - `train_automl.py`: AutoML-based text classification via Vertex AI
    ```python
    # Example configuration in automl_config.yaml
    modelType: MULTICLASS_TEXT
    optimizationObjective: MINIMIZE_LOG_LOSS
    budgetMilliNodeHours: 8000
    ```
  - `train_gpt_genz.py`: Fine-tunes base GPT model on Bangla corpus
    - Handles: Tokenization, training, model compression
    - Outputs: HuggingFace-compatible checkpoints
  - `train_image_classifier.py`: Vision model for UI interaction
    - Purpose: Identify UI elements in computer interfaces
    - Format: PyTorch model with custom attention layers

### Evaluation System
- **Central Script**: `scripts/evaluate_model.py`
- **Key Framework**: Computer Use Benchmark (CUB)
  - Tests: 
    1. Long-sequence memory (8K+ tokens)
    2. Cross-application coordination
    3. Bangla UI navigation proficiency
  - Scenarios: 
    1. Healthcare EHR: Patient data interpretation
    2. Construction: Block map visualization
    3. System navigation: OS/app interaction
- **Metrics**: 
  - Task completion: Accuracy, F1-score
  - Efficiency: Response time, memory usage
  - Language: Bangla coherence, technical accuracy

### Data Processing Chain
1. **Input Processing** (`scripts/data_processing.py`):
   - Bangla text normalization
   - UI screenshot preprocessing
   - Action sequence tokenization
   
2. **Training Pipeline**:
   ```
   Raw Data → Preprocessing → Training → Evaluation
   ├── text/      # Bangla corpus
   ├── images/    # UI screenshots
   └── actions/   # Interaction logs
   ```

3. **Output Management**:
   - Checkpoints: `GenZ-checkpoints/{model}-{version}-{timestamp}`
   - Metrics: `reports/evaluation/{model}/{timestamp}/`
   - Logs: `logs/{model}/{run_id}/`

## Development Operations

### Local Environment (Docker)
```bash
# Build training environment
docker build -t genz-trainer .

# Run training container
docker run --rm -e HUGGING_FACE_HUB_TOKEN=<your_token> genz-trainer
```

### CI/CD Pipeline
1. **Main Pipeline** (`main.yml`):
   - Triggers: Push/PR to `main`, weekly schedule, manual
   - Actions: Lint → Test → Train → Evaluate → Deploy
   - Integrations: Vertex AI, W&B/MLflow

2. **Documentation** (`docs.yml`):
   - Trigger: Push to `main`
   - Action: Build and deploy to GitHub Pages

## Project Standards

### Configuration Management
1. **Training Parameters**: YAML files in `config/`
2. **Local Development**: `.env` file (git-ignored)
3. **Documentation**: `mkdocs.yml`

### Checkpoint Management
- **Location**: `GenZ-checkpoints/`
- **Format**: `{model_type}-{version}-{timestamp}`
- **Retention**: Latest 3 versions per configuration

## Integration Architecture

### External Services
1. **Training**: Google Cloud Vertex AI, HuggingFace Hub
2. **Monitoring**: MLflow, Weights & Biases
3. **Deployment**: GitHub Pages (documentation)

### Component Communication
- **Training → Evaluation**: Via checkpoints
- **Evaluation → Docs**: Through benchmark updater
- **CI/CD → Services**: Via GitHub Actions

## Development Tasks

### Adding a New Model Type
1. **Configuration**:
   ```yaml
   # config/new_model_config.yaml
   model:
     name: "my-bangla-model"
     type: "transformer"  # or "cnn", "automl"
     params:
       vocab_size: 32000  # Bangla vocab
       max_length: 8192   # For long contexts
   ```

2. **Implementation**:
   ```python
   # train_new_model.py
   from genz.training import BaseTrainer
   from genz.data import BanglaDataset

   class NewModelTrainer(BaseTrainer):
       def setup_model(self):
           # Your model setup
   ```

3. **Integration**:
   - Add evaluation metrics in `scripts/evaluate_model.py`
   - Update benchmark categories in `docs/benchmarks/`
   - Configure CI/CD in `.github/workflows/main.yml`

### Troubleshooting Guide
1. **Data Pipeline Issues**:
   ```bash
   # Check data processing logs
   tail -f logs/data_processing.log
   
   # Validate dataset statistics
   python scripts/validate_data.py
   ```

2. **Training Problems**:
   - MLflow: `http://localhost:5000` (training metrics)
   - W&B: Project "genz-bangla" (experiment tracking)
   - Checkpoints: Check `GenZ-checkpoints/latest/`

3. **Model Performance**:
   - Evaluation: `reports/evaluation/latest/`
   - Benchmarks: `docs/benchmarks/results.md`
   - Error Analysis: `reports/errors/analysis.ipynb`
