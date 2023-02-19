#!/bin/bash
IMAGE_NAME="ubuntu:18.04"
CONTAINER_NAME="ubuntu-carla"
TAR_NAME="ubuntu-carla-archive.tar"

# 2/7/2023 12:52:17 PM: load image from tar file
# podman load < $TAR_NAME
# 2/7/2023 12:52:31 PM: run
# podman run -d -it --name $CONTAINER_NAME docker.io/library/$IMAGE_NAME
# podman run -d -it --name $CONTAINER_NAME --user nsambhu docker.io/library/$IMAGE_NAME
# 2/10/2023 11:49:08 AM: try GPU
# podman run -d -it --name $CONTAINER_NAME --runtime=nvidia --user nsambhu docker.io/library/$IMAGE_NAME
# podman run -d -it --name $CONTAINER_NAME --user nsambhu --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all docker.io/library/$IMAGE_NAME
podman run --name $CONTAINER_NAME --security-opt=label=disable --hooks-dir=/usr/share/containers/oci/hooks.d/ -e NVIDIA_VISIBLE_DEVICES=0 docker.io/library/$IMAGE_NAME /opt/carla-simulator/CarlaUE4.sh

# 2/10/2023 11:48:57 AM: attach to container
# podman attach $CONTAINER_NAME