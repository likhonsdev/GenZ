# GenZ: The First-Ever Bangla AGI Model

This repository contains the source code and resources for **GenZ**, a groundbreaking project to create the first-ever Bangla Artificial General Intelligence (AGI) model. Our mission is to build an autonomous and highly capable AI that understands and communicates in the Bangla language with unprecedented fluency and accuracy.

## Automated Workflow

- **Trigger**: The workflow is triggered automatically on every push to the `main` branch.
- **Training**: The `train_gpt_genz.py` script fine-tunes a large language model on a Bangla dataset.
- **Deployment**: After training, the model is automatically pushed to the [Hugging Face Hub](https://huggingface.co/likhonsdev/GenZ).

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
