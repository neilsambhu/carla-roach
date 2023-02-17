#!/bin/bash
podman kill --signal KILL -a
# podman container cleanup --all --rm

CONTAINER_NAME="mycontainer2"
xhost local:root
podman container create -i -t --name $CONTAINER_NAME carlasim/carla:0.9.13
# podman container start --privileged --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
podman container start --attach -i $CONTAINER_NAME
# Install CARLA 0.9.13
# Use Ctrl+P+Q to detach 

# Save to hard disk
# podman save docker.io/library/ubuntu:18.04 > $CONTAINER_NAME.tar