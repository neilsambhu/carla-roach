#!/bin/bash
IMAGE_NAME="vulkan:1.1.121-cuda-10.1--ubuntu18.04"
CONTAINER_NAME="ubuntu-jennifer2"
TAR_NAME="ubuntu-jennifer-archive.tar"

# cleanup
# podman kill --signal KILL -a && \
# podman container cleanup --all --rm && \
# podman rmi -f docker.io/nvidia/$IMAGE_NAME && \
# podman image prune --filter="dangling=true" -f

# 2/6/2023 4:18:05 PM: call Dockerfile
podman build -t $IMAGE_NAME .
# 2/7/2023 11:50:02 AM: run image
# podman run -d -it --name $CONTAINER_NAME nvidia/$IMAGE_NAME
# podman run --runtime=nvidia --gpus all -d -it --name $CONTAINER_NAME nvidia/$IMAGE_NAME
# podman run --rm --runtime=nvidia --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
# podman attach $CONTAINER_NAME

# xhost + ; podman run -it --rm --runtime=nvidia --gpus='"device=1","capabilities=graphics,utility,display,video,compute"' --name $CONTAINER_NAME -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=:2.0 nvidia/$IMAGE_NAME
xhost local:root
podman run --name $CONTAINER_NAME -d --privileged --net=host -e DISPLAY=$DISPLAY docker.io/nvidia/$IMAGE_NAME
# podman attach $CONTAINER_NAME

# 2/7/2023 12:03:27 PM: write ~/example.txt file

# 2/7/2023 12:03:41 PM: save to hard disk
# podman commit $CONTAINER_NAME $IMAGE_NAME
# podman export $CONTAINER_NAME > $TAR_NAME
# podman save $IMAGE_NAME > $TAR_NAME