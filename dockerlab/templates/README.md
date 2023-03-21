# Dockerlab pre-built images

The table below lists the pre-built images for different versions of Ubuntu and CUDA. You can use these images directly without building them yourself.


- All images can be found in [Docker Hub](https://hub.docker.com/r/deepbase/dockerlab/tags).
- The source code of these images can be found in [hughplay/dockerlab](https://github.com/hughplay/dockerlab/tree/main/dockerlab/templates)


[![](http://github-actions.40ants.com/hughplay/dockerlab/matrix.svg)](https://github.com/hughplay/dockerlab?only=images-build)


| Name | Description | Dockerfile |
| --- | --- | --- |
| `FROM workspace_base` | Image includes: <ul><li>Ubuntu 20.04</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul></ul> | [Dockerfile](workspace_cuda_11_1/Dockerfile) |
| `FROM workspace_cuda_11_1` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.1.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul></ul> | [Dockerfile](workspace_cuda_11_1/Dockerfile) |
| `FROM workspace_cuda_11_7` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.7.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul></ul> | [Dockerfile](workspace_cuda_11_1/Dockerfile) |
| `FROM workspace_pytorch_1_13` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.4.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul><li>Pytorch 1.13.1</li><li>Pytorch Lightning 1.9.4</li></ul> | [Dockerfile](workspace_pytorch_1_13/Dockerfile) |
| `FROM workspace_pytorch_2_0` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.4.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul><li>Pytorch 2.0</li><li>Pytorch Lightning 2.0.0</li></ul> | [Dockerfile](workspace_pytorch_2_0/Dockerfile) |
| `FROM workspace_protein` | Image includes: <ul><li>Ubuntu 20.04</li><li>CUDA 11.1.1</li><li>cuDNN 8</li><li>Miniconda (Python 3.8)</li><li>ZSH (Oh-My-ZSH)</li><li>Docker (docker in docker)</li><li>Tmux (tmux-config)</li><li>Common used fonts for plotting</li><ul><li>Arial (recommended)</li><li>Helvetica</li><li>Palatino Linotype</li><li>Times New Roman</li></ul><li>FFindex</li><li>CCMpred</li><li>HH-suite3</li><li>HMMER</li><li>BLAST</li><li>MMseqs2</li><li>Align toools: Clustal-Omega, EMBOSS, ProbCons, Kalign 3</li></ul> | [Dockerfile](workspace_protein/Dockerfile) |
| `FROM runtime_node` | Image includes: <ul><li>Node LTS</li><li>yrm</li></ul> | [Dockerfile](runtime_node/Dockerfile) |
