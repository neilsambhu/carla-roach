#!/bin/bash
IMAGE_NAME="ubuntu:18.04"
CONTAINER_NAME="ubuntu-carla"
TAR_NAME="ubuntu-carla-archive.tar"

# 2/8/2023 12:34:45 PM: get user
# podman exec $CONTAINER_NAME sh -c "whoami"
# podman exec $CONTAINER_NAME whoami && su nsambhu && whoami

# 2/8/2023 12:38:22 PM: switch user
# podman exec $CONTAINER_NAME "su nsambhu"

# 2/8/2023 12:38:53 PM: get user
# podman exec $CONTAINER_NAME "whoami"

# 2/9/2023 12:00:50 PM: test if changes to container exist between exec statements 
# podman exec $CONTAINER_NAME sh -c "pwd"
# podman exec $CONTAINER_NAME sh -c "cd /opt/carla-simulator"
# podman exec $CONTAINER_NAME sh -c "pwd"
# 2/9/2023 12:02:50 PM: changes do not persist

# 2/9/2023 12:00:12 PM: get to /opt/carla-simulator
# podman exec $CONTAINER_NAME sh -c "./opt/carla-simulator/CarlaUE4.sh"

# 2/9/2023 12:50:02 PM: how to run carla container
# podman run --privileged --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
# 2/9/2023 12:50:44 PM: run ubuntu container carla
xhost local:root
podman run --privileged --net=host -e DISPLAY=$DISPLAY --user nsambhu $IMAGE_NAME /bin/bash ./opt/carla-simulator/CarlaUE4.sh