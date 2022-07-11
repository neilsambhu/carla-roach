#!/bin/bash
DISPLAY_NUMBER=2
XSERVER_NUMBER=7

sudo rm /tmp/.X11-unix/X$DISPLAY_NUMBER
sudo rm /tmp/.X$DISPLAY_NUMBER
/opt/TurboVNC/bin/vncserver -kill :$DISPLAY_NUMBER
# sudo xfstt -deferglyphs 16
sudo nvidia-xconfig -a --use-display-device=None --virtual=1280x1024 
sudo nohup Xorg :$XSERVER_NUMBER & 
/opt/TurboVNC/bin/vncserver :$DISPLAY_NUMBER
# /opt/TurboVNC/bin/vncserver -fp /usr/share/fonts/X11/misc :$DISPLAY_NUMBER
sudo service lightdm stop
# xhost +local: 
# export DISPLAY=:$DISPLAY_NUMBER
DISPLAY=:$DISPLAY_NUMBER vglrun -d :$XSERVER_NUMBER.0 glxinfo  

# sudo -E evince
export XDG_RUNTIME_DIR=~github/carla-roach/runtime/
# DISPLAY=:8 vglrun -d :$XSERVER_NUMBER.0 $CARLA_ROOT/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping
# DISPLAY=:8 vglrun -d :$XSERVER_NUMBER.0 ${CARLA_ROOT}/CarlaUE4.sh
python -u run/train_rl_parent_NeilBranch0.py>out.txt