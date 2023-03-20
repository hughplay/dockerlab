FROM deepbase/dockerlab:workspace_cuda_11_7


# Install Pytorch 1.13.1
# you can find other versions and installation commands from:
# https://pytorch.org/get-started/previous-versions/
# https://github.com/pytorch/pytorch/wiki/PyTorch-Versions
RUN pip install --no-cache-dir \
    torch==1.13.1 \
    torchvision==0.14.1 \
    torchaudio==0.13.1 \
    --extra-index-url https://download.pytorch.org/whl/cu117


RUN pip install --no-cache-dir \
    pytorch-lightning==1.9.4 \
    torchmetrics
