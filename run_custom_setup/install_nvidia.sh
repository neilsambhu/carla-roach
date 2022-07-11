#!/bin/bash

# BASE_URL=https://us.download.nvidia.com/tesla
# DRIVER_VERSION=384.11
# curl -fSsl -O $BASE_URL/$DRIVER_VERSION/NVIDIA-Linux-x86_64-$DRIVER_VERSION.run
# sudo sh NVIDIA-Linux-x86_64-$DRIVER_VERSION.run

# sudo apt-get purge nvidia*
# sudo apt-get install --reinstall xserver-xorg-video-intel libgl1-mesa-glx libgl1-mesa-dri xserver-xorg-core
# sudo dpkg-reconfigure xserver-xorg

# sudo ln -s /usr/lib/mesa-diverted/x86_64-linux-gnu/libGL.so.1 /usr/lib/libGL.so.1
# sudo rm /usr/lib/i386-linux-gnu/libGL.so.1
# sudo ln -s /usr/lib/mesa-diverted/i386-linux-gnu/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so.1

sudo apt purge nvidia
sudo rm /etc/X11/Xorg.conf
sudo apt autoremove
dpkg -l | awk '/^rc/{print $2}' | xargs sudo dpkg -P
sudo apt update
sudo ubuntu-drivers autoinstall