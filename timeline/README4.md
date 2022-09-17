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

~7/13/2020:~  
~blk id~

8/1/2022 4:52 PM:
```
blkid
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
# Continue CARLA install debugging
7/18/2022 11:39 AM: 
```
(base) nsambhu@SAMBHU19:/opt/carla-simulator$ ./CarlaUE4.sh
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Signal 11 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
CommonUnixCrashHandler: Signal=11
Malloc Size=131160 LargeMemoryPoolOffset=196744 
Malloc Size=131160 LargeMemoryPoolOffset=327928 
Engine crash handling finished; re-raising signal 11 for the default handler. Good bye.
Segmentation fault (core dumped)
```
```
(base) nsambhu@SAMBHU19:/opt/carla-simulator$ ./CarlaUE4.sh -RenderOffScreen
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
```
7/18/2022 12:03 PM: try to re-install CARLA with keeping the "pip install" commands separate.  
7/18/2022 12:33 PM: still failed.

# Try running CARLA-Roach
7/18/2022 12:58 PM:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ python -u run/train_rl_parent_NeilBranch0.py>out.txt
```
7/18/2022 12:58 PM:
```
wandb login
```
https://wandb.ai/authorize  
7/18/2022 12:58 PM: 
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


train_rl_NeilBranch0.py:19: UserWarning: 
The version_base parameter is not specified.
Please specify a compatability version level, or None.
Will assume defaults for version 1.1
  @hydra.main(config_path='config', config_name='train_rl')
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/defaults_list.py:251: UserWarning: In 'train_rl': Defaults list is missing `_self_`. See https://hydra.cc/docs/upgrades/1.0_to_1.1/default_composition_order for more information
  warnings.warn(msg, UserWarning)
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'train_envs/endless_all': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/training/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py:127: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/next/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  configure_logging=with_log_configuration,
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
a
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:34: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize("%s: %s" % ("WARN", msg % args), "yellow"))
wandb: Currently logged in as: neilsambhu. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.12.21
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-07-18/12-57-22/wandb/run-20220718_125740-145iz2ht
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/145iz2ht
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
Error executing job with overrides: ['agent.ppo.wb_run_path=null', 'wb_project=train_rl_experts', 'wb_name=roach', 'agent/ppo/policy=xtma_beta', 'agent.ppo.training.kwargs.explore_coef=0.05', 'carla_sh_path=/opt/carla-simulator/CarlaUE4.sh']
An error occurred during Hydra's exception formatting:
AssertionError()
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 254, in run_and_report
    assert mdl is not None
