<div align = center>


<h1>DockerLab</h1>

[![Package Building Status](https://img.shields.io/github/actions/workflow/status/hughplay/dockerlab/poetry-publish.yml?label=Package%20Build&style=flat-square)](https://github.com/hughplay/dockerlab/actions)
[![pypi](https://img.shields.io/pypi/v/dockerlab?color=blue&label=pypi&style=flat-square)](https://pypi.org/project/dockerlab/)
[![Image Building Status](https://img.shields.io/github/actions/workflow/status/hughplay/dockerlab/images-build.yml?label=Image%20Build&style=flat-square)](https://github.com/hughplay/dockerlab/actions)
[![](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square&labelColor=gray)](#license)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)](https://docs.docker.com/engine/)

*用Docker搭建你的工作区。*



</div>

<br>

Read this in [English](README.en.md).

## 环境要求

- [Docker](https://docs.docker.com/engine/install)


## 特点

- **易于使用**：只需几个命令即可构建和启动 Docker 容器。
- **可定制**：可以自定义要安装在容器中的 Docker 镜像和 Python 包。
- **可重现**：可以在不同的计算机上构建相同的 Docker 镜像。告别[“这在我的机器上可以运行”](https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/)的问题。
- **方便**：Dockerlab提供了一些方便的设置，包括工具和功能：
  - 工具：[oh-my-zsh](https://ohmyz.sh/)，[docker within docker](https://www.docker.com/blog/docker-can-now-run-within-docker/)，[tmux](https://github.com/tmux/tmux/wiki)，[lightvim](https://github.com/hughplay/lightvim)
  - 解决权限问题：与主机相同的 uid 和 gid。
  - 将 $HOME 目录从容器反向挂载到主机
    - 轻松共享 `~/.ssh` 和 `~/.gitconfig`
    - 即使删除容器，配置文件也不会丢失，例如：zsh历史记录、配置文件、模型检查点等
  - 解决端口映射问题：与主机共享网络
- **预构建镜像**：Dockerlab提供了几个基本的[预构建镜像](dockerlab/templates/)，可快速设置工作区环境。


## 快速开始

**1. 安装dockerlab**

用pip安装dockerlab：

```bash
pip install dockerlab
```

或者从源码安装最新版本：

```bash
pip install git+https://github.com/hughplay/dockerlab.git
```


**2. 设置dockerlab项目**

创建一个新的dockerlab项目：

```bash
dockerlab new <project_name>
```

或者为现有项目初始化一个dockerlab环境：

```bash
dockerlab init .
```

这将设置一些文件和目录，其结构如下：

```bash
.
├── docker/
│   ├── Dockerfile
│   └── misc/
├── docker-compose.yml
├── docker.py
└── .gitignore
```


**3. 自定义工作环境**

通常情况下，只需要修改`docker/Dockerfile`文件来自定义自己的工作环境。可能关心的文件:

- `docker/Dockerfile`: 用于构建docker镜像的dockerfile。
- `docker-compose.yml`: 用于构建docker容器的docker-compose文件。
- `docker.py`: 用于构建和启动容器的python脚本。


dockerlab准备了几个模板和预构建的docker镜像。可以通过运行以下命令将默认的`docker/Dockerfile`替换为需要的模板:

```bash
dockerlab use <template_name>
```

可用的模板可以通过 `dockerlab ls`列出，每个模板的详细信息可以在[dockerlab/templates](dockerlab/templates)找到。

默认情况下，生成的`docker/Dockerfile`将使用预构建的docker镜像（如果存在）。也可以通过运行以下命令获取完整的dockerfile：

```bash
dockerlab use <template_name> --full
```

**4. 构建和启动容器**

```bash
python docker.py startd
```

当你第一次执行上述命令时，它将要求你输入与容器相关的信息，并将它们存储在`.env`中。提示和输出示例如下：

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

**5. 进入容器开启旅程**


```bash
python docker.py
```

## 许可证

Dockerlab使用[MIT许可证](LICENSE)。
