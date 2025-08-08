# GenZ: Automated Training and Deployment

This repository contains the code for training and deploying the GenZ model. The process is fully automated using GitHub Actions.

## Automated Workflow

- **Trigger**: The workflow is triggered automatically on every push to the `main` branch.
- **Training**: The `train_gpt_genz.py` script fine-tunes the `bigscience/bloom-560m` model on the `rishiraj/bengalichat` dataset.
- **Deployment**: After training, the model is automatically pushed to the [Hugging Face Hub](https://huggingface.co/likhonsheikh/GenZ).

## Setup

To enable the automated workflow, you need to add your Hugging Face Hub token as a secret to your GitHub repository:

1.  Go to your repository's **Settings** > **Secrets and variables** > **Actions**.
2.  Click **New repository secret**.
3.  Name the secret `HUGGING_FACE_HUB_TOKEN`.
4.  Paste your Hugging Face Hub token (with write permissions) into the value field.

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
