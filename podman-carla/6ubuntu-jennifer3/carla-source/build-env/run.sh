#!/bin/bash
podman build -t usf_nsambhu_carla_source /home/nsambhu/github/carla-roach/podman-carla/6ubuntu-jennifer3/carla-source/build-env
podman stop usf_nsambhu_carla_build
podman rm usf_nsambhu_carla_build
xhost +
podman run -it --rm --privileged --net=host -e DISPLAY=$DISPLAY -v /data/data1/podman_storage_hdd:/usr/src/app --entrypoint='/bin/bash' --name=usf_nsambhu_carla_build usf_nsambhu_carla_source
