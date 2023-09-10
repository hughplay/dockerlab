# syntax=docker/dockerfile:1.4
FROM deepbase/dockerlab:workspace_cuda_11_7


# Install Pytorch 2.0
# you can find other versions and installation commands from:
# https://pytorch.org/get-started/previous-versions/
# https://github.com/pytorch/pytorch/wiki/PyTorch-Versions
RUN pip install --no-cache-dir \
    torch==2.0.1 \
    torchvision==0.15.2 \
    torchaudio==2.0.2 \
    --extra-index-url https://download.pytorch.org/whl/cu117
