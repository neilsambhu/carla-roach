FROM nvidia/vulkan:1.1.121-cuda-10.1--ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-key adv --fetch-keys "https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub" \
    && apt-get update \
    && apt-get install -y software-properties-common wget \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1AF1527DE64CB8D9 \
    && add-apt-repository "deb [arch=amd64] http://dist.carla.org/carla bionic main" \
    && apt-get update \
    && apt-get install -y carla-simulator libomp5 libsdl2-2.0 xserver-xorg libvulkan1 vulkan-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/carla-simulator

COPY /home/nsambhu/data1/carla_install/Import/AdditionalMaps_0.9.13.tar.gz /opt/carla-simulator/Import/AdditionalMaps_0.9.13.tar.gz
COPY /home/nsambhu/data1/carla_install/Import/CARLA_0.9.13.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13.tar.gz
COPY /home/nsambhu/data1/carla_install/Import/CARLA_0.9.13_RSS.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13_RSS.tar.gz

RUN bash /opt/carla-simulator/ImportAssets.sh \
    && rm -v /opt/carla-simulator/Import/AdditionalMaps_0.9.13.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13_RSS.tar.gz

RUN groupadd -g 1000 nsambhu 
RUN useradd -d /home/nsambhu -s /bin/bash -m nsambhu -u 1000 -g 1000 
USER nsambhu 
ENV HOME /home/nsambhu 

CMD ["bash","/opt/carla-simulator/CarlaUE4.sh"]