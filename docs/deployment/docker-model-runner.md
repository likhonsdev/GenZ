# Docker Model Runner with Dagger

This document describes the GitHub Actions workflow for running an AI model using Docker Model Runner and Dagger. The workflow is defined in the file `.github/workflows/docker-model-runner.yml`.

## Overview

The workflow automates the process of:
- Setting up a Docker environment.
- Pulling a pre-trained AI model from Docker Hub.
- Using Dagger to interact with the model and generate output.

This allows for easy integration of AI models into the CI/CD pipeline, enabling automated testing and generation of content.

## Workflow Definition

The workflow is triggered on pushes to the `main` branch and can also be triggered manually.

```yaml
name: Docker Model Runner with Dagger

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  run_model:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Docker
        uses: docker/setup-buildx-action@v3

      - name: Pull AI Model
        run: docker model pull index.docker.io/ai/qwen2.5:7B-F16

      - name: Run Dagger with Local Model
        env:
          OPENAI_BASE_URL: http://model-runner.docker.internal/engines/llama.cpp/v1/
          OPENAI_DISABLE_STREAMING: "true"
          OPENAI_MODEL: index.docker.io/ai/qwen2.5:7B-F16
        run: |
          myenv=$(env |
            with-directory-input "empty" $(directory) "empty directory to add new files to" |
            with-directory-output "full" "a directory containing the ascii art files")

          llm |
            with-env $myenv |
            with-prompt "start with empty, add 2 new smiley-themed pieces of ascii art, return as full" |
            env |
            output "full" |
            as-directory |
            terminal
```

## Workflow Steps

1.  **Checkout repository**: This step checks out the source code of the repository.
2.  **Set up Docker**: This step sets up the Docker buildx environment, which is required for building and running Docker containers.
3.  **Pull AI Model**: This step pulls the `qwen2.5:7B-F16` model from Docker Hub. This model is a large language model that can be used for various natural language processing tasks.
4.  **Run Dagger with Local Model**: This step runs a Dagger pipeline that interacts with the local model.

    -   **Environment Variables**:
        -   `OPENAI_BASE_URL`: Specifies the URL of the local OpenAI-compatible engine provided by Docker Model Runner.
        -   `OPENAI_DISABLE_STREAMING`: Disables streaming of responses from the model.
        -   `OPENAI_MODEL`: Specifies the default model to use.

    -   **Dagger Command**: The Dagger command creates an environment for the LLM, provides a prompt to generate ASCII art, and then outputs the result to the terminal.

## How to Use

To use this workflow, simply push a commit to the `main` branch or trigger it manually from the Actions tab in the GitHub repository. The workflow will then run automatically and generate the ASCII art as specified in the prompt.

> [!NOTE]
> The model used in this workflow is quite large (~14 GB). The `docker model pull` command may take some time to complete.
