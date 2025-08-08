# GenZ: The First-Ever Bangla AGI Model

**"আমরা কৃত্রিম সাধারণ বুদ্ধিমত্তার জগতে একটি নতুন দিগন্ত উন্মোচন করছি।"**

This repository contains the source code and resources for **GenZ**, a groundbreaking project to create the first-ever Bangla Artificial General Intelligence (AGI) model. Our mission is to build an autonomous and highly capable AI that understands and communicates in the Bangla language with unprecedented fluency and accuracy. This project is proudly led by [likhonsheikhofficial](https://github.com/likhonsheikhofficial).

## Automated Workflow

- **Trigger**: The workflow is triggered automatically on every push to the `main` branch.
- **Training**: The `train_gpt_genz.py` script fine-tunes a large language model on a Bangla dataset.
- **Deployment**: After training, the model is automatically pushed to the [Hugging Face Hub](https://huggingface.co/likhonsdev/GenZ).

### Workflow Diagram

```
+-------------------+      +----------------------+      +-------------------------+
|                   |      |                      |      |                         |
|  Push to `main`   +----->+  GitHub Actions CI/CD  +----->+  Hugging Face Hub Model |
|                   |      |                      |      |                         |
+-------------------+      +----------------------+      +-------------------------+
```

### Conceptual Sketch
*(A sketch illustrating the architecture of the Bangla AGI will be added here soon.)*

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
