FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu20.04


# Set default RUN shell to /bin/bash
SHELL ["/bin/bash", "-cu"]


# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


# Install basic packages for compiling and building
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    build-essential \
    cmake \
    g++-7 \
    git \
    curl \
    wget \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    librdmacm1 \
    libibverbs1 \
    ibverbs-providers \
    tzdata \
    libgl1-mesa-glx \
    libglib2.0-0 \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*


# Install Miniconda & use Python 3.8
ARG python=3.8
ENV PYTHON_VERSION=${python}
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/install-conda.sh \
    && chmod +x /tmp/install-conda.sh \
    && bash /tmp/install-conda.sh -b -f -p /usr/local \
    && rm -f /tmp/install-conda.sh \
    && conda install -y python=${PYTHON_VERSION} \
    && conda clean -y --all


# ==================================================
# *Tools installation (optional)
#
# You find some tools useful or unwanted, comment or uncomment them as you wish.
# Check this page for more installation commands:
# https://github.com/hughplay/memo/blob/master/scripts/prepare_dl.sh
# ==================================================


# Install basic packages
RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    zsh \
    vim \
    zip \
    unzip \
    rsync \
    htop \
    language-pack-en \
    nethogs \
    sysstat \
    gnupg \
    lsb-release \
    sudo \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*


# Set ZSH as default shell & Install Oh My Zsh and zsh plugin: zsh-autosuggestions
RUN chsh -s `which zsh` \
    && curl https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash -s -- --unattended \
    && wget https://raw.githubusercontent.com/oskarkrawczyk/honukai-iterm/master/honukai.zsh-theme -O ${ZSH:-~/.oh-my-zsh}/themes/honukai.zsh-theme --no-check-certificate \
    && sed -i.bak '/ZSH_THEME/s/\".*\"/\"honukai\"/' ~/.zshrc \
    && git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH:-~/.oh-my-zsh}/custom/plugins/zsh-autosuggestions\
    && sed -i.bak '/plugin/s/(.*)/(git zsh-autosuggestions)/' ~/.zshrc


# make the color of zsh-autosuggestions right
ENV TERM xterm-256color


# Install docker (to make docker in docker work)
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*


# Install Tmux
RUN apt-get update && apt-get install -y libevent-dev ncurses-dev automake pkg-config \
    && cd /tmp \
    && wget -O tmux-2.8.tar.gz https://github.com/tmux/tmux/archive/2.8.tar.gz \
    && tar zxvf tmux-2.8.tar.gz \
    && cd tmux-2.8 \
    && ./autogen.sh \
    && ./configure --prefix=/usr/local \
    && make \
    && make install \
    && rm -rf /var/lib/apt/lists/*

# Tmux configuration
RUN git clone https://github.com/hughplay/tmux-config.git /tmp/tmux-config \
    && bash /tmp/tmux-config/install.sh \
    && rm -rf /tmp/tmux-config \
    && echo "set -g default-shell `which zsh`" >> ~/.tmux.conf


# Install lightvim, a configuration for vim
# RUN wget https://raw.githubusercontent.com/hughplay/lightvim/master/install.sh -O - | sh


# ==================================================
# *Fonts installation
#
# Install fonts that are commonly used in plotting.
# Question: "Which font looks best in a scientific figure?"
# Answer: "Arial or Helvetica, always."
# https://pubs.acs.org/doi/10.1021/acs.chemmater.6b00306
#
# fonts include:
#   - Arial (recommended)
#   - Helvetica
#   - Palatino Linotype
#   - Times New Roman
# ==================================================


RUN cd /tmp \
    && wget https://github.com/hughplay/memo/raw/master/code/snippet/drawing/plot_fonts.tar.gz \
    && tar zxvf plot_fonts.tar.gz \
    && cp plot_fonts/* /usr/share/fonts/truetype/ \
    && rm -rf plot_fonts.tar.gz plot_fonts \
    && fc-cache -fv
