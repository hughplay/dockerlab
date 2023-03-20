# Dockerlab pre-built images

The table below lists the pre-built images for different versions of Ubuntu and CUDA. You can use these images directly without building them yourself.

All images can be found on [Docker Hub](https://hub.docker.com/r/deepbase/dockerlab).

| Name | Description | Dockerfile |
| --- | --- | --- |
| `FROM workspace_cuda_11_1` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.1.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul></ul> | [Dockerfile](workspace_cuda_11_1/Dockerfile) |
| `FROM workspace_cuda_11_7` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.7.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul></ul> | [Dockerfile](workspace_cuda_11_1/Dockerfile) |
