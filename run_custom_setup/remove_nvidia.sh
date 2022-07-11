#!/bin/bash

# https://askubuntu.com/questions/206283/how-can-i-uninstall-a-nvidia-driver-completely
sudo apt-get remove --purge '^.*nvidia.*'
sudo apt-get remove --purge '^libnvidia.*'
sudo apt-get install ubuntu-desktop
sudo rm /etc/X11/xorg.conf
echo 'nouveau' | sudo tee -a /etc/modules