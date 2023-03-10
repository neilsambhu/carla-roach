#!/bin/bash
podman build -t usf_nsambhu_carla_source /home/nsambhu/github/carla-roach/podman-carla/7ubuntu-jennifer4/build-env
podman stop usf_nsambhu_carla_build
podman rm usf_nsambhu_carla_build
podman run -it --rm --security-opt label=disable -v /data/data1/podman_storage_hdd:/usr/src/app --entrypoint='/bin/bash' --name=usf_nsambhu_carla_build usf_nsambhu_carla_source /usr/src/install/install.sh
