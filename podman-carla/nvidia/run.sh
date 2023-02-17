#!/bin/bash
IMAGE_NAME="cuda:12.0.1-runtime-ubuntu18.04"
CONTAINER_NAME="ubuntu-nvidia"
TAR_NAME="ubuntu-nvidia-archive.tar"

# cleanup
podman kill --signal KILL -a && \
podman container cleanup --all --rm && \
# podman rmi docker.io/library/$IMAGE_NAME

# 2/6/2023 4:18:05 PM: call Dockerfile
podman build -t $IMAGE_NAME .
# 2/7/2023 11:50:02 AM: run image
# podman run -d -it --name $CONTAINER_NAME nvidia/$IMAGE_NAME
podman run --runtime=nvidia --gpus all -d -it --name $CONTAINER_NAME nvidia/$IMAGE_NAME
# podman run --rm --runtime=nvidia --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
podman attach $CONTAINER_NAME

# 2/7/2023 12:03:27 PM: write ~/example.txt file

# 2/7/2023 12:03:41 PM: save to hard disk
# podman commit $CONTAINER_NAME $IMAGE_NAME
# podman export $CONTAINER_NAME > $TAR_NAME
# podman save $IMAGE_NAME > $TAR_NAME