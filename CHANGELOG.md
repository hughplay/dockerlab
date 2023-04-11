# Changelog


## TODO

- build docker images to dockerhub
  - [ ] copy extra files
  - [ ] plot the logic of template assembly

## 0.3

- templates
  - [x] assemble Dockerfiles
    - [x] with pre-built images
    - [x] full Dockerfiles
  - [x] build docker images to dockerhub
    - matrix: https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs
      - `max_parallel: 1` for sequential builds
  - [x] pre-commit

## 0.2 (last update: 2023-03-20)

- [x] implement the cli
  - `new/init`: copy essential files into a new directory
- [x] github workflow
