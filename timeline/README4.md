7/7/2022 5:01 PM: 
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ python -u run/train_rl_parent_NeilBranch0.py>out.txt
```
```
grep -r  --exclude *README1.md--exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb "num_timesteps.txt">outgrep.txt
```
7/7/2022 5:35 PM: change Python from 3.8 to 3.7

7/10/2022 2:08 PM: CARLA will only run with "-RenderOffScreen" flag. 

# Notes for CARLA setup with Daniel
7/14/2022 4:15 PM: on USB boot, nomodeset

7/13/2020: 
```
blk id
```

7/13/2022 7:37 PM: (for Red Hat Enterprise Linux)
```
sudo apt install gparted
```
Bootloader (500 MB): EFI System Partition  
OS (200 GB): Ext4. Mount at "/" (i.e. "root")  
Home: Ext4. Mount at "/home"  

7/31/2022 7:58 PM: Ubuntu 18.04 installed
```
sudo apt update
sudo apt upgrade
```

7/13/2022 7:59 PM: CUDA Toolkit: deb (network)

7/13/2022 8:13 PM: install Anaconda

7/13/2022 8:15 PM: create conda environment with Python 3.7

7/13/2022 8:16 PM: install pygame
```
pip install pygame numpy
```
7/13/2022 8:16 PM: Debian CARLA installation

apt is good for user (i.e. human readable). apt-get is good for piping into other programs.

7/14/2022 11:31 AM: 
```
/opt
chmod -R 777 carla-simulator
```
7/14/2022 11:32 AM: copy 3 additional assets into "Import" directory
```
mv ~/Downloads/AdditionalMaps_0.9.13.tar.gz /opt ...
```
7/14/2022 11:36 AM: run import assets script

7/14/2022 11:37 AM: 
```
pip install carla
```
7/14/2022 11:37 AM: in Python examples, install requirements.txt
```
pip install -r requirements.txt
```
7/14/2022 11:39 AM:
```
sudo apt install libomp5
```
7/14/2022 11:40 AM: running CARLA failed with window global shader cache file is missing.

7/14/2022 11:44 AM:
```
sudo apt install vulkan-utils
```
7/14/2022 6:36 PM: HDD symbolic link
```
(base) nsambhu@SAMBHU19:/media/nsambhu/data1/carla_install$ cd /
(base) nsambhu@SAMBHU19:/$ sudo mkdir data
[sudo] password for nsambhu: 
(base) nsambhu@SAMBHU19:/$ cd d
data/ dev/  
(base) nsambhu@SAMBHU19:/$ cd data/
(base) nsambhu@SAMBHU19:/data$ sudo mkdir data1
```
```
(base) nsambhu@SAMBHU19:/data$ sudo blkid
 UUID="b1465c28-6bc1-4531-829c-6576c028703f" TYPE="ext4" PARTLABEL="data1" PARTUUID="fe5be838-dd78-461f-82ed-854ffabb9a3e"
```
```
(base) nsambhu@SAMBHU19:/data$ sudo vim /etc/fstab
```
```
# data1 mount point /data/data1
UUID="b1465c28-6bc1-4531-829c-6576c028703f" /data/data1 ext4 defaults 0 0
```
```
(base) nsambhu@SAMBHU19:/data$ sudo mount -a
(base) nsambhu@SAMBHU19:/data$ ln -s /data/data1/ ~
```