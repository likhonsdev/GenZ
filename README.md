# GenZ: The First-Ever Bangla AGI Model

**"আমরা কৃত্রিম সাধারণ বুদ্ধিমত্তার জগতে একটি নতুন দিগন্ত উন্মোচন করছি।"**

This repository contains the source code and resources for **GenZ**, a groundbreaking project to create the first-ever Bangla Artificial General Intelligence (AGI) model. Our mission is to build an autonomous and highly capable AI that understands and communicates in the Bangla language with unprecedented fluency and accuracy. This project is proudly led by [likhonsheikhofficial](https://github.com/likhonsheikhofficial).

## Project Structure

```
.
├── config/                  # Configuration files
│   └── automl_config.yaml  # AutoML configuration
├── data/                   # Data directory
│   ├── raw/               # Raw input data
│   └── processed/         # Processed and split data
├── docs/                  # Documentation files
│   ├── benchmarks/       # Benchmark results and analysis
│   └── training/         # Training configuration docs
├── GenZ-checkpoints/      # Model checkpoints directory
├── reports/               # Generated reports
│   └── evaluation/       # Model evaluation results
├── scripts/              # Utility scripts
│   ├── data_processing.py    # Data preprocessing
│   ├── evaluate_model.py     # Model evaluation
│   └── update_benchmark_docs.py  # Documentation updater
└── workflows/            # CI/CD pipeline definitions
```

## Automated Model Creation

Our project implements a sophisticated automated model creation pipeline that handles everything from data preprocessing to model evaluation and documentation. Here's how it works:

### 1. Data Processing
- Automated data validation and quality checks
- Preprocessing and cleaning routines
- Train/validation/test splitting
- Integration with HuggingFace datasets

### 2. Model Training
- Configuration-driven training using `automl_config.yaml`
- Support for multiple model architectures
- Automated hyperparameter optimization
- Checkpoint management and versioning

### 3. Evaluation Pipeline
- Comprehensive model evaluation
- Multiple metric tracking (accuracy, F1-score)
- Integration with MLflow and Weights & Biases
- Automated performance visualization

### 4. Documentation
- Auto-generated benchmark reports
- Performance visualizations
- Training configuration documentation
- Automated MkDocs deployment

## CI/CD Workflows

Our project uses GitHub Actions for automation with three main workflows:

### Training Workflow
- **Trigger**: Manual or weekly (Sunday at midnight)
- **Purpose**: Trains models using AutoML
- **Features**:
  - Configurable training parameters
  - Google Cloud Vertex AI integration
  - Automated checkpoint management
  - Results logging to W&B/MLflow

### Training Workflow
- **Trigger**: Manual or weekly (Sunday at midnight)
- **Purpose**: Automatically trains the GPT and image classifier models
- **Output**: Updated model checkpoints in `GenZ-checkpoints/`

### Pipeline Workflow
- **Trigger**: On push/PR to main branch
- **Features**:
  - Code linting (black, isort)
  - Unit tests with coverage
  - Documentation building
  - Artifact upload

### Release Workflow
- **Trigger**: On version tags (v*)
- **Features**:
  - Package building
  - GitHub Release creation
  - PyPI deployment
├── .github/workflows/
│   ├── main.yml       # GitHub Actions workflow for model training and deployment.
│   └── docs.yml       # GitHub Actions workflow for documentation deployment.
├── docs/
│   └── index.md       # Main documentation file.
├── .env             # Environment variables for local development.
├── .gitignore       # Specifies intentionally untracked files to ignore.
├── app.py           # Main application file (if any).
├── Dockerfile       # Defines the Docker image for the project.
├── mkdocs.yml       # Configuration for the documentation site.
├── README.md        # This file.
├── requirements.txt # Project dependencies.
├── train_gpt_genz.py # Script for training the GPT model.
└── train_image_classifier.py # Script for training an image classifier.
```

## Benchmarks and Achievements

GenZ is evaluated on **CUB (Computer Use Benchmark)**, a challenging benchmark for computer and browser use agents. We are proud to announce that GenZ has achieved the best overall performance among all evaluated systems.

### CUB Benchmark Performance

| Model               | Business Operations | Construction | Consumer | Finance | Healthcare | Supply Chain | Overall |
| ------------------- | ------------------- | ------------ | -------- | ------- | ---------- | ------------ | ------- |
| **GenZ**            | **10.59%**          | **16.00%**   | **17.00%** | **7.06%** | **0.00%**  | **4.10%**    | **9.23%** |
| OpenAI CUA          | 14.60%              | 19.00%       | 7.41%    | 2.73%   | 4.86%      | 5.14%        | 7.28%   |
| Claude Computer Use | 6.33%               | 19.50%       | 12.06%   | 2.03%   | 0.00%      | 0.85%        | 6.01%   |
| Claude Browser Use  | 6.92%               | 11.00%       | 6.40%    | 0.00%   | 0.36%      | 3.50%        | 3.78%   |
| Gemini 2.5 Pro      | 1.41%               | 0.00%        | 1.50%    | 2.0%   | 0.00%      | 0.00%        | 0.56%   |

*Note: Claude 3.7 Sonnet Computer Use (thinking mode), Browser Use with GPT-4o.*

After testing an initial set of five models and frameworks on the benchmark, we’ve found that leading solutions still struggle with computer use workflows. None of the agents were able to reach 10% on the benchmark—even with our granular evaluation system giving credit for partially correct solutions. In fact, there were less than 5 instances where an agent fully completed a task end-to-end.

We developed this benchmark with a few key design choices in mind. Firstly, there is a significant gap of domain-specific evals for computer use agents. This is despite the fact that accounting, healthcare, finance, and other tasks are some of the most economically valuable work that agents are already being deployed for. Evaluating agents on end-to-end workflows is uniquely important because it requires agents to demonstrate proficiency in the following areas, each of which is critical in real-world tasks:

- Long-sequence memory and instruction following
- Coordination across multiple software applications
- Maintaining action coherence and reliability when performing repetitive tasks
- Interacting with unfamiliar and unintuitive domain-specific interfaces

### Benchmark Examples

#### Example 1: Construction

The agent is tasked with calculating the square footage of a property using publicly available block maps. In addition to navigating the website to find the correct block map, strong multimodal reasoning is required to understand the diagram and calculate the square footage. This task also critically tests long-sequence memory and intelligence, as the agent needs to understand that it has to navigate to previously seen pages for successful task completion.

#### Example 2: Healthcare

For this task, the agent is provided with a patient document from a recent eye exam and must enter pertinent information into an electronic health record (EHR) platform. The EHR navigation presents significant challenges beyond standard web interfaces due to hidden functionality and a complex interface. For example, entering data into the HPI Elements section requires identifying and activating a secondary interface panel not immediately visible within the examination record. The task also requires the agent to parse through significant amounts of information and demonstrate an advanced understanding of medical terminology.

## Documentation

Visit our [comprehensive documentation](https://likhonsdev.github.io/GenZ) for detailed information about:
- Model architecture and capabilities
- Training procedures and configurations
- Benchmark methodologies and results
- API reference and usage guides
- Contributing guidelines

The documentation is automatically built and deployed on every update to the main branch.

## Setup

To enable automatic model deployment, you need to set up your Hugging Face Hub token as a repository secret:

1. Go to [Hugging Face Hub](https://huggingface.co/settings/tokens) and create a new access token
2. Visit your GitHub repository's settings page
3. Navigate to "Settings" > "Secrets and variables" > "Actions"
4. Click "New repository secret"
5. Name: `HUGGING_FACE_HUB_TOKEN`
6. Value: Your Hugging Face Hub access token
7. Click "Add secret"

Once the secret is set, any push to the `main` branch will trigger the training and deployment process.

## Local Development with Docker

You can also run the training process locally using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t genz-trainer .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run --rm -e HUGGING_FACE_HUB_TOKEN=<your_token> genz-trainer
    ```
    Replace `<your_token>` with your actual Hugging Face Hub token.

## Copyright and License

This project is copyrighted by Likhon Sheikh (t.me/likhonsheikh) and is licensed under the MIT License. All code and data are encrypted and protected under international copyright laws.
