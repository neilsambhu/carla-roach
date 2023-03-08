#!/bin/bash
podman build -t usf_nsambhu_carla_source /home/nsambhu/github/carla-roach/podman-carla/6ubuntu-jennifer3/carla-source/build-env
podman run -it --rm -v /data/data1/podman_storage_hdd:/usr/src/app --entrypoint='/bin/bash' --name=usf_nsambhu_carla_build usf_nsambhu_carla_source /usr/src/install/script.sh