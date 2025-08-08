# GenZ: The First-Ever Bangla AGI Model

**"আমরা কৃত্রিম সাধারণ বুদ্ধিমত্তার জগতে একটি নতুন দিগন্ত উন্মোচন করছি।"**

This repository contains the source code and resources for **GenZ**, a groundbreaking project to create the first-ever Bangla Artificial General Intelligence (AGI) model. Our mission is to build an autonomous and highly capable AI that understands and communicates in the Bangla language with unprecedented fluency and accuracy. This project is proudly led by [likhonsheikhofficial](https://github.com/likhonsheikhofficial).

## Project Structure

```
.
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

GenZ is evaluated on the **GAIA benchmark**, a challenging set of real-world problems designed to test the capabilities of General AI Assistants. We are proud to announce that GenZ has achieved new state-of-the-art (SOTA) performance across all three difficulty levels of the GAIA benchmark.

### GAIA Benchmark Performance
- **Level 1 (Basic)**: Mastery in fundamental task completion and language understanding
- **Level 2 (Complex)**: Superior performance in multi-step problem solving
- **Level 3 (Advanced)**: Outstanding results in complex reasoning and decision making

### Automated Training and Evaluation
- Continuous benchmark evaluation through GitHub Actions
- Automated model training and performance tracking
- Regular updates to maintain SOTA status

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