AssertionError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 168, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 296, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 132, in run
    _ = ret.return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 260, in return_value
    raise self._return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
  File "train_rl_NeilBranch0.py", line 160, in main
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/rl_birdview_agent.py", line 275, in learn
    model.learn(total_timesteps, callback=callback, seed=seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/models/ppo.py", line 236, in learn
    callback.init_callback(self)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/stable_baselines3/common/callbacks.py", line 47, in init_callback
    self.logger = model.logger
AttributeError: 'PPO' object has no attribute 'logger'
wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb:                                                                                
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/145iz2ht
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: Find logs at: ./outputs/2022-07-18/12-57-22/wandb/run-20220718_125740-145iz2ht/logs
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
# 2022 07 26 1:36 PM: to Daniel:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


train_rl_NeilBranch0.py:19: UserWarning: 
The version_base parameter is not specified.
Please specify a compatability version level, or None.
Will assume defaults for version 1.1
  @hydra.main(config_path='config', config_name='train_rl')
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/defaults_list.py:251: UserWarning: In 'train_rl': Defaults list is missing `_self_`. See https://hydra.cc/docs/upgrades/1.0_to_1.1/default_composition_order for more information
  warnings.warn(msg, UserWarning)
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'train_envs/endless_all': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/training/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py:127: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/next/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  configure_logging=with_log_configuration,
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
Signal 11 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
Malloc Size=131160 LargeMemoryPoolOffset=196744 
Malloc Size=131160 LargeMemoryPoolOffset=327928 
/opt/carla-simulator/CarlaUE4.sh: line 2: 18914 Segmentation fault      (core dumped) "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
```
# 2022 07 27 1:12 PM: to Daniel:
```
(carla) nsambhu@SAMBHU19:/opt/carla-simulator$ bash CarlaUE4.sh 
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Signal 11 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
CommonUnixCrashHandler: Signal=11
Malloc Size=131160 LargeMemoryPoolOffset=196744 
Malloc Size=131160 LargeMemoryPoolOffset=327928 
Engine crash handling finished; re-raising signal 11 for the default handler. Good bye.
CarlaUE4.sh: line 2: 51975 Segmentation fault      (core dumped) "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
```
# 2022 08 01 2:39 PM: to Daniel:
7/31/2022: I reinstalled Ubuntu 18.04 on SAMBHU19: (1) deselect download 18.04 updates and (2) select third-party drivers.  
```
(carla) nsambhu@SAMBHU19:/opt/carla-simulator/PythonAPI/examples$ sudo apt install vulkan-utils
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  vulkan-utils
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 88.7 kB of archives.
After this operation, 314 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 vulkan-utils amd64 1.1.70+dfsg1-1ubuntu0.18.04.1 [88.7 kB]
Fetched 88.7 kB in 0s (401 kB/s)        
Selecting previously unselected package vulkan-utils.
(Reading database ... 212283 files and directories currently installed.)
Preparing to unpack .../vulkan-utils_1.1.70+dfsg1-1ubuntu0.18.04.1_amd64.deb ...
Unpacking vulkan-utils (1.1.70+dfsg1-1ubuntu0.18.04.1) ...
Setting up vulkan-utils (1.1.70+dfsg1-1ubuntu0.18.04.1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
(carla) nsambhu@SAMBHU19:/opt/carla-simulator$ bash CarlaUE4.sh 
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
(carla) nsambhu@SAMBHU19:/opt/carla-simulator$ sudo apt install vulkan-utils
Reading package lists... Done
Building dependency tree       
Reading state information... Done
vulkan-utils is already the newest version (1.1.70+dfsg1-1ubuntu0.18.04.1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
(carla) nsambhu@SAMBHU19:/opt/carla-simulator$ bash CarlaUE4.sh 
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
(carla) nsambhu@SAMBHU19:/opt/carla-simulator$ 
```
There is an error message window pop-up about vulkan-utils not being installed when I run CARLA.  
8/1/2022 2:42 PM: TODO: reboot SAMBHU19  
8/1/2022 2:47 PM: 
```
(carla) nsambhu@SAMBHU19:/opt/carla-simulator$ bash CarlaUE4.sh 
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Signal 11 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
CommonUnixCrashHandler: Signal=11
Malloc Size=131160 LargeMemoryPoolOffset=196744 
Malloc Size=131160 LargeMemoryPoolOffset=327928 
Engine crash handling finished; re-raising signal 11 for the default handler. Good bye.
CarlaUE4.sh: line 2:  2911 Segmentation fault      (core dumped) "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
```
8/1/2022 2:57 PM: I tried running CARLA with vulkan: 
```
(carla) nsambhu@SAMBHU19:/media/nsambhu/data1/carla_install$ cat run_carla.sh 
/opt/carla-simulator/CarlaUE4.sh -vulkan
(carla) nsambhu@SAMBHU19:/media/nsambhu/data1/carla_install$ bash run_carla.sh 
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Signal 11 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
CommonUnixCrashHandler: Signal=11
Malloc Size=131160 LargeMemoryPoolOffset=196744 
Malloc Size=131160 LargeMemoryPoolOffset=327928 
Engine crash handling finished; re-raising signal 11 for the default handler. Good bye.
Segmentation fault (core dumped)
```
The opengl flag is not supported.

# 2022 08 01: CARLA setup with Daniel Sawyer
```
sudo chown -R $USER:$USER /opt/carla-simulator
sudo chmod -R 777 /opt/carla-simulator
```
#install CARLA  
deactivate conda (1) carla and (2) base environments

# 2022 08 02 Daniel Sawyer: restore root directory from backup on HDD
Preface: (1) boot from USB and (2) nomodeset  
8/2/2022 11:13:17 AM:  
```
blkid
```
/dev/nvme0n1p2 is system / partition  
/dev/sda1 is data1 partition  
mount data1:
```
mkdir data1
sudo mount -t ext4 /dev/sda1 ~/data1/
ls data1/
sudo dd if=~/data1/ubuntu_carla0-backup.img of=/dev/nvme0n1p2 status=progress
```
check for errors on the image:
```
sudo mount -t ext4 data1/ubuntu_carla0-backup.img test/
ls test
sudo umount test
ls test
```
reboot regular (i.e. not from USB)

# 2022 08 02 Daniel Sawyer: backup root directory to HDD
8/2/2022 1:03:11 PM: 
```
sudo blkid
```
```
sudo dd if=/dev/nvme0n1p2 of=/data/data1/ubuntu_carla0_teamviewer-backup.img status=progress
```

# 2022 08 05
Daniel Sawyer updated apt, installed sublime, vim, and OpenSSH. Daniel Sawyer performed the backup.  

8/5/2022 2:51:45 PM: update ~/.bashrc
8/5/2022 2:55:13 PM: 
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


train_rl_NeilBranch0.py:19: UserWarning: 
The version_base parameter is not specified.
Please specify a compatability version level, or None.
Will assume defaults for version 1.1
  @hydra.main(config_path='config', config_name='train_rl')
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/defaults_list.py:251: UserWarning: In 'train_rl': Defaults list is missing `_self_`. See https://hydra.cc/docs/upgrades/1.0_to_1.1/default_composition_order for more information
  warnings.warn(msg, UserWarning)
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'train_envs/endless_all': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/training/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py:127: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/next/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  configure_logging=with_log_configuration,
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:34: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize("%s: %s" % ("WARN", msg % args), "yellow"))
wandb: Currently logged in as: neilsambhu. Use `wandb login --relogin` to force relogin
wandb: wandb version 0.13.0 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.12.21
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-08-05/14-52-49/wandb/run-20220805_145304-st1yut2a
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/st1yut2a
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
Error executing job with overrides: ['agent.ppo.wb_run_path=null', 'wb_project=train_rl_experts', 'wb_name=roach', 'agent/ppo/policy=xtma_beta', 'agent.ppo.training.kwargs.explore_coef=0.05', 'carla_sh_path=/opt/carla-simulator/CarlaUE4.sh']
An error occurred during Hydra's exception formatting:
AssertionError()
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 254, in run_and_report
    assert mdl is not None
AssertionError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 168, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 296, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 132, in run
    _ = ret.return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 260, in return_value
    raise self._return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
  File "train_rl_NeilBranch0.py", line 160, in main
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/rl_birdview_agent.py", line 275, in learn
    model.learn(total_timesteps, callback=callback, seed=seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/models/ppo.py", line 236, in learn
    callback.init_callback(self)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/stable_baselines3/common/callbacks.py", line 47, in init_callback
    self.logger = model.logger
AttributeError: 'PPO' object has no attribute 'logger'
wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb:                                                                                
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/st1yut2a
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: Find logs at: ./outputs/2022-08-05/14-52-49/wandb/run-20220805_145304-st1yut2a/logs
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ /opt/carla-simulator/CarlaUE4.sh: line 2: 13828 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
```
8/6/2022 4:03:18 PM: TODO: find line number of hydra error  
8/6/2022 4:14:20 PM: TODO: find how to specify hydra version. Possibility: option in config/train_rl.yaml file.  
8/6/2022 6:37:23 PM: hydra version 1.2 and HYDRA_FULL_ERROR=1
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/defaults_list.py:251: UserWarning: In 'train_rl': Defaults list is missing `_self_`. See https://hydra.cc/docs/upgrades/1.0_to_1.1/default_composition_order for more information
  warnings.warn(msg, UserWarning)
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 520, in _compose_config_from_defaults_list
    cfg.merge_with(loaded.config)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 490, in merge_with
    self._format_and_raise(key=None, value=None, cause=e)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/base.py", line 237, in _format_and_raise
    type_override=type_override,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 873, in format_and_raise
    _raise(ex, cause)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 771, in _raise
    raise ex.with_traceback(sys.exc_info()[2])  # set env var OC_CAUSE=1 for full trace
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 488, in merge_with
    self._merge_with(*others)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 512, in _merge_with
    BaseContainer._map_merge(self, other)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 397, in _map_merge
    dest_node._merge_with(src_node)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 516, in _merge_with
    raise TypeError("Cannot merge DictConfig with ListConfig")
omegaconf.errors.ConfigTypeError: Cannot merge DictConfig with ListConfig
    full_key: 
    object_type=dict

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 216, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 109, in run
    run_mode=RunMode.RUN,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 599, in compose_config
    validate_sweep_overrides=validate_sweep_overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 146, in load_configuration
    validate_sweep_overrides=validate_sweep_overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 253, in _load_configuration_impl
    defaults=defaults_list.defaults, repo=caching_repo
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 524, in _compose_config_from_defaults_list
    ).with_traceback(sys.exc_info()[2])
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 520, in _compose_config_from_defaults_list
    cfg.merge_with(loaded.config)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 490, in merge_with
    self._format_and_raise(key=None, value=None, cause=e)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/base.py", line 237, in _format_and_raise
    type_override=type_override,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 873, in format_and_raise
    _raise(ex, cause)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 771, in _raise
    raise ex.with_traceback(sys.exc_info()[2])  # set env var OC_CAUSE=1 for full trace
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 488, in merge_with
    self._merge_with(*others)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 512, in _merge_with
    BaseContainer._map_merge(self, other)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 397, in _map_merge
    dest_node._merge_with(src_node)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 516, in _merge_with
    raise TypeError("Cannot merge DictConfig with ListConfig")
hydra.errors.ConfigCompositionException: In 'train_envs/endless_all': ConfigTypeError raised while composing config:
Cannot merge DictConfig with ListConfig
    full_key: 
    object_type=dict
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 12:35:16 PM: train_rl.yaml:defaults: \_self\_
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 520, in _compose_config_from_defaults_list
    cfg.merge_with(loaded.config)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 490, in merge_with
    self._format_and_raise(key=None, value=None, cause=e)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/base.py", line 237, in _format_and_raise
    type_override=type_override,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 873, in format_and_raise
    _raise(ex, cause)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 771, in _raise
    raise ex.with_traceback(sys.exc_info()[2])  # set env var OC_CAUSE=1 for full trace
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 488, in merge_with
    self._merge_with(*others)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 512, in _merge_with
    BaseContainer._map_merge(self, other)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 397, in _map_merge
    dest_node._merge_with(src_node)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 516, in _merge_with
    raise TypeError("Cannot merge DictConfig with ListConfig")
omegaconf.errors.ConfigTypeError: Cannot merge DictConfig with ListConfig
    full_key: 
    object_type=dict

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 216, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 109, in run
    run_mode=RunMode.RUN,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 599, in compose_config
    validate_sweep_overrides=validate_sweep_overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 146, in load_configuration
    validate_sweep_overrides=validate_sweep_overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 253, in _load_configuration_impl
    defaults=defaults_list.defaults, repo=caching_repo
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 524, in _compose_config_from_defaults_list
    ).with_traceback(sys.exc_info()[2])
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 520, in _compose_config_from_defaults_list
    cfg.merge_with(loaded.config)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 490, in merge_with
    self._format_and_raise(key=None, value=None, cause=e)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/base.py", line 237, in _format_and_raise
    type_override=type_override,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 873, in format_and_raise
    _raise(ex, cause)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/_utils.py", line 771, in _raise
    raise ex.with_traceback(sys.exc_info()[2])  # set env var OC_CAUSE=1 for full trace
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 488, in merge_with
    self._merge_with(*others)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 512, in _merge_with
    BaseContainer._map_merge(self, other)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 397, in _map_merge
    dest_node._merge_with(src_node)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/omegaconf/basecontainer.py", line 516, in _merge_with
    raise TypeError("Cannot merge DictConfig with ListConfig")
hydra.errors.ConfigCompositionException: In 'train_envs/endless_all': ConfigTypeError raised while composing config:
Cannot merge DictConfig with ListConfig
    full_key: 
    object_type=dict
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 12:42:27 PM: moving "self" to the top of the config file did not change the error.  
8/8/2022 12:45:31 PM: change hydra version from 1.2 to 1.1
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'train_envs/endless_all': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/training/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py:127: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/next/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  configure_logging=with_log_configuration,
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:34: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize("%s: %s" % ("WARN", msg % args), "yellow"))
wandb: Currently logged in as: neilsambhu. Use `wandb login --relogin` to force relogin
wandb: wandb version 0.13.1 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.12.21
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-08-08/12-44-21/wandb/run-20220808_124436-2ptwy5sf
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/2ptwy5sf
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
Error executing job with overrides: ['agent.ppo.wb_run_path=null', 'wb_project=train_rl_experts', 'wb_name=roach', 'agent/ppo/policy=xtma_beta', 'agent.ppo.training.kwargs.explore_coef=0.05', 'carla_sh_path=/opt/carla-simulator/CarlaUE4.sh']
Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 216, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 132, in run
    _ = ret.return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 260, in return_value
    raise self._return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
  File "train_rl_NeilBranch0.py", line 166, in main
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/rl_birdview_agent.py", line 275, in learn
    model.learn(total_timesteps, callback=callback, seed=seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/models/ppo.py", line 236, in learn
    callback.init_callback(self)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/stable_baselines3/common/callbacks.py", line 47, in init_callback
    self.logger = model.logger
AttributeError: 'PPO' object has no attribute 'logger'
wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb:                                                                                
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/2ptwy5sf
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: Find logs at: ./outputs/2022-08-08/12-44-21/wandb/run-20220808_124436-2ptwy5sf/logs
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 12:50:12 PM: hydra 1.1 to 1.0
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 22, in <module>
    @hydra.main(config_path='config', config_name='train_rl', version_base='1.0')
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 56, in main
    version.setbase(version_base)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/version.py", line 79, in setbase
    raise HydraException(f'version_base must be >= "{__compat_version__}"')
hydra.errors.HydraException: version_base must be >= "1.1"
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 1:01:53 PM: hydra 1.0 to 0.11
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 22, in <module>
    @hydra.main(config_path='config', config_name='train_rl', version_base='1.0')
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 56, in main
    version.setbase(version_base)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/version.py", line 79, in setbase
    raise HydraException(f'version_base must be >= "{__compat_version__}"')
hydra.errors.HydraException: version_base must be >= "1.1"
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 1:10:19 PM: assumption: hydra 1.1 is valid. TODO: locate package header https://hydra.cc/docs/upgrades/1.0_to_1.1/changes_to_package_header/  
8/8/2022 1:19:02 PM: ppo.yaml:remove header  
8/8/2022 1:20:01 PM: hydra 0.11 to 1.1  
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'train_envs/endless_all': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py:127: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/next/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  configure_logging=with_log_configuration,
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:34: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize("%s: %s" % ("WARN", msg % args), "yellow"))
wandb: Currently logged in as: neilsambhu. Use `wandb login --relogin` to force relogin
wandb: wandb version 0.13.1 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.12.21
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-08-08/13-22-23/wandb/run-20220808_132237-myagi2db
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/myagi2db
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
Error executing job with overrides: ['agent.ppo.wb_run_path=null', 'wb_project=train_rl_experts', 'wb_name=roach', 'agent/ppo/policy=xtma_beta', 'agent.ppo.training.kwargs.explore_coef=0.05', 'carla_sh_path=/opt/carla-simulator/CarlaUE4.sh']
Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 216, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 132, in run
    _ = ret.return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 260, in return_value
    raise self._return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
  File "train_rl_NeilBranch0.py", line 166, in main
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/rl_birdview_agent.py", line 275, in learn
    model.learn(total_timesteps, callback=callback, seed=seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/models/ppo.py", line 236, in learn
    callback.init_callback(self)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/stable_baselines3/common/callbacks.py", line 47, in init_callback
    self.logger = model.logger
AttributeError: 'PPO' object has no attribute 'logger'
wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb:                                                                                
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/myagi2db
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: Find logs at: ./outputs/2022-08-08/13-22-23/wandb/run-20220808_132237-myagi2db/logs
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 1:38:24 PM: find "# @package \_group\_"
```
grep -r  --exclude timeline/README1.md --exclude timeline/README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "# @package _group_">outgrep.txt
```
8/8/2022 1:52:27 PM: train_rl_parent_NeilBranch0.py > remove "# @package \_group\_"
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/default_element.py:128: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py:127: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/next/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  configure_logging=with_log_configuration,
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:34: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize("%s: %s" % ("WARN", msg % args), "yellow"))
wandb: Currently logged in as: neilsambhu. Use `wandb login --relogin` to force relogin
wandb: wandb version 0.13.1 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.12.21
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-08-08/14-03-18/wandb/run-20220808_140333-3dz9ykhd
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/3dz9ykhd
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
Error executing job with overrides: ['agent.ppo.wb_run_path=null', 'wb_project=train_rl_experts', 'wb_name=roach', 'agent/ppo/policy=xtma_beta', 'agent.ppo.training.kwargs.explore_coef=0.05', 'carla_sh_path=/opt/carla-simulator/CarlaUE4.sh']
Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 95, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 396, in _run_hydra
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 453, in _run_app
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 216, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 213, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 456, in <lambda>
    overrides=overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 132, in run
    _ = ret.return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 260, in return_value
    raise self._return_value
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
  File "train_rl_NeilBranch0.py", line 166, in main
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/rl_birdview_agent.py", line 275, in learn
    model.learn(total_timesteps, callback=callback, seed=seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/models/ppo.py", line 236, in learn
    callback.init_callback(self)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/stable_baselines3/common/callbacks.py", line 47, in init_callback
    self.logger = model.logger
AttributeError: 'PPO' object has no attribute 'logger'
wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb:                                                                                
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/3dz9ykhd
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: Find logs at: ./outputs/2022-08-08/14-03-18/wandb/run-20220808_140333-3dz9ykhd/logs
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 2:06:58 PM: pause upgrading code to hydra 1.1. TODO: (1) ppo.yaml header; (2) train_rl_parent_NeilBranch0.py  
8/8/2022 2:15:08 PM: conda environment carla -> carla1
```
conda create --name carla1 --clone carla
```
```
(carla1) nsambhu@SAMBHU19:~/github/carla-roach$ conda list hydra
# packages in environment at /home/nsambhu/anaconda3/envs/carla1:
#
# Name                    Version                   Build  Channel
hydra                     2.5              py37h5e8e339_0    conda-forge
hydra-core                1.2.0                    pypi_0    pypi
```
8/8/2022 2:22:12 PM: install hydra v1.0
```
conda install -c conda-forge hydra=1.0
```
failed.  
try again: 
```
pip install hydra-core==1.0
```
```
(carla1) nsambhu@SAMBHU19:~/github/carla-roach$ conda list hydra
# packages in environment at /home/nsambhu/anaconda3/envs/carla1:
#
# Name                    Version                   Build  Channel
hydra                     2.5              py37h5e8e339_0    conda-forge
hydra-core                1.0.0                    pypi_0    pypi
```
8/8/2022 2:38:04 PM: run
```
(carla1) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/utils.py:143: UserWarning: register_resolver() is deprecated.
See https://github.com/omry/omegaconf/issues/426 for migration instructions.

  OmegaConf.register_resolver(name, f)
CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/gym/logger.py:34: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize("%s: %s" % ("WARN", msg % args), "yellow"))
wandb: Currently logged in as: neilsambhu. Use `wandb login --relogin` to force relogin
wandb: wandb version 0.13.1 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.12.21
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-08-08/14-36-42/wandb/run-20220808_143656-3r5miqri
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/3r5miqri
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 356, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 210, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 207, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 359, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "train_rl_NeilBranch0.py", line 166, in main
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/rl_birdview_agent.py", line 275, in learn
    model.learn(total_timesteps, callback=callback, seed=seed)
  File "/home/nsambhu/github/carla-roach/agents/rl_birdview/models/ppo.py", line 236, in learn
    callback.init_callback(self)
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/stable_baselines3/common/callbacks.py", line 47, in init_callback
    self.logger = model.logger
AttributeError: 'PPO' object has no attribute 'logger'
wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb:                                                                                
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/3r5miqri
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: Find logs at: ./outputs/2022-08-08/14-36-42/wandb/run-20220808_143656-3r5miqri/logs
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 2:41:37 PM: try to install hydra v1.1
```
(carla1) nsambhu@SAMBHU19:~/github/carla-roach$ conda list hydra
# packages in environment at /home/nsambhu/anaconda3/envs/carla1:
#
# Name                    Version                   Build  Channel
hydra                     2.5              py37h5e8e339_0    conda-forge
hydra-core                1.1.0                    pypi_0    pypi
```
8/8/2022 2:46:35 PM: run
```
(carla1) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/default_element.py:127: UserWarning: In 'train_envs/endless_all': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/default_element.py:127: UserWarning: In 'agent/ppo/obs_configs/birdview': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/default_element.py:127: UserWarning: In 'agent/ppo/training/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/default_element.py:127: UserWarning: In 'agent/ppo/policy/xtma_beta': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/core/default_element.py:127: UserWarning: In 'agent/ppo': Usage of deprecated keyword in package header '# @package _group_'.
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_package_header for more information
  See {url} for more information"""
Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 175, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/main.py", line 53, in decorated_main
    config_name=config_name,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 368, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 214, in run_and_report
    raise ex
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 211, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/utils.py", line 371, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 91, in run
    run_mode=RunMode.RUN,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 568, in compose_config
    from_shell=from_shell,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 150, in load_configuration
    from_shell=from_shell,
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 250, in _load_configuration_impl
    defaults=defaults_list.defaults, repo=caching_repo
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 515, in _compose_config_from_defaults_list
    loaded = self._load_single_config(default=default, repo=repo)
  File "/home/nsambhu/anaconda3/envs/carla1/lib/python3.7/site-packages/hydra/_internal/config_loader_impl.py", line 400, in _load_single_config
    f"Config {config_path} must be a Dictionary, got {type(ret).__name__}"
ValueError: Config train_envs/endless_all must be a Dictionary, got ConfigResult
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 3:00:38 PM: create conda environment carla2 from environment.yml  
```
conda env create -f environment.yml
```
8/8/2022 3:15:01 PM: run
```
(carla2) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


Traceback (most recent call last):
  File "train_rl_NeilBranch0.py", line 14, in <module>
    from carla_gym.utils import config_utils
  File "/home/nsambhu/github/carla-roach/carla_gym/utils/config_utils.py", line 7, in <module>
    import carla
ModuleNotFoundError: No module named 'carla'
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 81, in <module>
    completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/8/2022 3:21:33 PM: upgrade pip
```
pip3 install --upgrade pip
```
8/8/2022 3:23:02 PM: install carla
```
pip install carla
```
8/8/2022 3:28:30 PM: run
```
(carla2) nsambhu@SAMBHU19:~/github/carla-roach$ HYDRA_FULL_ERROR=1 python -u run/train_rl_parent_NeilBranch0.py>out.txt
run/train_rl_NeilBranch0.sh: line 21: /home/nsambhu/miniconda3/etc/profile.d/conda.sh: No such file or directory

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


CarlaUE4-Linux: no process found
CarlaUE4-Linux: no process found
/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.13.1 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run roach
wandb: ⭐ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/1vmonw63
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-08-08/15-36-44/wandb/run-20220808_153717-1vmonw63
wandb: Run `wandb offline` to turn off syncing.
wandb: WARNING Symlinked 3 files into the W&B run directory, call wandb.save again to sync new files.
/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
/opt/carla-simulator/CarlaUE4.sh: line 2: 46769 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
/opt/carla-simulator/CarlaUE4.sh: line 2: 46778 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
/opt/carla-simulator/CarlaUE4.sh: line 2: 46766 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
/opt/carla-simulator/CarlaUE4.sh: line 2: 46775 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
/opt/carla-simulator/CarlaUE4.sh: line 2: 46772 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
wandb: Waiting for W&B process to finish, PID 48271
wandb: Program ended successfully.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-08-08/15-36-44/wandb/run-20220808_153717-1vmonw63/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-08-08/15-36-44/wandb/run-20220808_153717-1vmonw63/logs/debug-internal.log
wandb: Run summary:
wandb:                         time/rollout 318.84855
wandb:                  rollout/score_route 0.01581
wandb:                rollout/score_penalty 0.85564
wandb:               rollout/score_composed 0.01369
wandb:                       rollout/length 2819.71429
wandb:                       rollout/reward -2271.84745
wandb:                      rollout/timeout 0.0
wandb:           rollout/is_route_completed 0.0
wandb:   rollout/is_route_completed_nocrash 0.0
wandb:        rollout/route_completed_in_km 0.01581
wandb:           rollout/route_length_in_km 1.64707
wandb:      rollout/percentage_outside_lane 0.0
wandb:        rollout/percentage_wrong_lane 0.03008
wandb:            rollout/collisions_layout 0.0
wandb:           rollout/collisions_vehicle 22.68909
wandb:        rollout/collisions_pedestrian 0.0
wandb:            rollout/collisions_others 0.0
wandb:                    rollout/red_light 0.0
wandb:                 rollout/light_passed 0.0
wandb:              rollout/encounter_light 0.0
wandb:              rollout/stop_infraction 0.0
wandb:                  rollout/stop_passed 0.0
wandb:               rollout/encounter_stop 0.0
wandb:                    rollout/route_dev 0.0
wandb:              rollout/vehicle_blocked 0.0
wandb:                   rollout/n_episodes 7.0
wandb:                         time/n_epoch 1
wandb:                   time/sec_per_epoch 347.43335
wandb:                             time/fps 35.3593
wandb:                           time/train 52.40159
wandb:                    time/train_values 0.0
wandb:                   train/entropy_loss 0.08331
wandb:               train/exploration_loss 0.01847
wandb:           train/policy_gradient_loss 0.3679
wandb:                     train/value_loss 4.48912
wandb:                  train/last_epoch_kl 0.00142
wandb:                  train/clip_fraction 0.03141
wandb:                           train/loss 2.61421
wandb:             train/explained_variance -0.78875
wandb:                     train/clip_range 0.2
wandb:                    train/train_epoch 19
wandb:                  train/learning_rate 1e-05
wandb:                                _step 24570
wandb:                             _runtime 704
wandb:                           _timestamp 1659988141
wandb: Run history:
wandb:                         time/rollout ▁█
wandb:                  rollout/score_route ▁█
wandb:                rollout/score_penalty ▁█
wandb:               rollout/score_composed ▁█
wandb:                       rollout/length ▁█
wandb:                       rollout/reward █▁
wandb:                      rollout/timeout ▁▁
wandb:           rollout/is_route_completed ▁▁
wandb:   rollout/is_route_completed_nocrash ▁▁
wandb:        rollout/route_completed_in_km ▁█
wandb:           rollout/route_length_in_km ▁█
wandb:      rollout/percentage_outside_lane ▁▁
wandb:        rollout/percentage_wrong_lane ▁█
wandb:            rollout/collisions_layout ▁▁
wandb:           rollout/collisions_vehicle █▁
wandb:        rollout/collisions_pedestrian ▁▁
wandb:            rollout/collisions_others ▁▁
wandb:                    rollout/red_light ▁▁
wandb:                 rollout/light_passed ▁▁
wandb:              rollout/encounter_light ▁▁
wandb:              rollout/stop_infraction ▁▁
wandb:                  rollout/stop_passed ▁▁
wandb:               rollout/encounter_stop ▁▁
wandb:                    rollout/route_dev ▁▁
wandb:              rollout/vehicle_blocked ▁▁
wandb:                   rollout/n_episodes ▁█
wandb:                         time/n_epoch ▁█
wandb:                   time/sec_per_epoch ▁█
wandb:                             time/fps █▁
wandb:                           time/train ▁█
wandb:                    time/train_values ▁▁
wandb:                   train/entropy_loss ▁█
wandb:               train/exploration_loss ▁█
wandb:           train/policy_gradient_loss ▁█
wandb:                     train/value_loss █▁
wandb:                  train/last_epoch_kl █▁
wandb:                  train/clip_fraction █▁
wandb:                           train/loss █▁
wandb:             train/explained_variance ▁█
wandb:                     train/clip_range ▁▁
wandb:                    train/train_epoch ▁▁
wandb:                  train/learning_rate ▁▁
wandb:                                _step ▁█
wandb:                             _runtime ▁█
wandb:                           _timestamp ▁█
wandb: 
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 4 other file(s)
wandb: 
wandb: Synced roach: https://wandb.ai/neilsambhu/train_rl_experts/runs/1vmonw63
PYTHON_RETURN=0
CarlaUE4-Linux: no process found
```
8/8/2022 3:59:47 PM: train_rl_parent_NeilBranch0.py > removed hardcoded lEpochs=1
```
wandb: ⭐️ View project at https://wandb.ai/neilsambhu/train_rl_experts
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/1n3jvkk0
```
8/8/2022 4:03:05 PM:  
TODO:  
(1) CARLA non-gui (i.e. -RenderOffScreen flag) https://carla.readthedocs.io/en/latest/adv_rendering_options/ and  
(2) CARLA on multiple GPUs:  
(a) train_rl_parent_NeilBranch0.py > endless_all gpu 0 to 1  
(b) nvidia-smi > check gpu 1  

8/8/2022 4:43:20 PM: carla won't run on GPU 1. TODO: try to run carla on gpu 1.  
unrealengine: Unable to select GPU when using RenderOffscreen.  
TODO: (maybe) select GPU using docker.  
8/8/2022 9:11:35 PM: train non-GUI on GPU 0 for 10M steps
```
grep -r  --exclude timeline/README1.md --exclude timeline/README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "bVerbose = True">outgrep.txt
```
Note: cancelled execution  
```
nvidia-smi | grep 'CarlaUE4' | awk '{ print $5 }' | xargs -n1 kill -9
```
8/8/2022 9:26:12 PM: TODO: find max town count on 1 GPU. Current: 5.  
5 towns: 11843MiB / 24576MiB  
6 towns: memory allocation error  
8/8/2022 9:36:39 PM: train non-GUI on GPU 0 for 10M steps on 5 towns on GPU 0.  
wandb: ⭐️ View project at https://wandb.ai/neilsambhu/train_rl_experts  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/v5k7i84s  
Note: error during execution. Wandb did not sync a checkpoint for the second epoch. 73368 steps should be sufficient for a sync.  
8/8/2022 10:24:28 PM: train_rl_parent_NeilBranch0.py: add code to modify ppo.yaml:n_steps_total  
8/8/2022 10:26:03 PM: train non-GUI on GPU 0 for 10M steps on 5 towns on GPU 0. Try 100k steps.  
wandb: ⭐️ View project at https://wandb.ai/neilsambhu/train_rl_experts  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/3rwvg1ye  
```
Process ForkServerProcess-4:
Process ForkServerProcess-5:
Process ForkServerProcess-1:
Process ForkServerProcess-3:
Process ForkServerProcess-2:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/stable_baselines3/common/vec_env/subproc_vec_env.py", line 23, in _worker
    remote.send((observation, reward, done, info))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 206, in send
    self._send_bytes(_ForkingPickler.dumps(obj))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/stable_baselines3/common/vec_env/subproc_vec_env.py", line 23, in _worker
    remote.send((observation, reward, done, info))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 398, in _send_bytes
    self._send(buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/stable_baselines3/common/vec_env/subproc_vec_env.py", line 23, in _worker
    remote.send((observation, reward, done, info))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 206, in send
    self._send_bytes(_ForkingPickler.dumps(obj))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 206, in send
    self._send_bytes(_ForkingPickler.dumps(obj))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 398, in _send_bytes
    self._send(buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/stable_baselines3/common/vec_env/subproc_vec_env.py", line 23, in _worker
    remote.send((observation, reward, done, info))
BrokenPipeError: [Errno 32] Broken pipe
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 398, in _send_bytes
    self._send(buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/site-packages/stable_baselines3/common/vec_env/subproc_vec_env.py", line 23, in _worker
    remote.send((observation, reward, done, info))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 206, in send
    self._send_bytes(_ForkingPickler.dumps(obj))
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 206, in send
    self._send_bytes(_ForkingPickler.dumps(obj))
BrokenPipeError: [Errno 32] Broken pipe
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 398, in _send_bytes
    self._send(buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 398, in _send_bytes
    self._send(buf)
BrokenPipeError: [Errno 32] Broken pipe
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
  File "/home/nsambhu/anaconda3/envs/carla2/lib/python3.7/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
BrokenPipeError: [Errno 32] Broken pipe
BrokenPipeError: [Errno 32] Broken pipe
run/train_rl_NeilBranch0.sh: line 3:  6965 Killed                  python -u train_rl_NeilBranch0.py agent.ppo.wb_run_path=null wb_project=train_rl_experts wb_name=roach agent/ppo/policy=xtma_beta agent.ppo.training.kwargs.explore_coef=0.05 carla_sh_path=${CARLA_ROOT}/CarlaUE4.sh
PYTHON_RETURN=0
Traceback (most recent call last):
  File "run/train_rl_parent_NeilBranch0.py", line 91, in <module>
    print(f"completed_timesteps: {completed_timesteps}")
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/num_timesteps.txt'
```
8/9/2022 10:36:08 AM: train again  
wandb: ⭐️ View project at https://wandb.ai/neilsambhu/train_rl_experts  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/2e007w4u  
Error: EOF  
8/9/2022 11:43:12 AM: train_rl_parent_NeilBranch0.py > n_steps_total > 1e5 -> 1e4  
wandb: ⭐️ View project at https://wandb.ai/neilsambhu/train_rl_experts  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/train_rl_experts/runs/32r0l3yx  
cancelled execution  
8/9/2022 2:59:33 PM: change program output  
```
python -u run/train_rl_parent_NeilBranch0.py |& tee out.txt
```
train_rl_parent_NeilBranch0.py > GPU 1  
execution EOF error  
8/9/2022 3:20:55 PM: train_rl_parent_NeilBranch0.py > GPU 0  
stop execution to work on docker  
8/9/2022 4:09:22 PM: carla docker
```
sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
```
server_utils.py > new carla docker:
```
cmd = f'sudo docker run --privileged --gpus "device={cfg["gpu"]}" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port={cfg["port"]} -RenderOffScreen'
```
8/9/2022 4:43:47 PM: new command for calling carla-roach  
sudo /home/nsambhu/anaconda3/envs/carla2/bin/python -u run/train_rl_parent_NeilBranch0.py |& tee out.txt  
new 2 command for calling carla-roach  
python -u run/train_rl_parent_NeilBranch0.py |& tee out.txt  
8/11/2022 11:07:47 AM: cancelled execution  
8/12/2022 11:32:54 AM: server_utils.py: can't properly call Apptainer carla.  
```
chmod: cannot access '/home/nsambhu/github/carla-roach/outputs/2022-08-12/11-30-21/carla-0.9.13/home/carla/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping': No such file or directory
carla-0.9.13/home/carla/CarlaUE4.sh: line 5: /home/nsambhu/github/carla-roach/outputs/2022-08-12/11-30-21/carla-0.9.13/home/carla/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping: No such file or directory
INFO:    Build complete: carla-0.9.13/
```
# SAMBHU19 Red Hat Enterprise Linux
8/18/2022 4:13:04 PM: install docker: https://docs.docker.com/engine/install/rhel/  
8/19/2022 4:56:35 PM: run_custom_setup/install_docker_rhel3.sh > docker installed  
8/21/2022 2:58:00 PM: run_custom_setup/install_nvidia-docker2_rhel.sh (i.e. copy line by line) > Error: 
```
(base) [nsambhu@localhost carla-roach]$ sudo docker run --rm -e NVIDIA_VISIBLE_DEVICES=all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
Failed to initialize NVML: Insufficient Permissions
```
## 2022 08 21 2022: to Daniel: 
8/21/2022 3:11:39 PM:  
1. Google search "docker failed to initialize nvml: insufficient permissions" (i.e. https://www.google.com/search?q=docker+failed+to+initialize+nvml%3A+insufficient+permissions&rlz=1C1CHBF_enUS856US856&sxsrf=ALiCzsaVGolpp73zYZzFoppJJMkEpN73nQ%3A1661026549331&ei=9UABY_rwE_qykvQPvo2r4As&ved=0ahUKEwi6v72Lntb5AhV6mYQIHb7GCrwQ4dUDCA4&uact=5&oq=docker+failed+to+initialize+nvml%3A+insufficient+permissions&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCCMQsAIQJzoECAAQDToGCAAQHhAHOgYIABAeEA06BQgAEIYDSgQIQRgASgQIRhgAUIUJWIUOYJ4PaAFwAXgAgAGMAYgBhQWSAQM2LjGYAQCgAQHIAQbAAQE&sclient=gws-wiz-serp )  
2. https://bbs.archlinux.org/viewtopic.php?id=266915 > changes bootloader parameter (i.e. Even sudo isn't sufficient)  
## Debug: Failed to initialize NVML: Insufficient Permissions
1. https://github.com/NVIDIA/nvidia-docker/issues/1523 > https://github.com/NVIDIA/nvidia-docker/issues/1547 (failed)  
2. https://stackoverflow.com/questions/52507744/enable-nvidia-smi-permissions-to-be-run-by-all-users > https://stackoverflow.com/a/70391740 (works)  
## 2022 08 21 2022: to Daniel: 
```
(base) [nsambhu@localhost ~]$ sudo docker run --rm -e NVIDIA_VISIBLE_DEVICES=all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
Mon Aug 22 00:30:49 2022
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 515.65.01    Driver Version: 515.65.01    CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA TITAN RTX    Off  | 00000000:01:00.0 Off |                  N/A |
| 41%   36C    P8    11W / 280W |    114MiB / 24576MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA TITAN RTX    Off  | 00000000:21:00.0 Off |                  N/A |
| 40%   33C    P8    12W / 280W |      1MiB / 24576MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
(base) [nsambhu@localhost ~]$ sudo -S docker run --privileged --gpus "device=0" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port=2000 -RenderOffScreen
unknown flag: --gpus
See 'docker run --help'.
```
## CARLA GUI
8/23/2022 2:13 PM: carla-roach/server_utils.py:  
```
# working docker
cmd = f'echo q | sudo -S docker run --privileged --gpus "device={cfg["gpu"]}" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port={cfg["port"]} -RenderOffScreen'
```  
modified for simplicity:  
```
sudo -S docker run --privileged --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
```
```
(base) [nsambhu@localhost ~]$ sudo -S docker run --privileged --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
[sudo] password for nsambhu: 
sh: 1: xdg-user-dir: not found
error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
```
## GAIVI
8/23/2022 3:39:18 PM: GAIVI container builder client  
```
[nsambhu@forest.usf.edu@gaivi2 ~]$ container-builder-client -u Dockerfile
Uploading Dockerfile to http://eregion.cse.usf.edu
Got back build id "a2f33a20-5094-4019-9811-caaaa8589a7b"
{:host "http://eregion.cse.usf.edu", :poll-time 2, :upload true, :input-file "Dockerfile", :build-id #uuid "a2f33a20-5094-4019-9811-caaaa8589a7b"}
```
8/23/2022 3:44:51 PM: GAIVI check for carla singularity to run on a GPU:
```
[nsambhu@forest.usf.edu@gaivi2 ~]$ srun --pty --gpus 1 /bin/bash
srun: job 63122 queued and waiting for resources
srun: job 63122 has been allocated resources
[nsambhu@forest.usf.edu@gpu20 ~]$ hostname
gpu20.cse.usf.edu
[nsambhu@forest.usf.edu@gpu20 ~]$ nvidia-smi
Tue Aug 23 15:43:17 2022
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.42.01    Driver Version: 470.42.01    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:84:00.0 Off |                  N/A |
| 23%   24C    P8     8W / 250W |      0MiB / 11178MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
8/23/2022 3:52:05 PM: GAIVI notes
```
[nsambhu@forest.usf.edu@gaivi2 ~]$ srun -p Contributors -w GPU20 --pty --gpus 1 /bin/bash
srun: job 63123 queued and waiting for resources
srun: job 63123 has been allocated resources
[nsambhu@forest.usf.edu@gpu20 ~]$ exit
exit
[nsambhu@forest.usf.edu@gaivi2 ~]$ sinfo -N --format="%10N | %10t | %7X | %7Y | %7Z | %9m | %19G"
NODELIST   | STATE      | SOCKETS | CORES   | THREADS | MEMORY    | GRES
GPU2       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU2       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU3       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU3       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU4       | mix        | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU4       | mix        | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU4       | mix        | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU5       | idle       | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU5       | idle       | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU6       | mix        | 2       | 8       | 2       | 128664    | gpu:1080Ti:4
GPU6       | mix        | 2       | 8       | 2       | 128664    | gpu:1080Ti:4
GPU7       | alloc      | 2       | 8       | 2       | 128664    | gpu:1080Ti:4
GPU7       | alloc      | 2       | 8       | 2       | 128664    | gpu:1080Ti:4
GPU8       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU8       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU8       | alloc      | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU9       | idle       | 2       | 8       | 2       | 128667    | gpu:1080Ti:4
GPU9       | idle       | 2       | 8       | 2       | 128667    | gpu:1080Ti:4
GPU10      | idle       | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU10      | idle       | 2       | 8       | 2       | 128670    | gpu:1080Ti:4
GPU11      | drain      | 2       | 8       | 2       | 128664    | gpu:TitanX:8
GPU11      | drain      | 2       | 8       | 2       | 128664    | gpu:TitanX:8
GPU12      | alloc      | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU12      | alloc      | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU13      | alloc      | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU13      | alloc      | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU14      | idle       | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU14      | idle       | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU15      | alloc      | 2       | 8       | 1       | 386699    | gpu:TitanX:8
GPU15      | alloc      | 2       | 8       | 1       | 386699    | gpu:TitanX:8
GPU16      | mix        | 2       | 8       | 1       | 386699    | gpu:TitanX:4(S:0)
GPU16      | mix        | 2       | 8       | 1       | 386699    | gpu:TitanX:4(S:0)
GPU17      | mix        | 2       | 8       | 1       | 128667    | gpu:TitanX:4,gpu:Ti
GPU17      | mix        | 2       | 8       | 1       | 128667    | gpu:TitanX:4,gpu:Ti
GPU18      | alloc      | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU18      | alloc      | 2       | 8       | 1       | 128667    | gpu:TitanX:8
GPU19      | alloc      | 2       | 8       | 1       | 386698    | gpu:TitanX:8
GPU19      | alloc      | 2       | 8       | 1       | 386698    | gpu:TitanX:8
GPU20      | mix        | 2       | 8       | 1       | 386699    | gpu:1080Ti:8
GPU20      | mix        | 2       | 8       | 1       | 386699    | gpu:1080Ti:8
GPU21      | drain      | 2       | 8       | 1       | 128667    | gpu:1080Ti:8(S:0)
GPU21      | drain      | 2       | 8       | 1       | 128667    | gpu:1080Ti:8(S:0)
GPU22      | idle       | 2       | 10      | 2       | 1031770   | gpu:1080Ti:8
GPU41      | mix        | 2       | 8       | 2       | 128659    | gpu:TitanX:4
GPU41      | mix        | 2       | 8       | 2       | 128659    | gpu:TitanX:4
GPU42      | alloc      | 2       | 16      | 2       | 191850    | gpu:TitanRTX:4
GPU42      | alloc      | 2       | 16      | 2       | 191850    | gpu:TitanRTX:4
GPU43      | alloc      | 1       | 64      | 2       | 515730    | gpu:A40:4
GPU43      | alloc      | 1       | 64      | 2       | 515730    | gpu:A40:4
GPU44      | alloc      | 1       | 32      | 2       | 515739    | gpu:A40:4
GPU44      | alloc      | 1       | 32      | 2       | 515739    | gpu:A40:4
GPU45      | idle       | 2       | 24      | 1       | 257647    | gpu:A40:1
GPU45      | idle       | 2       | 24      | 1       | 257647    | gpu:A40:1
PHI1       | idle       | 2       | 8       | 2       | 128673    | (null)
[nsambhu@forest.usf.edu@gaivi2 ~]$ squeue -w GPU43
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             62803 Contribut   dispMT gdayhoff  R 4-06:28:46      1 GPU43
[nsambhu@forest.usf.edu@gaivi2 ~]$ squeue -p Contributors
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             62265 Contribut  chex.sh kbenahme  R 13-21:51:32      1 GPU16
             62422 Contribut   nmr2WT gdayhoff  R 12-13:55:33      1 GPU3
             62429 Contribut   rsffMT gdayhoff  R 12-13:41:27      1 GPU19
             62511 Contribut   rsffWT gdayhoff  R 11-05:57:55      1 GPU7
             62513 Contribut   nmr2MT gdayhoff  R 11-05:53:54      1 GPU8
             62801 Contribut   dispWT gdayhoff  R 4-06:29:10      1 GPU44
             62803 Contribut   dispMT gdayhoff  R 4-06:29:16      1 GPU43
             63029 Contribut  DPPC_NA mwsaunde  R 1-01:41:49      1 GPU42
             63063 Contribut run_trai saeed3@f  R    9:24:44      1 GPU41
             63076 Contribut     DPPC mwsaunde  R    3:35:01      1 GPU2
[nsambhu@forest.usf.edu@gaivi2 ~]$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             62265 Contribut  chex.sh kbenahme  R 13-21:51:37      1 GPU16
             62422 Contribut   nmr2WT gdayhoff  R 12-13:55:38      1 GPU3
             62429 Contribut   rsffMT gdayhoff  R 12-13:41:32      1 GPU19
             62511 Contribut   rsffWT gdayhoff  R 11-05:58:00      1 GPU7
             62513 Contribut   nmr2MT gdayhoff  R 11-05:53:59      1 GPU8
             62801 Contribut   dispWT gdayhoff  R 4-06:29:15      1 GPU44
             62803 Contribut   dispMT gdayhoff  R 4-06:29:21      1 GPU43
             63029 Contribut  DPPC_NA mwsaunde  R 1-01:41:54      1 GPU42
             63063 Contribut run_trai saeed3@f  R    9:24:49      1 GPU41
             63076 Contribut     DPPC mwsaunde  R    3:35:06      1 GPU2
             62221  Extended     p045 hamzakar PD       0:00      1 (ReqNodeNotAvail, UnavailableNodes:GPU21)
             63014  Extended train.sh grotich@  R 1-04:01:36      1 GPU13
             63069  Extended train.sh grotich@  R    5:19:32      1 GPU12
             62938     Quick tcctrain sainathr PD       0:00      1 (Resources)
             63110   general run_trai saeed3@f PD       0:00      1 (Resources)
             62794   general generate snehaola  R 4-14:44:35      1 GPU17
             62860   general   run.sh coleh@fo  R 4-00:46:03      1 GPU4
             62932   general generate snehaola  R 2-02:27:36      1 GPU6
             62933   general generate snehaola  R 2-02:22:49      1 GPU20
             63104   general     bash abibat@f  R      58:43      1 GPU20
             63107   general train.sh mdimranh  R      54:43      1 GPU18
             63108   general run_base caiodasi  R      52:55      1 GPU15
             63120   general  jupyter sainathr  R       9:39      1 GPU20
             63121   general generate snehaola  R       8:19      1 GPU4
```
wiki: https://docs.gaivi.cse.usf.edu/doku.php?id=main:gaivi:1.manual:1.quickstart > Checking compute nodes for all resources (i.e. what nodes have what cards)  
8/23/2022 3:52:59 PM: download singularity image from container-builder-client:  
check status:  
```
container-builder-client -s <build_id>
```
download container:  
```
containe-builder-client -d <build_id> filename.sif
```
## CARLA GUI
8/23/2022 4:13:38 PM: SAMBHU19: RHEL: CARLA GUI: https://carla.readthedocs.io/en/latest/build_docker/  
8/23/2022 5:16 PM: 
```
(base) [nsambhu@localhost 7RHEL]$ sudo docker pull carlasim/carla:0.9.13
Trying to pull repository registry.access.redhat.com/carlasim/carla ... 
Pulling repository registry.access.redhat.com/carlasim/carla
Trying to pull repository registry.redhat.io/carlasim/carla ... 
Trying to pull repository docker.io/carlasim/carla ... 
0.9.13: Pulling from docker.io/carlasim/carla
Digest: sha256:2c1a59808792b99233c92dcdab6afb575357b863a00f7ff44b3ae096f648af12
Status: Image is up to date for docker.io/carlasim/carla:0.9.13
(base) [nsambhu@localhost 7RHEL]$ sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
unknown flag: --gpus
See 'docker run --help'.
````
## GAIVI
8/24/2022 1:27:07 PM: build-id: 7433a09a-65bf-4a8d-8eed-04db60ca38bc
```
[nsambhu@forest.usf.edu@gaivi2 ~]$ container-builder-client -uwd Dockerfile carla-0.9.13.sif
Uploading Dockerfile to http://eregion.cse.usf.edu
Got back build id "7433a09a-65bf-4a8d-8eed-04db60ca38bc"
Checking the status of build 7433a09a-65bf-4a8d-8eed-04db60ca38bc every 2 seconds
Build status: running
Build status: running
...
2022/08/24 17:10:17  info unpack layer: sha256:e85fa0a163b13ab5b742dfa4dad887413e9089a258d192f3df104a42ea296510
INFO:    Creating SIF file...
INFO:    Build complete: /apps/container_builder/images/7433a09a-65bf-4a8d-8eed-04db60ca38bc.img

Downloading the result of build 7433a09a-65bf-4a8d-8eed-04db60ca38bc to carla-0.9.13.sif
{:host "http://eregion.cse.usf.edu", :poll-time 2, :upload true, :watch true, :download true, :input-file "Dockerfile", :output-file "carla-0.9.13.sif", :build-id #uuid "7433a09a-65bf-4a8d-8eed-04db60ca38bc"}
```
8/24/2022 4:28:55 PM: (re: https://carla.readthedocs.io/en/latest/build_docker/) CARLA docker GUI and non-GUI:  
```
1. Pull the CARLA image.

You can pull either the latest CARLA image or a specific release version. The latest image refers to the most recent packaged release. To pull the image, run one of the following commands:

# Pull the latest image
docker pull carlasim/carla:latest

# Pull a specific version
docker pull carlasim/carla:0.9.12
2. Run the CARLA container.

Different versions of CARLA support different graphics APIs which can affect the conditions in which the Docker image can run:

0.9.12 supports only Vulkan
0.9.7+ supports both Vulkan and OpenGL.
CARLA 0.9.12

To run CARLA with a display:

sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.12 /bin/bash ./CarlaUE4.sh
To run CARLA in off-screen mode:
sudo docker run --privileged --gpus all --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.12 /bin/bash ./CarlaUE4.sh -RenderOffScreen
```
8/24/2022 4:45:39 PM: CARLA in GAIVI  
```
[nsambhu@forest.usf.edu@gaivi2 ~]$ srun --gpus 1 singularity exec --nv carla-real.sif /home/carla/CarlaUE4.sh -RenderOffScreen
srun: job 63230 queued and waiting for resources
srun: job 63230 has been allocated resources
chmod: changing permissions of '/home/carla/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping': Read-only file system
sh: 1: xdg-user-dir: not found
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
```
new shell for job submission
```
[nsambhu@forest.usf.edu@gaivi2 ~]$ squeue -u `whoami`
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             63227   general     bash nsambhu@  R      10:05      1 GPU20
[nsambhu@forest.usf.edu@gaivi2 ~]$ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             63227   general     bash nsambhu@  R      10:17      1 GPU20
[nsambhu@forest.usf.edu@gaivi2 ~]$ srun --interactive --jobid 63227 --pty /bin/bash
[nsambhu@forest.usf.edu@gpu20 ~]$ nvidia-smi
```
8/24/2022 4:47:35 PM: (re: https://apptainer.org/docs/user/main/gpu.html#multiple-gpus) Apptainer select GPU: 
```
$ APPTAINERENV_CUDA_VISIBLE_DEVICES=0 apptainer run --nv tensorflow_latest-gpu.sif

# or

$ export APPTAINERENV_CUDA_VISIBLE_DEVICES=0
$ apptainer run tensorflow_latest-gpu.sif
```
8/24/2022 4:55:56 PM: (re: https://docs.sylabs.io/guides/3.5/user-guide/gpu.html#multiple-gpus) Singularity select GPU:
```
$ SINGULARITYENV_CUDA_VISIBLE_DEVICES=0 singularity run --nv tensorflow_latest-gpu.sif

# or

$ export SINGULARITYENV_CUDA_VISIBLE_DEVICES=0
$ singularity run tensorflow_latest-gpu.sif
```
# HiPerGator
8/25/2022 5:25:52 PM: use singularity; do not use apptainer.

# SAMBHU19 Red Hat Enterprise Linux
8/26/2022 5:48:25 PM: 
```
python -u run/train_rl_parent_NeilBranch0.py |& tee out.txt  
```
9/1/2022 3:16:17 PM:  
sandbox
```
docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES="1" --
```
Jennifer's line
```
docker run --rm --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all nvidia/cuda nvidia-smi
```
TODO: install nvidia container runtime
9/1/2022 3:33:15 PM 
```
(carla) [nsambhu@localhost carla-roach]$ nvidia-container-toolkit
Usage of nvidia-container-toolkit:
  -config string
      configuration file
  -debug
      enable debug output
  -version
      enable version output

Commands:
  prestart
        run the prestart hook
  poststart
        no-op
  poststop
        no-op
```
9/1/2022 3:50:10 PM:
```
(base) [nsambhu@localhost Apptainer]$ nvidia-smi -i 0 --query-gpu=uuid --format=csv
uuid
GPU-118a9ae7-a087-d9dd-077a-8e7b871255f1
```
```
docker run --gpus device=GPU-118a9ae7-a087-d9dd-077a-8e7b871255f1 nvidia/cuda nvidia-smi
```
9/1/2022 4:13:21 PM: send to Jennifer
```
(carla) [nsambhu@localhost carla-roach]$ conda list carla
# packages in environment at /home/nsambhu/anaconda3/envs/carla:
#
# Name                    Version                   Build  Channel
carla                     0.9.5                    pypi_0    pypi
```
9/2/2022 3:04:21 PM: successful: 
```
(base) [nsambhu@localhost Apptainer]$ sudo docker run --privileged --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh
```
9/2/2022 3:06:10 PM: TODO: Docker 1.13.1 select GPU  
9/2/2022 3:11:19 PM: (1) remove docker and (2) follow https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html  
9/2/2022 3:20:08 PM:
```
(base) [nsambhu@localhost Apptainer]$ sudo docker run --rm -e NVIDIA_VISIBLE_DEVICES=all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
Failed to initialize NVML: Insufficient Permissions
```
```
(base) [nsambhu@localhost Apptainer]$ sudo docker run --security-opt=label=disable --rm -e NVIDIA_VISIBLE_DEVICES=all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
Fri Sep  2 19:20:33 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 515.65.01    Driver Version: 515.65.01    CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA TITAN RTX    Off  | 00000000:01:00.0  On |                  N/A |
| 41%   40C    P8    19W / 280W |    226MiB / 24576MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA TITAN RTX    Off  | 00000000:21:00.0 Off |                  N/A |
| 41%   36C    P8    14W / 280W |      1MiB / 24576MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```
9/2/2022 3:24:23 PM: try docker select gpu
```
(base) [nsambhu@localhost Apptainer]$ sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.12 /bin/bash ./CarlaUE4.sh
unknown flag: --gpus
See 'docker run --help'.
```
```
sudo docker run --security-opt=label=disable --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.12 /bin/bash ./CarlaUE4.sh
```
9/2/2022 4:04:07 PM: 
```
sudo -S docker run --privileged --gpus "device=1" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port=2000 -RenderOffScreen
sudo -S docker run --privileged --gpus "device=1" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port=2000
```
```
(base) [nsambhu@localhost Apptainer]$ sudo -S docker run --privileged --gpus "device=1" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port=2000
[sudo] password for nsambhu: 
unknown flag: --gpus
See 'docker run --help'.
```

# SSD Red Hat Enterprise Linux 7
## Apptainer namespace
9/12/2022 5:16:54 PM: why newest apptainer won't run: https://github.com/apptainer/apptainer/issues/686  
configure user namespace: https://apptainer.org/docs/admin/main/user_namespace.html  
9/12/2022 5:21:03 PM: use --fix-perms when building docker CARLA  
9/12/2022 5:31:13 PM: build
```
apptainer build --sandbox carla_0.9.13 docker://carlasim/carla:0.9.13
```
run
```
apptainer exec -w carla_0.9.13 bash
```
9/12/2022 6:07:09 PM: run CARLA
```
apptainer run --nvccli carla_0.9.13 /home/carla/CarlaUE4.sh
```
# SAMBHU19 Ubuntu 18.04
9/13/2022 3:31 PM: check training on 5 towns per GPU. TODO: inference to recreate table of ICCV 2021 carla-roach.  
```
python -u run/train_rl_parent_NeilBranch0.py |& tee out.txt  
```
9/13/2022 4:00 PM: TODO: get docker CARLA working through training.  
9/13/2022 4:14 PM: new anaconda environment: carla3

# SSD Red Hat Enterprise Linux 8
9/14/2022 3:47:11 PM: bookmark https://www.redhat.com/en/blog/how-use-gpus-containers-bare-metal-rhel-8  
9/16/2022 5:04:46 PM: rootless container setup: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#step-3-rootless-containers-setup  
9/16/2022 5:25:07 PM: modify server_utils.py for podman  
9/16/2022 5:25:36 PM: create conda environment carla from environment.yml  
```
conda env create -f environment.yml
```
9/16/2022 5:26:11 PM: TODO:  
python -u run/train_rl_parent_NeilBranch0.py |& tee out.txt  
9/16/2022 5:38:40 PM: creating carla anaconda environment and installing carla forces carla to be 0.9.5.  
9/16/2022 5:39:42 PM: 
```
(c0) [nsambhu@localhost carla-roach]$ conda env update --file environment.yml --prune
```