# syntax=docker/dockerfile:1.4
FROM deepbase/dockerlab:workspace_base


# ==================================================
# Node install
# ==================================================

RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | \
    gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

ENV NODE_MAJOR=20
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | \
    sudo tee /etc/apt/sources.list.d/nodesource.list

RUN apt-get update && \
    apt-get install nodejs -y && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g yarn yrm
