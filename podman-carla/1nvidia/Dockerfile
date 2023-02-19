FROM cuda:12.0.1-runtime-ubuntu18.04
# COPY . /app

#
# Python3.8 install for Ubuntu
#
# ref: https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/
# RUN apt-get update
# RUN apt-get install -y software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt-get install -y python3.8 python3-pip
# Update symlink to point to latest
# RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python3
# RUN python3 --version
# RUN pip3 --version

# 2/6/2023 4:14:04 PM: disk modification: start
# CMD touch ~/example.txt
# 2/6/2023 4:14:04 PM: disk modification: end

# 2/7/2023 1:16:09 PM: carla install
# RUN apt-get update 
# RUN apt-get install wget software-properties-common
# RUN add-apt-repository ppa:ubuntu-toolchain-r/test
# RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - 
# RUN apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main" 
# RUN apt-get update 
# RUN apt-get install build-essential clang-8 lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git 
# RUN update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 
# RUN update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180 
# RUN pip3 install --upgrade pip 
# RUN pip3 install --user pygame numpy