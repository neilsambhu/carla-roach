#!/bin/bash
IMAGE_NAME="ubuntu:18.04"
CONTAINER_NAME="ubuntu-carla"
TAR_NAME="ubuntu-carla-archive.tar"

# cleanup
podman kill --signal KILL -a && \
podman container cleanup --all --rm && \
# podman rmi docker.io/library/$IMAGE_NAME

# 2/6/2023 4:18:05 PM: call Dockerfile
podman build -t $IMAGE_NAME .
# 2/7/2023 11:50:02 AM: run image
podman run -d -it --name $CONTAINER_NAME docker.io/library/$IMAGE_NAME
podman attach $CONTAINER_NAME

# 2/7/2023 12:03:27 PM: write ~/example.txt file

# 2/7/2023 12:03:41 PM: save to hard disk
# podman commit $CONTAINER_NAME $IMAGE_NAME
# podman export $CONTAINER_NAME > $TAR_NAME
# podman save $IMAGE_NAME > $TAR_NAME