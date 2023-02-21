FROM nvidia/vulkan:1.1.121-cuda-10.1--ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

# 2/21/2023 4:08:06 PM: file system debug: start
# RUN pwd
# RUN ls
# WORKDIR /bin
# RUN pwd
# RUN ls
# 2/21/2023 4:08:06 PM: file system debug: end

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
RUN apt-get update
RUN apt-get install -y wget software-properties-common
# 2/20/2023 3:52:11 PM: debug python 3.7: start
# RUN apt-cache search python3
RUN python3 -V
# 2/20/2023 3:52:11 PM: debug python 3.7: end
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add -
RUN apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main"
RUN apt-get update

# 2/20/2023 3:27:57 PM: Debug: start
RUN apt-get install -y python3.7
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
RUN update-alternatives --config python3
RUN python3 -V
# 2/20/2023 3:27:57 PM: Debug: end
RUN apt-get install -y build-essential clang-8 lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git
RUN update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180
RUN update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180

RUN pip3 -V

RUN pip3 install --upgrade pip

RUN pip install --user setuptools
RUN pip3 install --user -Iv setuptools==47.3.1
RUN pip install --user distro
RUN pip3 install --user distro
RUN pip install --user wheel
RUN pip3 install --user wheel auditwheel

# 2/21/2023 12:55:25 PM: git debug: start
# RUN git config --global user.name "Neil Sambhu"
# RUN git config --global user.name
# RUN git config --global user.email "neilsambhu@gmail.com"
# RUN git config --global user.email
# RUN eval "$(ssh-agent -s)"
# RUN ls ~/.ssh/
# COPY id_rsa 
# 2/21/2023 12:55:25 PM: git debug: start

# RUN git clone --depth 1 -b carla https://github.com/CarlaUnreal/UnrealEngine.git ~/UnrealEngine_4.26

# 2/21/2023 3:41:31 PM: git replacement line: start
# RUN pwd
# WORKDIR $HOME
# RUN pwd
# RUN ls
COPY ./UnrealEngine_4.26 $HOME/UnrealEngine_4.26
# RUN ls
# RUN ls /UnrealEngine_4.26
# 2/21/2023 3:41:31 PM: git replacement line: end

WORKDIR $HOME/UnrealEngine_4.26
RUN ./Setup.sh && ./GenerateProjectFiles.sh && make
RUN cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor

# RUN apt-key adv --fetch-keys "https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub" \
#     && apt-get update \
#     && apt-get install -y software-properties-common wget \
#     && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1AF1527DE64CB8D9 \
#     && add-apt-repository "deb [arch=amd64] http://dist.carla.org/carla bionic main" \
#     && apt-get update \
#     && apt-get install -y carla-simulator libomp5 libsdl2-2.0 xserver-xorg libvulkan1 vulkan-utils \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /opt/carla-simulator

# COPY /home/nsambhu/data1/carla_install/Import/AdditionalMaps_0.9.13.tar.gz /opt/carla-simulator/Import/AdditionalMaps_0.9.13.tar.gz
# COPY /home/nsambhu/data1/carla_install/Import/CARLA_0.9.13.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13.tar.gz
# COPY /home/nsambhu/data1/carla_install/Import/CARLA_0.9.13_RSS.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13_RSS.tar.gz

# RUN bash /opt/carla-simulator/ImportAssets.sh \
#     && rm -v /opt/carla-simulator/Import/AdditionalMaps_0.9.13.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13.tar.gz /opt/carla-simulator/Import/CARLA_0.9.13_RSS.tar.gz

# RUN groupadd -g 1000 nsambhu 
# RUN useradd -d /home/nsambhu -s /bin/bash -m nsambhu -u 1000 -g 1000 
# USER nsambhu 
# ENV HOME /home/nsambhu 

# CMD ["bash","/opt/carla-simulator/CarlaUE4.sh"]