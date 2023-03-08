<div align = center>


<h1>DockerLab</h1>

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)
[![](docs/_static/imgs/hydra.svg)](https://hydra.cc)
[![](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square&labelColor=gray)](#license)

*Build a docker container as your workspace.*


</div>

<br>

## Pre-requirements

- [Docker](https://docs.docker.com/engine/install)
- [docker-compose](https://docs.docker.com/compose/install/)



## Quick Start

**1. Clone the project to local**

```bash
git clone https://github.com/hughplay/dockerlab.git
```

**2. Modify `docker/Dockerfile`, `docker/requirements.txt`, ...**

**3. Modify `docker-compose.yml`**

**4. Build and start the container**

```bash
python docker.py startd
```

**6. Get in the container and start your journey.**

```bash
python docker.py
```

## License

DockerLab is released under the [MIT license](LICENSE).
