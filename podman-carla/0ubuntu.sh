#!/bin/bash
podman kill --signal KILL -a && \
podman container cleanup --all --rm

CONTAINER_NAME="mycontainer"
podman container create -i -t --name $CONTAINER_NAME ubuntu:18.04
podman container start --attach -i $CONTAINER_NAME
# Install CARLA 0.9.13
# Use Ctrl+P+Q to detach 

# Save to hard disk
# podman save docker.io/library/ubuntu:18.04 > $CONTAINER_NAME.tar
# podman save --output $CONTAINER_NAME.tar ubuntu:18.04
