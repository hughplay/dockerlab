<div align = center>


<h1>DockerLab</h1>

[![Package Building Status](https://img.shields.io/github/actions/workflow/status/hughplay/dockerlab/poetry-publish.yml?label=Package%20Build&style=flat-square)](https://github.com/hughplay/dockerlab/actions)
[![pypi](https://img.shields.io/pypi/v/dockerlab?color=blue&label=pypi&style=flat-square)](https://pypi.org/project/dockerlab/)
[![Image Building Status](https://img.shields.io/github/actions/workflow/status/hughplay/dockerlab/images-build.yml?label=Image%20Build&style=flat-square)](https://github.com/hughplay/dockerlab/actions)
[![](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square&labelColor=gray)](#license)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)](https://docs.docker.com/engine/)

*Build a docker container as your workspace.*


</div>

<br>

## Pre-requirements

- [Docker](https://docs.docker.com/engine/install)


## Features

- **Easy to use**: Just a few commands to build and start a docker container.
- **Customizable**: You can customize the docker image and the python packages you want to install in the container.
- **Reproducible**: You can build the same docker image on different machines. Say bye bye to the ["It works on my machine"](https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/) problem.
- **Convenient**: We made some convenient setups for you, including tools and functions:
  - tools: [oh-my-zsh](https://ohmyz.sh/), [docker within docker](https://www.docker.com/blog/docker-can-now-run-within-docker/), [tmux](https://github.com/tmux/tmux/wiki), [lightvim](https://github.com/hughplay/lightvim)
  - free of permission problems: same uid and gid as the host
  - reversely mounting $HOME directory from container to host
    - easy to share `~/.ssh` and `~/.gitconfig`
    - files will not be lost even if the container is removed, e.g., zsh history, configuration files, model checkpoints, ...
  - free of port mapping: sharing network with the host
- **Pre-built Images**: We provide several basic [pre-built images](dockerlab/templates/) for quickly setting up your own workspace environment.


## Quick Start

**1. Install dockerlab**

Install dockerlab with pip:

```bash
pip install dockerlab
```

Or install the latest version from source:

```bash
pip install git+https://github.com/hughplay/dockerlab.git
```


**2. Setup a dockerlab project**

Create a new dockerlab project:

```bash
dockerlab new <project_name>
```

Or init a dockerlab environment for the existing project:

```bash
dockerlab init .
```

This will setup a few files and directories, the structure is as follows:

```bash
.
├── docker/
│   ├── Dockerfile
│   └── misc/
├── docker-compose.yml
├── docker.py
└── .gitignore
```


**3. DIY your own workspace environment**

In general, you only need to modify `docker/Dockerfile` to customize your own workspace environment. Files you may care about:

- `docker/Dockerfile`: The dockerfile for building the docker image.
- `docker-compose.yml`: The docker-compose file for building the docker container.
- `docker.py`: The python script for building and starting the container.


We have prepared several templates and pre-built docker images for you. You can replace the default `docker/Dockerfile` with the template you like by running the following command:

```bash
dockerlab use <template_name>
```

The available templates can be listed by `dockerlab ls`, and the details of each template can be found in [dockerlab/templates](dockerlab/templates).

By default, the generated `docker/Dockerfile` will use pre-built docker images if there exists. You can also get the full dockerfile by running the following command:

```bash
dockerlab use <template_name> --full
```

**4. Build and start the container**

```bash
python docker.py startd
```

When you first execute the above command, it will ask you to enter information related to the container and store them in `.env`. The example of prompt and the output are as follows:

```bash
# prompts
Give a project name [dockerlab]: dockerlab
Code root to be mounted at /project [.]:
Data root to be mounted at /data [data]:
`/home/hongxin/code/dockerlab/data` does not exist in your machine. Create? [yes]:
Log root to be mounted at /log [log]:
`/home/hongxin/code/dockerlab/log` does not exist in your machine. Create? [yes]:
directory to be mounted to hongxin [./docker/misc/container_home]:
`/home/hongxin/code/dockerlab/container_home` does not exist in your machine. Create? [yes]:

# output
Your setting (.env):
  UID: 1000
  GID: 1000
  USER_NAME: hongxin
  PROJECT: dockerlab
  CODE_ROOT: .
  DATA_ROOT: /home/hongxin/code/dockerlab/data
  LOG_ROOT: /home/hongxin/code/dockerlab/log
  CONTAINER_HOME: /home/hongxin/code/dockerlab/container_home
  COMPOSE_PROJECT_NAME: dockerlab_hongxin
```

**5. Get in the container and start your journey.**

```bash
python docker.py
```

## License

DockerLab is released under the [MIT license](LICENSE).
