# syntax=docker/dockerfile:1.4
FROM deepbase/dockerlab:workspace_cuda_12_1


# Install Pytorch 2.1
# you can find other versions and installation commands from:
# https://pytorch.org/get-started/previous-versions/
# https://github.com/pytorch/pytorch/wiki/PyTorch-Versions
RUN pip install --no-cache-dir \
    torch==2.2.0 \
    torchvision==0.17.0 \
    torchaudio==2.2.0 \
    torchtext==0.17.0 \
    --extra-index-url https://download.pytorch.org/whl/cu118
