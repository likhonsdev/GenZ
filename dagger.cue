dagger:
  version: 2
  
tasks:
  deploy:
    container:
      from: likhonsdev/genz-model-runner:latest
      envs:
        OPENAI_BASE_URL: http://model-runner.docker.internal/engines/llama.cpp/v1/
        OPENAI_DISABLE_STREAMING: "true"
        OPENAI_MODEL: index.docker.io/ai/qwen2.5:7B-F16
      ports:
        - 8000:8000
      devices:
        - /dev/nvidia0
        - /dev/nvidiactl
        - /dev/nvidia-uvm
      volumes:
        - ~/.dagger:/root/.dagger
      memory: 16G
      cpus: 4
      gpus: all
