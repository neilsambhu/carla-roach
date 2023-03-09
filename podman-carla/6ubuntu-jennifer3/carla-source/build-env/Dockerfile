FROM nvidia/vulkan:1.1.121-cuda-10.1--ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-key adv --fetch-keys "https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub" \
    && apt update && apt upgrade -y \
    && apt-get install -y --no-install-recommends software-properties-common build-essential clang-8 \
     lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip \ 
     libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git \
     libomp5 libsdl2-2.0 xserver-xorg vulkan-utils \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 \
    && update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
    && pip install --upgrade pip \
    && pip install setuptools \
    && pip3 install -Iv setuptools==47.3.1 \
    && pip install distro \
    && pip3 install distro \
    && pip install wheel \
    && pip3 install wheel auditwheel

COPY UnrealEngine.zip /usr/src/install/UnrealEngine.zip
COPY install.sh /usr/src/install/install.sh

WORKDIR /usr/src/app

RUN groupadd -g 1000 nsambhu
RUN useradd -s /bin/bash -m nsambhu -u 1000 -g 1000
