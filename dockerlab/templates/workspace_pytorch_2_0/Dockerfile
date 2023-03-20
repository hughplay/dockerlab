FROM deepbase/dockerlab:workspace_cuda_11_7


# Install Pytorch 2.0
# you can find other versions and installation commands from:
# https://pytorch.org/get-started/previous-versions/
# https://github.com/pytorch/pytorch/wiki/PyTorch-Versions
RUN pip install --no-cache-dir \
    torch==2.0.0 \
    torchvision==0.15.1 \
    torchaudio==2.0.1 \
    --extra-index-url https://download.pytorch.org/whl/cu117


RUN pip install --no-cache-dir \
    pytorch-lightning==2.0.0 \
    torchmetrics
