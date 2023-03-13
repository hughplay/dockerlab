<div align = center>


<h1>DockerLab</h1>

[![Dockerlab](https://img.shields.io/pypi/v/dockerlab?color=blue&label=dockerlab&style=flat-square)](https://pypi.org/project/dockerlab/)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)
[![](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square&labelColor=gray)](#license)

*Build a docker container as your workspace.*


</div>

<br>

## Pre-requirements

- [Docker](https://docs.docker.com/engine/install)
- [docker-compose](https://docs.docker.com/compose/install/)


## Features

- **Easy to use**: Just a few commands to build and start a docker container.
- **Customizable**: You can customize the docker image and the python packages you want to install in the container.
- **Reproducible**: You can build the same docker image on different machines. Say bye bye to the [`It works on my machine`](https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/) problem.
- **Convenient**: We made some convenient setups for you, including tools and functions:
  - [miniconda](https://docs.conda.io/en/latest/miniconda.html)
  - [oh-my-zsh](https://ohmyz.sh/)
  - [run docker within docker](https://www.docker.com/blog/docker-can-now-run-within-docker/)
  - make the user have the same uid and gid as the host (prevent permission problems)
  - mount the home of the container to the host (by hacking)
    - easy to share `~/.ssh` and `~/.gitconfig`
    - files will not be lost even if the container is removed
      - zsh history
      - configuration files
      - model checkpoints
      - etc.
  - sharing network with the host (no need extra port mapping)
  - (optional) [tmux](https://github.com/tmux/tmux/wiki)
  - (optional) [lightvim](https://github.com/hughplay/lightvim)


## Quick Start

**1. Install dockerlab**

```bash
pip install dockerlab
```

**2. Setup a dockerlab project**

Create a new dockerlab project:

```bash
dockerlab new <project_name>
```

Or init a dockerlab project in the current directory:

```bash
dockerlab init .
```

This will setup a few files and directories, the structure is as follows:

```bash
.
├── docker
│   ├── Dockerfile
│   ├── Dockerfile.full
│   ├── misc
│   │   ├── init_workspace
│   │   ├── sources.list.ubuntu18.04
│   │   └── sources.list.ubuntu20.04
│   └── requirements.txt
├── docker-compose.yml
└── docker.py
```


**3. DIY your own workspace environment**

In general, you only need to modify `docker/Dockerfile` and `requirements.txt` to customize your own workspace environment. Files you may care about:

- `docker/Dockerfile`: The dockerfile for building the docker image.
- `requirements.txt`: The python packages you want to install in the container.
- `docker-compose.yml`: The docker-compose file for building the docker container.
- `docker.py`: The python script for building and starting the container.


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
