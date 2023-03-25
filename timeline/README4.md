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
9/17/2022 6:43:11 PM: setup anaconda environment:  
```
conda env create -f environment.yml
conda activate carla
pip3 install --upgrade pip
pip install carla
```
9/17/2022 7:42:23 PM: On Ubuntu 18.04, I could do 5 towns on 1 card or 4 towns on each card. In RHEL 8, I can do 5 towns on 1 card or 3 towns on each card.
## Benchmark carla-roach
9/19/2022 4:08:33 PM: TODO: find call to carla instance during benchmark  
9/19/2022 4:10:38 PM: call to carla for benchmark is same as call to carla for training  
9/19/2022 4:12:12 PM: benchmark
```
bash run/benchmark_NeilBranch0.sh |& tee out.txt
```
9/19/2022 4:34:07 PM: benchmark with time
```
time bash run/benchmark_NeilBranch0.sh |& tee out.txt
```
9/19/2022 11:46:49 PM: only trained env_idx 0: https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/c0pjqnzt?workspace=user-neilsambhu  
9/20/2022 2:47:27 PM: inference on Roach for NoCrash dense:  
[nsambhu@localhost carla-roach]$ cat out.txt | grep "View run at "  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/1sy0ktpm  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/1o359phk  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2p2lxnrv  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/3hp1bvog  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/1wsvip8l  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/1xg9ozfh  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2cl9dvm2  
9/23/2022 9:49:27 AM: inference on PPO+beta for NoCrash dense:  
[nsambhu@localhost ~]$ cat ~/github/carla-roach/out.txt | grep "View run at "  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2hzipkzv  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2j3mrf4x  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/f89qyky1  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2aa47u1s  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/3pza7k8j  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/ebyabqbi  
9/24/2022 4:42:48 PM: inference on PPO+beta for NoCrash busy:  
[nsambhu@localhost ~]$ cat ~/github/carla-roach/out.txt | grep "View run at "  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/24065p0s  
9/26/2022 5:04:40 PM: inference on PPO+beta for NoCrash busy  
```
[2022-09-25 16:34:58,863][__main__][INFO] - Finished, 1/1
wandb.log: <bound method Run.log of <wandb.sdk.wandb_run.Run object at 0x7f22f40d9490>>
Traceback (most recent call last):
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "benchmark_NeilBranch0.py", line 304, in main
    print(f'wandb.log.summary: {wandb.log.summary}')
AttributeError: 'function' object has no attribute 'summary'
```
9/26/2022 6:41:21 PM: find weather_group
```
grep -r  --exclude timeline/README1.md --exclude timeline/README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "weather_group">outgrep.txt
```
9/26/2022 7:04:18 PM: weather_group does not have integer of count. Try to find "25" for weather instances.  
```
grep -r  --exclude timeline/README1.md --exclude timeline/README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "25">outgrep.txt
```
9/26/2022 7:15:43 PM: no weather instances of "25". Search for "summary".
```
grep -r --exclude-dir=outputs --exclude *README1.md --exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "summary">outgrep.txt
```
```
README.md:license, please contact the authors. You can view a license summary here.
benchmark.py:    wandb.log({'table/summary': wandb.Table(data=table_data, columns=table_columns)})
benchmark_NeilBranch0.py:        #print(f'wandb.log.summary: {wandb.log.summary}
benchmark_NeilBranch0.py:    wandb.log({'table/summary': wandb.Table(data=table_data, columns=table_columns)})
benchmark_NeilBranch0.py:        print(f'wandb.summary: {wandb.summary}')
carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py:            # save episode summary
data_collect.py:    wandb.log({'table/summary': wandb.Table(data=table_data, columns=table_columns)})
data_collect_NeilBranch0.py:    wandb.log({'table/summary': wandb.Table(data=table_data, columns=table_columns)})
```
9/26/2022 11:55:05 PM: inference on PPO+beta for NoCrash busy (25 tasks per weather)  
```
[2022-09-26 20:17:24,759][__main__][INFO] - Finished Benchmarking env_idx 0, suite_name: ppo_NoCrash-v3_Town01_lbc_train_eval
[2022-09-26 20:17:24,760][__main__][INFO] - Finished, 1/1
wandb.log: <bound method Run.log of <wandb.sdk.wandb_run.Run object at 0x7f9ae8519410>>
wandb.summary: <wandb.sdk.wandb_summary.Summary object at 0x7f9ae8519490>
[2022-09-26 20:17:24,789][__main__][INFO] - data_collect.py DONE!
```
9/27/2022 12:10:04 AM: inference on PPO+beta for NoCrash busy (1 task per weather)  
```
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2a1uvpog
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-09-26/23-59-52/wandb/run-20220927_000007-2a1uvpog
wandb: Run `wandb offline` to turn off syncing.

[2022-09-27 00:00:08,746][__main__][INFO] - Start Benchmarking WetNoon_00.
CarlaUE4-Linux: no process found
[2022-09-27 00:07:07,985][utils.server_utils][INFO] - Kill Carla Servers!
[2022-09-27 00:07:12,990][utils.server_utils][INFO] - Kill Carla Servers!
[2022-09-27 00:07:12,996][__main__][INFO] - Finished Benchmarking env_idx 0, suite_name: ppo_NoCrash-v3_Town01_lbc_train_eval
[2022-09-27 00:07:12,996][__main__][INFO] - Finished, 1/1
wandb.log: <bound method Run.log of <wandb.sdk.wandb_run.Run object at 0x7f663031b510>>
wandb.summary: <wandb.sdk.wandb_summary.Summary object at 0x7f66303151d0>
[2022-09-27 00:07:13,007][__main__][INFO] - data_collect.py DONE!
```
9/27/2022 12:12:49 AM: find "score_composed"  
```
grep -r --exclude-dir=outputs --exclude *README1.md --exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "score_composed">outgrep.txt
```
never mind  
9/27/2022 12:29:50 AM: inference on PPO+beta for NoCrash busy (1 task per weather)  
```

wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/3eeui02p
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-09-27/00-21-47/wandb/run-20220927_002201-3eeui02p
wandb: Run `wandb offline` to turn off syncing.

[2022-09-27 00:22:02,530][__main__][INFO] - Start Benchmarking WetNoon_00.
CarlaUE4-Linux: no process found
[2022-09-27 00:28:17,308][utils.server_utils][INFO] - Kill Carla Servers!
[2022-09-27 00:28:22,313][utils.server_utils][INFO] - Kill Carla Servers!
[2022-09-27 00:28:22,318][__main__][INFO] - Finished Benchmarking env_idx 0, suite_name: ppo_NoCrash-v3_Town01_lbc_train_eval
[2022-09-27 00:28:22,318][__main__][INFO] - Finished, 1/1
wandb.log: <bound method Run.log of <wandb.sdk.wandb_run.Run object at 0x7efc2c3da790>>
wandb.summary: <wandb.sdk.wandb_summary.Summary object at 0x7efc78a67710>
table_columns: ['Suite', 'actor_id', 'n_episode', 'collisions_layout', 'collisions_others', 'collisions_pedestrian', 'collisions_vehicle', 'encounter_light', 'encounter_stop', 'is_route_completed', 'is_route_completed_nocrash', 'length', 'light_passed', 'percentage_outside_lane', 'percentage_wrong_lane', 'red_light', 'reward', 'route_completed_in_km', 'route_dev', 'route_length_in_km', 'score_composed', 'score_penalty', 'score_route', 'stop_infraction', 'stop_passed', 'timeout', 'vehicle_blocked', 'n_episodes']
table_data: [['ppo_NoCrash-v3_Town01_lbc_train_eval', 'hero', '1', '0.0000', '0.0000', '0.0000', '0.0000', '9.0000', '0.0000', '1.0000', '1.0000', '4429.0000', '9.0000', '0.0000', '0.0000', '0.0000', '3464.7315', '0.8242', '0.0000', '0.8322', '1.0000', '1.0000', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '1.0000']]
[2022-09-27 00:28:22,323][__main__][INFO] - data_collect.py DONE!
```
9/27/2022 12:51:02 AM: inference on PPO+beta for NoCrash busy (2 tasks per weather)  
```
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/q6bx2mkr
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-09-27/00-36-24/wandb/run-20220927_003639-q6bx2mkr
wandb: Run `wandb offline` to turn off syncing.

[2022-09-27 00:36:39,632][__main__][INFO] - Start Benchmarking WetNoon_00.
[2022-09-27 00:46:43,258][__main__][INFO] - Start Benchmarking WetNoon_01.
CarlaUE4-Linux: no process found
[2022-09-27 00:49:33,236][utils.server_utils][INFO] - Kill Carla Servers!
[2022-09-27 00:49:38,240][utils.server_utils][INFO] - Kill Carla Servers!
[2022-09-27 00:49:38,244][__main__][INFO] - Finished Benchmarking env_idx 0, suite_name: ppo_NoCrash-v3_Town01_lbc_train_eval
[2022-09-27 00:49:38,244][__main__][INFO] - Finished, 1/1
table_columns: ['Suite', 'actor_id', 'n_episode', 'collisions_layout', 'collisions_others', 'collisions_pedestrian', 'collisions_vehicle', 'encounter_light', 'encounter_stop', 'is_route_completed', 'is_route_completed_nocrash', 'length', 'light_passed', 'percentage_outside_lane', 'percentage_wrong_lane', 'red_light', 'reward', 'route_completed_in_km', 'route_dev', 'route_length_in_km', 'score_composed', 'score_penalty', 'score_route', 'stop_infraction', 'stop_passed', 'timeout', 'vehicle_blocked', 'n_episodes']
table_data: [['ppo_NoCrash-v3_Town01_lbc_train_eval', 'hero', '2', '0.0000', '0.0000', '0.0000', '0.6066', '6.5000', '0.0000', '1.0000', '0.5000', '4559.5000', '6.0000', '0.0000', '0.0000', '0.6066', '3264.0164', '0.7268', '0.0000', '0.7338', '0.7100', '0.7100', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '2.0000']]
table_data[0]: ['ppo_NoCrash-v3_Town01_lbc_train_eval', 'hero', '2', '0.0000', '0.0000', '0.0000', '0.6066', '6.5000', '0.0000', '1.0000', '0.5000', '4559.5000', '6.0000', '0.0000', '0.0000', '0.6066', '3264.0164', '0.7268', '0.0000', '0.7338', '0.7100', '0.7100', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '2.0000']
dict_table: {'Suite': 'ppo_NoCrash-v3_Town01_lbc_train_eval', 'actor_id': 'hero', 'n_episode': '2', 'collisions_layout': '0.0000', 'collisions_others': '0.0000', 'collisions_pedestrian': '0.0000', 'collisions_vehicle': '0.6066', 'encounter_light': '6.5000', 'encounter_stop': '0.0000', 'is_route_completed': '1.0000', 'is_route_completed_nocrash': '0.5000', 'length': '4559.5000', 'light_passed': '6.0000', 'percentage_outside_lane': '0.0000', 'percentage_wrong_lane': '0.0000', 'red_light': '0.6066', 'reward': '3264.0164', 'route_completed_in_km': '0.7268', 'route_dev': '0.0000', 'route_length_in_km': '0.7338', 'score_composed': '0.7100', 'score_penalty': '0.7100', 'score_route': '1.0000', 'stop_infraction': '0.0000', 'stop_passed': '0.0000', 'timeout': '0.0000', 'vehicle_blocked': '0.0000', 'n_episodes': '2.0000'}
[2022-09-27 00:49:38,245][__main__][INFO] - data_collect.py DONE!
```
9/27/2022 8:08:58 PM: inference on Roach for NoCrash dense:  
[nsambhu@localhost ~]$ cat ~/github/carla-roach/out.txt | grep "View run at "  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/qlnixdwq  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/2f2hym4t  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/1hxy3keu  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/3h9ygqz4  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/ap5yaa97  
wandb: 🚀 View run at https://wandb.ai/neilsambhu/iccv21-roach-benchmark/runs/1aje1zxu  
```
[2022-09-27 14:29:19,249][__main__][INFO] - Finished Benchmarking env_idx 3, suite_name: ppo_NoCrash-v2_Town02_lbc_new
[2022-09-27 14:29:19,249][__main__][INFO] - Finished, 4/4
score_composed: 0.8254
score_route: 0.8616
[2022-09-27 14:29:19,251][__main__][INFO] - data_collect.py DONE!
```
TODO: print score_composed and score_route after each env_idx is finished  
9/28/2022 1:05:38 PM: inference on Roach for NoCrash dense:  
```
[2022-09-28 00:37:02,544][__main__][INFO] - Finished Benchmarking env_idx 0, suite_name: ppo_NoCrash-v2_Town01_lbc_train_eval
score_composed: 0.9762, score_route: 0.9972
[2022-09-28 00:37:02,544][__main__][INFO] - Not finished, 1/4
```
score_composed and score_route successfully print for each env_idx finished.  
TODO: run benchmark_parent_NeilBranch0.py  
9/28/2022 1:53:13 PM: 
```
python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
```
9/28/2022 2:02:22 PM: error with wb_group  
9/28/2022 2:02:39 PM: 
```
bash run/benchmark_NeilBranch0.sh |& tee out.txt
Neil benchmark_NeilBranch0.py:329
os.getcwd() /home/nsambhu/github/carla-roach/outputs/2022-09-28/14-00-49
type(cfg) <class 'omegaconf.dictconfig.DictConfig'>
cfg {'actors': {'hero': {'agent': 'ppo', 'reward': {'entry_point': 'reward.valeo_action:ValeoAction'}, 'terminal': {'entry_point': 'terminal.leaderboard:Leaderboard'}}}, 'carla_sh_path': '/CarlaUE4.sh', 'log_level': 'INFO', 'host': 'localhost', 'port': 2000, 'seed': 2021, 'no_rendering': True, 'kill_running': True, 'resume': True, 'wb_project': 'iccv21-roach-benchmark', 'wb_notes': 'Benchmark Roach on NoCrash-dense.', 'wb_group': 'Roach', 'wb_tags': None, 'log_video': True, 'agent': {'ppo': {'entry_point': 'agents.rl_birdview.rl_birdview_agent:RlBirdviewAgent', 'wb_run_path': 'iccv21-roach/trained-models/1929isj0', 'wb_ckpt_step': None, 'env_wrapper': {'entry_point': 'agents.rl_birdview.utils.rl_birdview_wrapper:RlBirdviewWrapper', 'kwargs': {'input_states': ['control', 'vel_xy'], 'acc_as_action': True}}}}, 'test_suites': [{'env_id': 'NoCrash-v2', 'env_configs': {'route_description': 'lbc', 'carla_map': 'Town01', 'weather_group': 'train_eval'}}, {'env_id': 'NoCrash-v2', 'env_configs': {'route_description': 'lbc', 'carla_map': 'Town01', 'weather_group': 'new'}}, {'env_id': 'NoCrash-v2', 'env_configs': {'route_description': 'lbc', 'carla_map': 'Town02', 'weather_group': 'train_eval'}}, {'env_id': 'NoCrash-v2', 'env_configs': {'route_description': 'lbc', 'carla_map': 'Town02', 'weather_group': 'new'}}], 'wb_sub_group': 'nocrash_dense-2021'}
```
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
Neil benchmark_NeilBranch0.py:329
LexerNoViableAltException: 'wb_group="PPO+exp"'
                           ^
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
```
9/28/2022 6:58:05 PM: inference on PPO+exp for NoCrash dense train town:  
```
[2022-09-28 18:36:01,791][__main__][INFO] - Finished Benchmarking env_idx 0, suite_name: ppo_NoCrash-v2_Town01_lbc_train_eval
score_composed: 0.9295, score_route: 0.9641
[2022-09-28 18:36:01,791][__main__][INFO] - Finished, 1/1
```
10/1/2022 1:12:43 PM: delete checkpoint files after each new seed  
10/1/2022 1:20:23 PM: TODO: print benchmark configuration before calling benchark script  
10/1/2022 7:05:03 PM:
```
PPO+exp nocrash_dense_tt
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 1.0, 0.0
PPO+exp nocrash_dense_tn
        success rate (average, standard deviation): 0.9775, 0.031819805153394644
        driving score (average, standard deviation): 0.8842333333333334, 0.08410613665020064
```
10/2/2022 1:08:16 PM: Roach duplicated for results (2 weathers)
```
PPO+exp nocrash_dense_tt
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 0.8933, 0.1508
PPO+beta nocrash_dense_tt
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 1.0, 0.0
Roach nocrash_dense_tt
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 1.0, 0.0
Roach nocrash_dense_tt
        success rate (average, standard deviation): 0.9214, 0.1758
        driving score (average, standard deviation): 0.8945, 0.1775
PPO+exp nocrash_dense_tn
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 0.9333, 0.0943
PPO+beta nocrash_dense_tn
        success rate (average, standard deviation): 0.9175, 0.1167
        driving score (average, standard deviation): 0.8838, 0.1643
Roach nocrash_dense_tn
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 1.0, 0.0
Roach nocrash_dense_tn
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 1.0, 0.0
PPO+exp nocrash_dense_nt
        success rate (average, standard deviation): 0.6683, 0.27
        driving score (average, standard deviation): 0.3768, 0.2458
PPO+beta nocrash_dense_nt
        success rate (average, standard deviation): 0.8702, 0.1835
        driving score (average, standard deviation): 0.7221, 0.1101
Roach nocrash_dense_nt
        success rate (average, standard deviation): 0.5725, 0.3298
        driving score (average, standard deviation): 0.5546, 0.3505
Roach nocrash_dense_nt
        success rate (average, standard deviation): 0.7063, 0.3128
        driving score (average, standard deviation): 0.6723, 0.3455
PPO+exp nocrash_dense_nn
        success rate (average, standard deviation): 0.8872, 0.1595
        driving score (average, standard deviation): 0.7323, 0.2508
PPO+beta nocrash_dense_nn
        success rate (average, standard deviation): 1.0, 0.0
        driving score (average, standard deviation): 0.8067, 0.1367
Roach nocrash_dense_nn
        success rate (average, standard deviation): 0.5033, 0.016
        driving score (average, standard deviation): 0.5015, 0.0185
Roach nocrash_dense_nn
        success rate (average, standard deviation): 0.5375, 0.2365
        driving score (average, standard deviation): 0.4706, 0.1703
```
10/7/2022 3:36:58 PM: carla-roach (50 weathers)
```
PPO+exp nocrash_dense_tt
	success rate (average, standard deviation): 0.9927, 0.0
	driving score (average, standard deviation): 0.9427, 0.0
PPO+beta nocrash_dense_tt
	success rate (average, standard deviation): 0.9789, 0.015
	driving score (average, standard deviation): 0.9497, 0.0231
Roach nocrash_dense_tt
	success rate (average, standard deviation): 0.9812, 0.0
	driving score (average, standard deviation): 0.9592, 0.0
Autopilot nocrash_dense_tt
	success rate (average, standard deviation): 0.9647, 0.0178
	driving score (average, standard deviation): 0.8803, 0.0608
PPO+exp nocrash_dense_tn
	success rate (average, standard deviation): 0.9917, 0.0058
	driving score (average, standard deviation): 0.9684, 0.0082
PPO+beta nocrash_dense_tn
	success rate (average, standard deviation): 1.0, 0.0
	driving score (average, standard deviation): 0.9706, 0.0054
Roach nocrash_dense_tn
	success rate (average, standard deviation): 0.9953, 0.0033
	driving score (average, standard deviation): 0.9732, 0.0105
Autopilot nocrash_dense_tn
	success rate (average, standard deviation): 0.9867, 0.0066
	driving score (average, standard deviation): 0.8538, 0.0047
PPO+exp nocrash_dense_nt
	success rate (average, standard deviation): 0.9698, 0.0106
	driving score (average, standard deviation): 0.8678, 0.0105
PPO+beta nocrash_dense_nt
	success rate (average, standard deviation): 0.962, 0.0137
	driving score (average, standard deviation): 0.8757, 0.0374
Roach nocrash_dense_nt
	success rate (average, standard deviation): 0.9093, 0.0416
	driving score (average, standard deviation): 0.8338, 0.0279
Autopilot nocrash_dense_nt
	success rate (average, standard deviation): 0.9156, 0.0007
	driving score (average, standard deviation): 0.6875, 0.0041
PPO+exp nocrash_dense_nn
	success rate (average, standard deviation): 0.9798, 0.0113
	driving score (average, standard deviation): 0.8961, 0.0172
PPO+beta nocrash_dense_nn
	success rate (average, standard deviation): 0.9724, 0.0007
	driving score (average, standard deviation): 0.918, 0.0341
Roach nocrash_dense_nn
	success rate (average, standard deviation): 0.848, 0.0
	driving score (average, standard deviation): 0.804, 0.0
Autopilot nocrash_dense_nn
	success rate (average, standard deviation): 0.8688, 0.0295
	driving score (average, standard deviation): 0.7775, 0.0374
```
10/8/2022 2:27:47 PM: TODO: debug IL inference  
10/8/2022 3:03:04 PM: 
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
benchmark configuration: L_A(AP) trained on NoCrash benchmark nocrash_dense_tt-2021
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP) trained on NoCrash benchmark" wb_notes="Benchmark
L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=true
Traceback (most recent call last):
  File "run/benchmark_parent_NeilBranch0.py", line 101, in <module>
    benchmarkConfiguration.Benchmark()
  File "run/benchmark_parent_NeilBranch0.py", line 46, in Benchmark
    benchmarkProcess = self.StartBenchmarkProcess(seed)
  File "run/benchmark_parent_NeilBranch0.py", line 37, in StartBenchmarkProcess
    benchmarkProcess = subprocess.Popen([cmd])
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/subprocess.py", line 800, in __init__
    restore_signals, start_new_session)
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/subprocess.py", line 1551, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP) trained on NoCrash benchmark" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=true': 'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP) trained on NoCrash benchmark" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=true'
```
```
(carla) [nsambhu@localhost carla-roach]$ python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP) trained on NoCrash benchmark" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=true
mismatched input ' ' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
```
10/8/2022 7:03:52 PM: cilrs  
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
benchmark configuration: L_A(AP) trained on NoCrash benchmark nocrash_dense_tt-2021
mismatched input ' ' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
score_composed: [0.7246], score_route: [0.9105]
benchmark configuration: L_A(AP) trained on NoCrash benchmark nocrash_dense_tt-2022
mismatched input ' ' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details
```
cirls with cmd  
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
benchmark configuration: L_A(AP) trained on NoCrash benchmark nocrash_dense_tt-2021
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP) trained on NoCrash benchmark" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=true
mismatched input ' ' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
score_composed: [0.7246], score_route: [0.9105]
benchmark configuration: L_A(AP) trained on NoCrash benchmark nocrash_dense_tt-2022
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP) trained on NoCrash benchmark" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2022 +wb_sub_group=nocrash_dense_tt-2022 no_rendering=true
mismatched input ' ' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details
```
ppo with cmd
```
benchmark configuration: PPO+exp nocrash_dense_tt-2021
ppo cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=ppo actors.hero.agent=ppo agent.ppo.wb_run_path=iccv21-roach/trained-models/10pscpih wb_group="PPO+exp" wb_notes="Benchmark PPO+exp on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=true
```
10/8/2022 7:25:10 PM: cirls (i.e. change no_rendering from true to false)
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
benchmark configuration: L_A(AP) nocrash_dense_tt-2021
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP)" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=false
Error parsing override 'wb_group=L_A(AP)'
HydraException while evaluating 'L_A(AP)': Unknown function 'L_A'
Available: bool,choice,float,glob,int,interval,range,shuffle,sort,str,tag

See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
score_composed: [0.7246], score_route: [0.9105]
benchmark configuration: L_A(AP) nocrash_dense_tt-2022
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="L_A(AP)" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2022 +wb_sub_group=nocrash_dense_tt-2022 no_rendering=false
```
10/8/2022 7:56:38 PM: TODO: find wb_group
```
grep -r --exclude-dir=outputs --exclude *README1.md --exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "wb_group">outgrep.txt
```
10/8/2022 8:10:25 PM: cilrs wb_group="L_K+L_F(c)"
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
benchmark configuration: L_K+L_F(c) nocrash_dense_tt-2021
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/31u9tki7 wb_group="L_K+L_F(c)" wb_notes="Benchmark L_K+L_F(c) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=false
mismatched input '(' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
score_composed: [0.7246], score_route: [0.9105]
benchmark configuration: L_K+L_F(c) nocrash_dense_tt-2022
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/31u9tki7 wb_group="L_K+L_F(c)" wb_notes="Benchmark L_K+L_F(c) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2022 +wb_sub_group=nocrash_dense_tt-2022 no_rendering=false
mismatched input '(' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details
```
cilrs wb_group="bc_data"
```
(carla) [nsambhu@localhost carla-roach]$ python -u run/benchmark_parent_NeilBranch0.py |& tee out.txt
benchmark configuration: bc_data nocrash_dense_tt-2021
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="bc_data" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2021 +wb_sub_group=nocrash_dense_tt-2021 no_rendering=false
mismatched input '(' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
score_composed: [0.7246], score_route: [0.9105]
benchmark configuration: bc_data nocrash_dense_tt-2022
cilrs cmd: python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent=cilrs actors.hero.agent=cilrs agent.cilrs.wb_run_path=iccv21-roach/trained-models/39o1h862 wb_group="bc_data" wb_notes="Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-tt." test_suites=nocrash_dense_tt seed=2022 +wb_sub_group=nocrash_dense_tt-2022 no_rendering=false
mismatched input '(' expecting <EOF>
See https://hydra.cc/docs/next/advanced/override_grammar/basic for details
```
10/8/2022 9:57:41 PM: TODO: use non-parent bash script for inference to see IL inference results  
10/9/2022 3:20:50 PM: TODO: map IL inference to \*.yaml.  
10/9/2022 3:28:34 PM: no need to map IL inference: the NoCrash Dense is already split among the 4 environment files  
10/9/2022 4:15:13 PM: TODO: benchmark_NeilBranch0.sh: benchmark.py should be benchmark_NeilBranch0.py.  
10/10/2022 6:10:23 PM: results from non-parent bash script for IL inference using benchmark.py instead of benchmark_NeilBranch0.py: https://github.com/neilsambhu/carla-roach/blob/13fcf5685c6c8eb81e97c534c5449e41300e438b/out.txt  
10/10/2022 7:21:28 PM: changing benchmark.py to benchmark_NeilBranch0.py didn't change the output. I changed the test_suites to only 1 environment instead of 4.  
10/10/2022 7:40:53 PM: waiting on results to see if new command works for IL inference (1 environment).  
### inference handles crashes
10/13/2022 11:16:38 AM: inference on L_K+L_F(c) (50 weathers)  
```
L_K+L_F(c) nocrash_dense_tt
        success rate (average, standard deviation): 0.9762, 0.0074
        driving score (average, standard deviation): 0.8767, 0.0041
```
out.txt: https://github.com/neilsambhu/carla-roach/blob/5af49e30dc89ec0c4bc753a728d6cd42ab80fa60/out.txt  
TODO: verify cmd for L_A(AP)  
10/13/2022 11:38:58 AM: TODO: benchmark_parent_NeilBranch0.py: create ResultsLatex() function for results to be easily imported into Overleaf.  
10/13/2022 12:02:53 PM: functional inference: https://github.com/neilsambhu/carla-roach/blob/8daa28cabc34d806a80f75b59a9664c0038e2faf/run/benchmark_parent_NeilBranch0.py  
10/13/2022 1:29:39 PM: TODO: check for process flow of RL and IL (1 weather per environment).  
10/13/2022 1:46:39 PM: TODO: switch IL from NoCrash to DAGGER.  
10/14/2022 12:30:20 PM: (1) TODO: check for process flow of RL and IL (1 weather per environment). (2) no need to switch IL from NoCrash to DAGGER.  
10/27/2022 10:39:47 AM: inference on first cell in LB-all column
```
Traceback (most recent call last):
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "benchmark_NeilBranch0.py", line 177, in main
    seed=cfg.seed, no_rendering=cfg.no_rendering, **env_setup['env_configs'])
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/gym/envs/registration.py", line 145, in make
    return registry.make(id, **kwargs)
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/gym/envs/registration.py", line 90, in make
    env = spec.make(**kwargs)
  File "/home/nsambhu/.conda/envs/carla/lib/python3.7/site-packages/gym/envs/registration.py", line 60, in make
    env = cls(**_kwargs)
  File "/home/nsambhu/github/carla-roach/carla_gym/envs/suites/leaderboard_env.py", line 13, in __init__
    obs_configs, reward_configs, terminal_configs, all_tasks)
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 32, in __init__
    self._init_client(carla_map, host, port, seed=seed, no_rendering=no_rendering)
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 162, in _init_client
    self._world = client.load_world(carla_map)
RuntimeError: map not found
```
11/14/2022 10:32:42 PM: TODO: find carla to add texture to objects in simulation
```
grep -r --exclude-dir=outputs --exclude *README1.md --exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "import carla">outgrep.txt
```
11/14/2022 10:36:16 PM: TODO: try to run CARLA simulator with GUI displayed. Significance: I can see changes to the textures of objects. 
11/30/2022 2:00:29 PM: I have the code working to see CARLA simulator with GUI displayed. TODO: view ego vehicle during inference. TODO: see where carla-roach lists "spawn_actor" or "world.wpawn_actor"
```
grep -r --exclude-dir=outputs --exclude *README1.md --exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "spawn_actor">outgrep.txt
```
12/3/2022 5:04:37 PM:  
ego_vehicle_handler.py requires "client" object.  
carla_multi_agent_env.py (1) initializes EgoVehcileHandler with self.\_client and (2) self.\_client is set to the client object. TODO: get "client" object to connect to podman instance of carla simulator.  
```
host: localhost	
port: 2000
```
12/3/2022 5:36:38 PM: successfully able to connect to podman carla simulator for carla client python object. For CLI podman carla, manual_control.py prints "Waiting for the ego vehicle".  
12/5/2022 4:48:57 PM: already successfully modified carla-roach code to show view of ego vehicle from manual_control.py. Code modification is in benchmark_NeilBranch0.py.  
12/5/2022 4:50:14 PM: TODO: find where in carla-roach there is "load_world(town)" or "self.client.load_world(town)".  
```
grep -r --exclude-dir=outputs --exclude *README1.md --exclude *README2.md --exclude *README3.md --exclude *README4.md --exclude out.txt --exclude outgrep.txt --exclude *.log --exclude *.wandb -e "load_world(">outgrep.txt
```
12/5/2022 10:28:50 PM: create regex to filter vehicles from list of objects  
# Podman Ubuntu 18.04
2/1/2023 8:24:43 PM: made podman-carla/0ubuntu.sh file. Use Ctrl+P+Q to detach from container.
## Attempt 1: (failed) Commands to install CARLA 0.9.13 within the Ubuntu container
~~2/1/2023 8:52:21 PM:
```
apt-get update &&
apt-get install wget software-properties-common &&
add-apt-repository ppa:ubuntu-toolchain-r/test &&
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - &&
apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main" &&
apt-get update
```
2/1/2023 9:05:53 PM:
```
apt-get install build-essential clang-8 lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git
```
2/1/2023 9:09:04 PM:
```
update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 &&
update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180
```
2/1/2023 9:10:14 PM:
```
pip3 install --upgrade pip
```
2/1/2023 9:12:06 PM:
```
pip install --user setuptools &&
pip3 install --user -Iv setuptools==47.3.1 &&
pip install --user distro &&
pip3 install --user distro &&
pip install --user wheel &&
pip3 install --user wheel auditwheel
```
2/1/2023 9:14:59 PM:
```
git clone --depth 1 -b carla https://github.com/CarlaUnreal/UnrealEngine.git ~/UnrealEngine_4.26
```
~~
## Attempt 2: Commands to install CARLA 0.9.13 within the Ubuntu container
2/2/2023 11:15:51 AM:
```
apt-get update &&
apt-get install wget software-properties-common &&
add-apt-repository ppa:ubuntu-toolchain-r/test &&
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - &&
apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main" &&
apt-get update &&
apt-get install build-essential clang-8 lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git &&
update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 &&
update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180 &&
pip3 install --upgrade pip &&
pip3 install --user pygame numpy
```
2/2/2023 11:21:32 AM:
```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1AF1527DE64CB8D9 &&
add-apt-repository "deb [arch=amd64] http://dist.carla.org/carla $(lsb_release -sc) main"
```
2/2/2023 11:23:54 AM:
```
apt-get update &&
apt-get install carla-simulator=0.9.13 &&
cd /opt/carla-simulator/Import
```
2/2/2023 11:49:46 AM:
```
curl -O https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/AdditionalMaps_0.9.13.tar.gz -O https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.13.tar.gz -O https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.13_RSS.tar.gz
```
2/2/2023 12:52:00 PM:
```
cd .. &&
chmod -R 777 /opt/carla-simulator &&
./ImportAssets.sh
```
2/2/2023 1:15:17 PM:
```
useradd nsambhu &&
passwd nsambhu
```
2/2/2023 1:18:59 PM:
```
su nsambhu
```
2/2/2023 1:21:07 PM:
```
./CarlaUE4.sh
```
## Save podman to hard disk
2/2/2023 1:24:42 PM:
```
podman save docker.io/library/ubuntu:18.04 > mycontainer.tar
```
2/2/2023 1:32:27 PM:
```
podman stop mycontainer
```
2/2/2023 1:32:39 PM:
```
podman load < mycontainer.tar
```
2/3/2023 5:16:59 PM: TODO: find out how to save a podman container to hard disk, reboot machine, and load container from hard disk.  
## Save podman image to hard disk (full process)
2/6/2023 10:56:53 AM:  
list images
```
podman images
```
remove old image  
```
podman rmi --force <image id>
```
list images
```
podman images
```
2/6/2023 10:35:25 AM:  
run Ubuntu script
```
./0ubuntu.sh
```
modify Ubuntu contianer
```
touch ~/example.txt
```
detach from container: Ctrl+P+Q  
export container
```
podman export mycontainer > mycontainer.tar
```
list images
```
podman images
```
remove image  
```
podman rmi --force <image id>
```
list images
```
podman images
```
import container
```
podman import mycontainer.tar
```
list images
```
podman images
```
start Ubuntu container
```
podman start <image id>
```
list containers
```
podman ps
```
## Save podman image to hard disk (full process) 2
https://www.geeksforgeeks.org/backing-up-a-docker-container/
## Save podman image to hard disk (full process) 3
2/6/2023 3:59:23 PM: TODO: (1) run docker ubuntu 18.04 and (2) touch ~/example.txt  
~## Dockerfile~  
~2/6/2023 6:07:27 PM: TODO: find ubuntu dockerfile with readme~  
2/7/2023 11:58:37 AM: TODO: write ~/example.txt file to container; make sure file exists through desktop reboot
# Podman Ubuntu 18.04: carla compiled from source
2/19/2023 3:08:23 PM: https://carla.readthedocs.io/en/0.9.13/build_linux/ following these instructions to create Dockerfile in carla-roach/podman-carla/4ubuntu-carla-source  
2/20/2023 2:50:25 PM: 
```
STEP 3/3: RUN apt-get update
Get:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease [1581 B]
Err:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY A4B469963BF863CC
Ign:2 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease
Get:3 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release [564 B]
Get:4 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release.gpg [833 B]
Get:5 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Packages [73.8 kB]
Get:6 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Get:7 http://archive.ubuntu.com/ubuntu bionic InRelease [242 kB]
Get:8 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 Packages [23.8 kB]
Get:9 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [3190 kB]
Get:10 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
Get:11 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [83.3 kB]
Get:12 http://security.ubuntu.com/ubuntu bionic-security/universe i386 Packages [1330 kB]
Get:13 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [1595 kB]
Get:14 http://security.ubuntu.com/ubuntu bionic-security/main i386 Packages [1637 kB]
Get:15 http://security.ubuntu.com/ubuntu bionic-security/multiverse i386 Packages [6602 B]
Get:16 http://security.ubuntu.com/ubuntu bionic-security/restricted amd64 Packages [1426 kB]
Get:17 http://archive.ubuntu.com/ubuntu bionic/multiverse i386 Packages [177 kB]
Get:18 http://archive.ubuntu.com/ubuntu bionic/restricted i386 Packages [13.5 kB]
Get:19 http://archive.ubuntu.com/ubuntu bionic/restricted amd64 Packages [13.5 kB]
Get:20 http://security.ubuntu.com/ubuntu bionic-security/restricted i386 Packages [38.8 kB]
Get:21 http://archive.ubuntu.com/ubuntu bionic/main amd64 Packages [1344 kB]
Get:22 http://archive.ubuntu.com/ubuntu bionic/multiverse amd64 Packages [186 kB]
Get:23 http://archive.ubuntu.com/ubuntu bionic/main i386 Packages [1328 kB]
Get:24 http://archive.ubuntu.com/ubuntu bionic/universe i386 Packages [11.3 MB]
Get:25 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages [11.3 MB]
Get:26 http://archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages [2011 kB]
Get:27 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [30.8 kB]
Get:28 http://archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages [2076 kB]
Get:29 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [2369 kB]
Get:30 http://archive.ubuntu.com/ubuntu bionic-updates/restricted i386 Packages [48.8 kB]
Get:31 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse i386 Packages [12.7 kB]
Get:32 http://archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages [1466 kB]
Get:33 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [3610 kB]
Get:34 http://archive.ubuntu.com/ubuntu bionic-backports/main amd64 Packages [64.0 kB]
Get:35 http://archive.ubuntu.com/ubuntu bionic-backports/main i386 Packages [64.1 kB]
Get:36 http://archive.ubuntu.com/ubuntu bionic-backports/universe i386 Packages [20.6 kB]
Get:37 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [20.5 kB]
Reading package lists...
W: GPG error: https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY A4B469963BF863CC
E: The repository 'https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease' is not signed.
Error: error building at STEP "RUN apt-get update": error while running runtime: exit status 100
```
2/20/2023 3:40:29 PM: need to change python 3.6 to python 3.7  
2/20/2023 4:08:26 PM: 
```
STEP 16/20: RUN pip3 install --user -Iv setuptools==47.3.1
Using pip 21.3.1 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
  Link requires a different Python (3.6.9 not in: '>=3.7'): https://files.pythonhosted.org/packages/4f/27/b51cc9cebfd53b168b8a187c844e7a67dc523dda76be9b46d532815df284/setuptools-59.7.0-py3-none-any.whl#sha256=0c8d5c36aea600828875ab751c03e2c52624edc8382a88a127e31bd8d860e34b (from https://pypi.org/simple/setuptools/) (requires-python:>=3.7)
```
2/20/2023 4:39:12 PM: https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-7-on-ubuntu-18-10/  how to change python 3.6 to python 3.7.  
2/21/2023 12:35:32 PM: TODO: github SSH
# CARLA hello world
2/26/2023 9:05:07 AM: problem: how to run a command after podman or docker display of carla? I can use podman in a python script like before.
# Podman Ubuntu 18.04: carla compiled from source (resume)
3/2/2023 1:48:30 PM: 
```
Setup successful.
Error: error committing container for step {Env:[DEBIAN_FRONTEND=noninteractive PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin CUDA_VERSION=10.1.243 CUDA_PKG_VERSION=10-1=10.1.243-1 LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility NVIDIA_REQUIRE_CUDA=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411] Command:run Args:[./Setup.sh] Flags:[] Attrs:map[] Message:RUN ./Setup.sh Original:RUN ./Setup.sh }: error copying layers and metadata for container "634057f208b325bcbfcba77ecaff8224641d662f55cae3570bb409b466c5abad": writing blob: storing blob to file "/var/tmp/storage246180599/1": write /var/tmp/storage246180599/1: no space left on device
```
```
sudo ln -s /data/data1/tmp_hdd tmp
```
3/3/2023 9:19:50 AM: 
```
Failed to download 'http://cdn.unrealengine.com/dependencies/UnrealEngine-7235308-3ea1d61ea5264fd9a0aba5ac630f4e2a/e8ffab06e9d0b101dc4c459df8a746e68594bd07': Disk full. Path /UnrealEngine_4.26/.git/ue4-gitdeps/e8 (IOException)
Result: 1
time="2023-03-02T14:08:13-05:00" level=error msg="error unmounting container: error saving updated state for build container \"106b1d49ce6ed7e2d054441972ccc5a9d6809910c22d4d944988f95bf2c9e3b1\": error saving builder state to \"/home/nsambhu/.local/share/containers/storage/overlay-containers/106b1d49ce6ed7e2d054441972ccc5a9d6809910c22d4d944988f95bf2c9e3b1/userdata/buildah.json\": open /home/nsambhu/.local/share/containers/storage/overlay-containers/106b1d49ce6ed7e2d054441972ccc5a9d6809910c22d4d944988f95bf2c9e3b1/userdata/.tmp-buildah.json2372903540: no space left on device"
Error: error building at STEP "RUN ./Setup.sh": error while running runtime: exit status 1
```
```
ln -s /data/data1/containers_hdd/ containers
```
3/3/2023 9:24:55 AM: error after moving container storage
```
STEP 3/32: RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
/bin/sh: error while loading shared libraries: libc.so.6: cannot change memory protections
Error: error building at STEP "RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC": error while running runtime: exit status 127
```
3/3/2023 9:32:01 AM: remove link to /data/data1/containers  
3/3/2023 10:48:03 AM: output from run.sh
```
Setup successful.
Error: error committing container for step {Env:[DEBIAN_FRONTEND=noninteractive PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin CUDA_VERSION=10.1.243 CUDA_PKG_VERSION=10-1=10.1.243-1 LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility NVIDIA_REQUIRE_CUDA=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411] Command:run Args:[./Setup.sh] Flags:[] Attrs:map[] Message:RUN ./Setup.sh Original:RUN ./Setup.sh }: error copying layers and metadata for container "ab2152da1b8a308db5f028f159876198a2cc5cd5d83b27dd1f5b985c3341f1ce": writing blob: adding layer with blob "sha256:931beabc8aa86855c834980011705ea61a749b371e761efd8877344832083bc4": processing tar file(write /UnrealEngine_4.26/Engine/Source/ThirdParty/PhysX3/Lib/IOS/libPhysX3PROFILE.a: no space left on device): exit status 1
```
3/3/2023 10:51:39 AM: remove tmp link  
3/3/2023 11:16:58 AM: output from run.sh
```
Setup successful.
Error: error committing container for step {Env:[DEBIAN_FRONTEND=noninteractive PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin CUDA_VERSION=10.1.243 CUDA_PKG_VERSION=10-1=10.1.243-1 LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility NVIDIA_REQUIRE_CUDA=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411] Command:run Args:[./Setup.sh] Flags:[] Attrs:map[] Message:RUN ./Setup.sh Original:RUN ./Setup.sh }: error copying layers and metadata for container "c8c6b0975845fc80f30b7f5ded926ba89f4c8938380f99e2989e5341fde25c0c": writing blob: adding layer with blob "sha256:4aa569b5efa531d9dbb99859aa1ddcfed46cbd0f29812f7f74e2ecdd10de79a2": processing tar file(write /UnrealEngine_4.26/Engine/Source/ThirdParty/PhysX3/Lib/IOS/libPhysX3ExtensionsPROFILE.a: no space left on device): exit status 1
```
~3/3/2023 11:19:54 AM: follow https://www.ibm.com/docs/en/cloud-private/3.1.1?topic=pyci-specifying-default-docker-storage-directory-by-using-bind-mount to change storage location of containers~  
3/3/2023 11:29:32 AM: follow https://docs.oracle.com/en/operating-systems/oracle-linux/podman/podman-ConfiguringStorageforPodman.html#podman-install-storage to change storage location of containers.  
3/3/2023 12:14:22 PM: after removing files from storage, run.sh
```
Setup successful.
time="2023-03-03T12:13:45-05:00" level=error msg="Can't add file /home/nsambhu/.local/share/containers/storage/overlay/c9598829cda6a6b98d0fa1603328960bbf695f21c6321dd214baa265e8d13e0a/diff/UnrealEngine_4.26/Engine/Binaries/Mac/UnrealSync.app/Contents/MacOS/UnrealSync to tar: io: read/write on closed pipe"
time="2023-03-03T12:13:45-05:00" level=error msg="Can't close tar writer: io: read/write on closed pipe"
Error: error committing container for step {Env:[DEBIAN_FRONTEND=noninteractive PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin CUDA_VERSION=10.1.243 CUDA_PKG_VERSION=10-1=10.1.243-1 LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility NVIDIA_REQUIRE_CUDA=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411] Command:run Args:[./Setup.sh] Flags:[] Attrs:map[] Message:RUN ./Setup.sh Original:RUN ./Setup.sh }: error copying layers and metadata for container "731e7da7995e2a57c5bf4d1a4a393c1728c15a7adc01c00b6e3f6330d0c39fca": initializing source containers-storage:e73b055ee5f8-working-container-2: error storing layer "c9598829cda6a6b98d0fa1603328960bbf695f21c6321dd214baa265e8d13e0a" to file: write /var/tmp/buildah2469029510/layer: no space left on device
```
3/3/2023 12:19:03 PM: restart podman service
```
(base) [nsambhu@mhb-open-wired-237-156 4ubuntu-carla-source]$ service podman restart
Redirecting to /bin/systemctl restart podman.service
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ====
Authentication is required to restart 'podman.service'.
Authenticating as: Neil Sambhu (nsambhu)
Password: 
==== AUTHENTICATION COMPLETE ====
```
3/3/2023 12:25:47 PM: 
```
Setup successful.
time="2023-03-03T12:24:59-05:00" level=error msg="Can't add file /home/nsambhu/.local/share/containers/storage/overlay/aef7678d829148019e01bca9d22473d7df12f2a9dddad8f8b10f0d310262040f/diff/UnrealEngine_4.26/Engine/Binaries/Mac/UnrealSync.app/Contents/MacOS/UnrealSync to tar: io: read/write on closed pipe"
time="2023-03-03T12:24:59-05:00" level=error msg="Can't close tar writer: io: read/write on closed pipe"
Error: error committing container for step {Env:[DEBIAN_FRONTEND=noninteractive PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin CUDA_VERSION=10.1.243 CUDA_PKG_VERSION=10-1=10.1.243-1 LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility NVIDIA_REQUIRE_CUDA=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411] Command:run Args:[./Setup.sh] Flags:[] Attrs:map[] Message:RUN ./Setup.sh Original:RUN ./Setup.sh }: error copying layers and metadata for container "cc635f926d5242eb140420be1b15a40b46bfeb63a4a8acd65a3e32941d0ec014": initializing source containers-storage:e73b055ee5f8-working-container-2: error storing layer "aef7678d829148019e01bca9d22473d7df12f2a9dddad8f8b10f0d310262040f" to file: write /var/tmp/buildah3088000481/layer: no space left on device
```
3/4/2023 1:46:19 PM: 
```
Error: error committing container for step {Env:[DEBIAN_FRONTEND=noninteractive PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin CUDA_VERSION=10.1.243 CUDA_PKG_VERSION=10-1=10.1.243-1 LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility NVIDIA_REQUIRE_CUDA=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411] Command:run Args:[make] Flags:[] Attrs:map[] Message:RUN make Original:RUN make}: error copying layers and metadata for container "cb242e96b55398110d0291029a9912060f99737925c8264370b04912da213ed9": writing blob: adding layer with blob "sha256:d0b971d362a9002ae0ae073cc52e703e5566aebc3a8fdf61a88c81f820a54923": processing tar file(write /UnrealEngine_4.26/Engine/Intermediate/Build/Linux/B4D820EA/CrashReportClient/Shipping/CoreUObject/Module.CoreUObject.7_of_8.cpp.o: no space left on device): exit status 1
```
Docker build options https://docs.docker.com/engine/reference/commandline/build/ . TODO: find option to allow for enough disk space for container.  
3/4/2023 1:57:24 PM: in run.sh, try build with --compress flag.  
3/4/2023 2:18:25 PM:  
```
(base) [nsambhu@mhb-open-wired-237-156 containers]$ pwd
/home/nsambhu/.local/share/containers
(base) [nsambhu@mhb-open-wired-237-156 containers]$ ll
total 0
drwx------. 2 nsambhu nsambhu  39 Mar  3 09:31 cache
drwx------. 9 nsambhu nsambhu 169 Mar  3 09:31 storage
(base) [nsambhu@mhb-open-wired-237-156 containers]$ ls -dZ storage/
unconfined_u:object_r:data_home_t:s0 storage/
```
3/4/2023 4:29:56 PM:
```
STEP 32/32: RUN cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor
/bin/sh: 1: cd: can't cd to /root/UnrealEngine_4.26/Engine/Binaries/Linux
Error: error building at STEP "RUN cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor": error while running runtime: exit status 2
```
3/4/2023 7:11:57 PM:
```
STEP 32/33: RUN whoami
root
--> ab2597fafb1
STEP 33/33: RUN cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor
/bin/sh: 1: cd: can't cd to /root/UnrealEngine_4.26/Engine/Binaries/Linux
Error: error building at STEP "RUN cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor": error while running runtime: exit status 2
```
3/4/2023 9:17:27 PM: change ~ to $HOME; error persists  
3/4/2023 9:18:26 PM: debug in progress  
3/4/2023 9:23:45 PM: 
```
STEP 33/33: RUN ./UE4Editor
/bin/sh: 1: ./UE4Editor: not found
Error: error building at STEP "RUN ./UE4Editor": error while running runtime: exit status 127
```
3/4/2023 9:34:22 PM: 
```
STEP 34/35: RUN find /UnrealEngine_4.26 -name "UE4Editor"
/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor
```
3/4/2023 9:57:04 PM:
```
STEP 32/32: RUN ./Engine/Binaries/Linux/UE4Editor
Refusing to run with the root privileges.
Error: error building at STEP "RUN ./Engine/Binaries/Linux/UE4Editor": error while running runtime: exit status 1
```
3/5/2023 12:39:19 PM:
```
STEP 36/36: RUN ./Engine/Binaries/Linux/UE4Editor
sh: 1: xdg-user-dir: not found
- Existing per-process limit (soft=1024, hard=1024) is enough for us (need only 1024)
```
3/5/2023 1:57:46 PM: revert back from nsambhu to root account. Rebuild without using any previous data.  
```
STEP 32/32: RUN ./Engine/Binaries/Linux/UE4Editor
Refusing to run with the root privileges.
```
3/5/2023 3:58:16 PM: switch from root to nsambhu. Rebuild without using any previous data. 
```
STEP 36/36: RUN ./Engine/Binaries/Linux/UE4Editor
sh: 1: xdg-user-dir: not found
- Existing per-process limit (soft=1024, hard=1024) is enough for us (need only 1024)
Increasing per-process limit of core file size to infinity.
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogTaskGraph: Started task graph with 5 named threads and 74 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.101002
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: +0:00, Platform Override: ''
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_2.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_2.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_3.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_3.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_5.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_5.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_6.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_6.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_7.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_7.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_8.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_8.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_9.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_9.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_10.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_10.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_11.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_11.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_12.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_12.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_13.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_13.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_14.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_14.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_15.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_15.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_16.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_16.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_17.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_17.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_18.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_18.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_19.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_19.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_20.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_20.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_21.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_21.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_22.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_22.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_23.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_23.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_24.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_24.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_25.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_25.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_26.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_26.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_27.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_27.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_28.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_28.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_29.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_29.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_30.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_30.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_31.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Logs/UE4_31.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Config/CrashReportClient/UE4CC-Linux-9500BF510C2244E39266008C80564A35/CrashReportClient.ini') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine_4.26/Engine/Saved/Config/CrashReportClient/UE4CC-Linux-9500BF510C2244E39266008C80564A35/CrashReportClient.ini') failed: errno=13 (Permission denied)
LogPluginManager: Mounting plugin MeshPainting
LogPluginManager: Mounting plugin XGEController
LogPluginManager: Mounting plugin Paper2D
LogPluginManager: Mounting plugin AISupport
LogPluginManager: Mounting plugin EnvironmentQueryEditor
LogPluginManager: Mounting plugin CameraShakePreviewer
LogPluginManager: Mounting plugin LightPropagationVolume
LogPluginManager: Mounting plugin Niagara
LogPluginManager: Mounting plugin AssetManagerEditor
LogPluginManager: Mounting plugin CryptoKeys
LogPluginManager: Mounting plugin DataValidation
LogPluginManager: Mounting plugin CurveEditorTools
LogPluginManager: Mounting plugin GameplayTagsEditor
LogPluginManager: Mounting plugin MaterialAnalyzer
LogPluginManager: Mounting plugin GeometryMode
LogPluginManager: Mounting plugin MacGraphicsSwitching
LogPluginManager: Mounting plugin SpeedTreeImporter
LogPluginManager: Mounting plugin FacialAnimation
LogPluginManager: Mounting plugin MobileLauncherProfileWizard
LogPluginManager: Mounting plugin TcpMessaging
LogPluginManager: Mounting plugin UdpMessaging
LogPluginManager: Mounting plugin DatasmithContent
LogPluginManager: Mounting plugin PluginBrowser
LogPluginManager: Mounting plugin VariantManagerContent
LogPluginManager: Mounting plugin PlasticSourceControl
LogPluginManager: Mounting plugin CodeLiteSourceCodeAccess
LogPluginManager: Mounting plugin AnimationSharing
LogPluginManager: Mounting plugin CLionSourceCodeAccess
LogPluginManager: Mounting plugin KDevelopSourceCodeAccess
LogPluginManager: Mounting plugin PluginUtils
LogPluginManager: Mounting plugin PropertyAccessNode
LogPluginManager: Mounting plugin NullSourceCodeAccess
LogPluginManager: Mounting plugin RiderSourceCodeAccess
LogPluginManager: Mounting plugin GitSourceControl
LogPluginManager: Mounting plugin SubversionSourceControl
LogPluginManager: Mounting plugin UObjectPlugin
LogPluginManager: Mounting plugin LauncherChunkInstaller
LogPluginManager: Mounting plugin XCodeSourceCodeAccess
LogPluginManager: Mounting plugin VisualStudioSourceCodeAccess
LogPluginManager: Mounting plugin VisualStudioCodeSourceCodeAccess
LogPluginManager: Mounting plugin ScreenshotTools
LogPluginManager: Mounting plugin PerforceSourceControl
LogPluginManager: Mounting plugin LuminPlatformFeatures
LogPluginManager: Mounting plugin MLSDK
LogPluginManager: Mounting plugin MagicLeap
LogPluginManager: Mounting plugin MagicLeapMedia
LogPluginManager: Mounting plugin MagicLeapLightEstimation
LogPluginManager: Mounting plugin TemplateSequence
LogPluginManager: Mounting plugin MagicLeapPassableWorld
LogPluginManager: Mounting plugin ActorSequence
LogPluginManager: Mounting plugin MatineeToLevelSequence
LogPluginManager: Mounting plugin AutomationUtils
LogPluginManager: Mounting plugin AlembicImporter
LogPluginManager: Mounting plugin BackChannel
LogPluginManager: Mounting plugin ChaosCloth
LogPluginManager: Mounting plugin ChaosEditor
LogPluginManager: Mounting plugin ChaosNiagara
LogPluginManager: Mounting plugin ChaosClothEditor
LogPluginManager: Mounting plugin ChaosSolverPlugin
LogPluginManager: Mounting plugin CharacterAI
LogPluginManager: Mounting plugin GeometryCache
LogPluginManager: Mounting plugin GeometryCollectionPlugin
LogPluginManager: Mounting plugin GeometryProcessing
LogPluginManager: Mounting plugin LevelSequenceEditor
LogPluginManager: Mounting plugin PlanarCut
LogPluginManager: Mounting plugin PlatformCrypto
LogPluginManager: Mounting plugin SkeletalReduction
LogPluginManager: Mounting plugin OnlineSubsystem
LogPluginManager: Mounting plugin OnlineSubsystemUtils
LogPluginManager: Mounting plugin MotoSynth
LogPluginManager: Mounting plugin ProxyLODPlugin
LogPluginManager: Mounting plugin AndroidMedia
LogPluginManager: Mounting plugin AvfMedia
LogPluginManager: Mounting plugin OnlineSubsystemNull
LogPluginManager: Mounting plugin ImgMedia
LogPluginManager: Mounting plugin MediaCompositing
LogPluginManager: Mounting plugin MediaPlayerEditor
LogPluginManager: Mounting plugin WebMMedia
LogPluginManager: Mounting plugin WmfMedia
LogPluginManager: Mounting plugin AndroidMoviePlayer
LogPluginManager: Mounting plugin AndroidDeviceProfileSelector
LogPluginManager: Mounting plugin AndroidPermission
LogPluginManager: Mounting plugin AppleImageUtils
LogPluginManager: Mounting plugin AppleMoviePlayer
LogPluginManager: Mounting plugin ArchVisCharacter
LogPluginManager: Mounting plugin AudioCapture
LogPluginManager: Mounting plugin AssetTags
LogPluginManager: Mounting plugin AudioSynesthesia
LogPluginManager: Mounting plugin ChunkDownloader
LogPluginManager: Mounting plugin CustomMeshComponent
LogPluginManager: Mounting plugin CableComponent
LogPluginManager: Mounting plugin GoogleCloudMessaging
LogPluginManager: Mounting plugin EditableMesh
LogPluginManager: Mounting plugin ExampleDeviceProfileSelector
LogPluginManager: Mounting plugin GooglePAD
LogPluginManager: Mounting plugin LinuxDeviceProfileSelector
LogPluginManager: Mounting plugin IOSDeviceProfileSelector
LogPluginManager: Mounting plugin LocationServicesBPLibrary
LogPluginManager: Mounting plugin MobilePatchingUtils
LogPluginManager: Mounting plugin PostSplashScreen
LogPluginManager: Mounting plugin PropertyAccessEditor
LogPluginManager: Mounting plugin PhysXVehicles
LogPluginManager: Mounting plugin SignificanceManager
LogPluginManager: Mounting plugin RuntimePhysXCooking
LogPluginManager: Mounting plugin ProceduralMeshComponent
LogPluginManager: Mounting plugin SoundFields
LogPluginManager: Mounting plugin ActorLayerUtilities
LogPluginManager: Mounting plugin Synthesis
LogPluginManager: Mounting plugin WebMMoviePlayer
LogPluginManager: Mounting plugin WindowsMoviePlayer
LogPluginManager: Mounting plugin ContentBrowserAssetDataSource
LogPluginManager: Mounting plugin ContentBrowserClassDataSource
LogPluginManager: Mounting plugin OnlineSubsystemGooglePlay
LogPluginManager: Mounting plugin OnlineSubsystemIOS
LogPluginManager: Mounting plugin OculusVR
LogPluginManager: Mounting plugin SteamVR
LogInit: Using libcurl 7.65.3-DEV
LogInit:  - built for x86_64-unknown-linux-gnu
LogInit:  - supports SSL with OpenSSL/1.1.1c
LogInit:  - supports HTTP deflate (compression) using libz 1.2.8
LogInit:  - other features:
LogInit:      CURL_VERSION_SSL
LogInit:      CURL_VERSION_LIBZ
LogInit:      CURL_VERSION_IPV6
LogInit:      CURL_VERSION_ASYNCHDNS
LogInit:      CURL_VERSION_LARGEFILE
LogInit:      CURL_VERSION_TLSAUTH_SRP
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit:  - bVerifyPeer = true  - Libcurl will verify peer certificate
LogInit:  - bUseHttpProxy = false  - Libcurl will NOT use HTTP proxy
LogInit:  - bDontReuseConnections = false  - Libcurl will reuse connections
LogInit:  - MaxHostConnections = 16  - Libcurl will limit the number of connections to a host
LogInit:  - LocalHostAddr = Default
LogInit:  - BufferSize = 65536
LogOnline: OSS: Creating online subsystem instance for: NULL
LogOnline: OSS: TryLoadSubsystemAndSetDefault: Loaded subsystem for module [NULL]
LogInit: Build: ++UE4+Release-4.26-CL-0
LogInit: Engine Version: 4.26.2-0+++UE4+Release-4.26
LogInit: Compatible Engine Version: 4.26.0-0+++UE4+Release-4.26
LogInit: Net CL: 0
LogInit: OS: GenericOSVersionLabel (GenericOSSubVersionLabel), CPU: AMD Ryzen Threadripper 3960X 24-Core Processor , GPU: GenericGPUBrand
LogInit: Compiled (64-bit): Mar  5 2023 21:29:55
LogInit: Compiled with Clang: 10.0.1 
LogInit: Build Configuration: Development
LogInit: Branch Name: ++UE4+Release-4.26
LogInit: Command Line: 
LogInit: Base Directory: /UnrealEngine_4.26/Engine/Binaries/Linux/
LogInit: Allocator: binned2
LogInit: Installed Engine Build: 0
LogDevObjectVersion: Number of dev versions registered: 29
LogDevObjectVersion:   Dev-Blueprints (B0D832E4-1F89-4F0D-ACCF-7EB736FD4AA2): 10
LogDevObjectVersion:   Dev-Build (E1C64328-A22C-4D53-A36C-8E866417BD8C): 0
LogDevObjectVersion:   Dev-Core (375EC13C-06E4-48FB-B500-84F0262A717E): 4
LogDevObjectVersion:   Dev-Editor (E4B068ED-F494-42E9-A231-DA0B2E46BB41): 40
LogDevObjectVersion:   Dev-Framework (CFFC743F-43B0-4480-9391-14DF171D2073): 37
LogDevObjectVersion:   Dev-Mobile (B02B49B5-BB20-44E9-A304-32B752E40360): 3
LogDevObjectVersion:   Dev-Networking (A4E4105C-59A1-49B5-A7C5-40C4547EDFEE): 0
LogDevObjectVersion:   Dev-Online (39C831C9-5AE6-47DC-9A44-9C173E1C8E7C): 0
LogDevObjectVersion:   Dev-Physics (78F01B33-EBEA-4F98-B9B4-84EACCB95AA2): 4
LogDevObjectVersion:   Dev-Platform (6631380F-2D4D-43E0-8009-CF276956A95A): 0
LogDevObjectVersion:   Dev-Rendering (12F88B9F-8875-4AFC-A67C-D90C383ABD29): 44
LogDevObjectVersion:   Dev-Sequencer (7B5AE74C-D270-4C10-A958-57980B212A5A): 12
LogDevObjectVersion:   Dev-VR (D7296918-1DD6-4BDD-9DE2-64A83CC13884): 3
LogDevObjectVersion:   Dev-LoadTimes (C2A15278-BFE7-4AFE-6C17-90FF531DF755): 1
LogDevObjectVersion:   Private-Geometry (6EACA3D4-40EC-4CC1-B786-8BED09428FC5): 3
LogDevObjectVersion:   Dev-AnimPhys (29E575DD-E0A3-4627-9D10-D276232CDCEA): 17
LogDevObjectVersion:   Dev-Anim (AF43A65D-7FD3-4947-9873-3E8ED9C1BB05): 15
LogDevObjectVersion:   Dev-ReflectionCapture (6B266CEC-1EC7-4B8F-A30B-E4D90942FC07): 1
LogDevObjectVersion:   Dev-Automation (0DF73D61-A23F-47EA-B727-89E90C41499A): 1
LogDevObjectVersion:   FortniteMain (601D1886-AC64-4F84-AA16-D3DE0DEAC7D6): 43
LogDevObjectVersion:   FortniteRelease (E7086368-6B23-4C58-8439-1B7016265E91): 1
LogDevObjectVersion:   Dev-Enterprise (9DFFBCD6-494F-0158-E221-12823C92A888): 10
LogDevObjectVersion:   Dev-Niagara (F2AED0AC-9AFE-416F-8664-AA7FFA26D6FC): 1
LogDevObjectVersion:   Dev-Destruction (174F1F0B-B4C6-45A5-B13F-2EE8D0FB917D): 10
LogDevObjectVersion:   Dev-Physics-Ext (35F94A83-E258-406C-A318-09F59610247C): 40
LogDevObjectVersion:   Dev-PhysicsMaterial-Chaos (B68FC16E-8B1B-42E2-B453-215C058844FE): 1
LogDevObjectVersion:   Dev-CineCamera (B2E18506-4273-CFC2-A54E-F4BB758BBA07): 1
LogDevObjectVersion:   Dev-VirtualProduction (64F58936-FD1B-42BA-BA96-7289D5D0FA4E): 1
LogDevObjectVersion:   Dev-MediaFramework (6F0ED827-A609-4895-9C91-998D90180EA4): 2
LogInit: Presizing for max 25165824 objects, including 0 objects not considered by GC, pre-allocating 0 bytes for permanent pool.
LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
LogInit: Object subsystem initialized
LogConfig: Setting CVar [[con.DebugEarlyDefault:1]]
LogConfig: Setting CVar [[r.setres:1280x720]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[r.VSync:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[r.RHICmdBypass:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[r.GPUCrashDebugging:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererOverrideSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:615][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.GarbageCollectionSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.MaxObjectsNotConsideredByGC:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.SizeOfPermanentObjectPool:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.FlushStreamingOnGC:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.NumRetriesBeforeForcingGC:10]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.AllowParallelGC:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.TimeBetweenPurgingPendingKillObjects:61.1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.MaxObjectsInEditor:25165824]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.IncrementalBeginDestroyEnabled:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.CreateGCClusters:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.MinGCClusterSize:5]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.ActorClusteringEnabled:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.BlueprintClusteringEnabled:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.UseDisregardForGCOnDedicatedServers:0]]
[2023.03.05-21.56.26:615][  0]LogConfig: Setting CVar [[gc.MultithreadedDestructionEnabled:1]]
[2023.03.05-21.56.26:615][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.NetworkSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:615error: XDG_RUNTIME_DIR not set in the environment.
][  0]LogConfig: Applying CVar settings from Section [/Script/UnrealEd.CookerSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:615][  0]LogInit: Initializing SDL.
[2023.03.05-21.56.26:628][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2023.03.05-21.56.26:628][  0]LogInit: Warning: FDisplayMetrics::GetDisplayMetrics: InitSDL() failed, cannot get display metrics
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2023.03.05-21.56.26:628][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2023.03.05-21.56.26:628][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2023.03.05-21.56.26:628][  0]LogLinux: Selected Device Profile: [Linux]
[2023.03.05-21.56.26:628][  0]LogInit: Applying CVar settings loaded from the selected device profile: [Linux]
[2023.03.05-21.56.26:628][  0]LogHAL: Display: Platform has ~ 4 GB [67166060544 / 4294967296 / 63], which maps to Smallest [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
[2023.03.05-21.56.26:628][  0]LogInit: Going up to parent DeviceProfile []
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [Startup] File [../../../Engine/Config/ConsoleVariables.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[net.UseAdaptiveNetUpdateFrequency:0]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[p.chaos.AllowCreatePhysxBodies:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[fx.SkipVectorVMBackendOptimizations:1]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.05-21.56.26:629][  0]LogConfig: Setting CVar [[g.TimeoutForBlockOnRenderFence:60000]]
[2023.03.05-21.56.26:629][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Editor.ini]
[2023.03.05-21.56.26:629][  0]LogInit: Unix hardware info:
[2023.03.05-21.56.26:629][  0]LogInit:  - we are the first instance of this executable
[2023.03.05-21.56.26:629][  0]LogInit:  - this process' id (pid) is 7, parent process' id (ppid) is 1
[2023.03.05-21.56.26:629][  0]LogInit:  - we are not running under debugger
[2023.03.05-21.56.26:629][  0]LogInit:  - machine network name is 'a6c9091c6f8d'
[2023.03.05-21.56.26:629][  0]LogInit:  - user name is 'nsambhu' (nsambhu)
[2023.03.05-21.56.26:629][  0]LogInit:  - we're logged in locally
[2023.03.05-21.56.26:629][  0]LogInit:  - we're running with rendering
[2023.03.05-21.56.26:629][  0]LogInit:  - CPU: AuthenticAMD 'AMD Ryzen Threadripper 3960X 24-Core Processor ' (signature: 0x830F10)
[2023.03.05-21.56.26:629][  0]LogInit:  - Number of physical cores available for the process: 24
[2023.03.05-21.56.26:629][  0]LogInit:  - Number of logical cores available for the process: 48
[2023.03.05-21.56.26:629][  0]LogInit:  - Cache line size: 64
[2023.03.05-21.56.26:629][  0]LogInit:  - Memory allocator used: binned2
[2023.03.05-21.56.26:629][  0]LogInit:  - This binary is optimized with LTO: no, PGO: no, instrumented for PGO data collection: no
[2023.03.05-21.56.26:629][  0]LogInit:  - This is an internal build.
[2023.03.05-21.56.26:629][  0]LogCore: Benchmarking clocks:
[2023.03.05-21.56.26:629][  0]LogCore:  - CLOCK_MONOTONIC (id=1) can sustain 49864499 (49864K, 50M) calls per second without zero deltas.
[2023.03.05-21.56.26:629][  0]LogCore:  - CLOCK_MONOTONIC_RAW (id=4) can sustain 49961584 (49962K, 50M) calls per second without zero deltas.
[2023.03.05-21.56.26:629][  0]LogCore:  - CLOCK_MONOTONIC_COARSE (id=6) can sustain 226062940 (226063K, 226M) calls per second with 99.999553% zero deltas.
[2023.03.05-21.56.26:629][  0]LogCore: Selected clock_id 4 (CLOCK_MONOTONIC_RAW) since it is the fastest support clock without zero deltas.
[2023.03.05-21.56.26:629][  0]LogInit: Unix-specific commandline switches:
[2023.03.05-21.56.26:629][  0]LogInit:  -ansimalloc - use malloc()/free() from libc (useful for tools like valgrind and electric fence)
[2023.03.05-21.56.26:629][  0]LogInit:  -jemalloc - use jemalloc for all memory allocation
[2023.03.05-21.56.26:629][  0]LogInit:  -binnedmalloc - use binned malloc  for all memory allocation
[2023.03.05-21.56.26:629][  0]LogInit:  -filemapcachesize=NUMBER - set the size for case-sensitive file mapping cache
[2023.03.05-21.56.26:629][  0]LogInit:  -useksm - uses kernel same-page mapping (KSM) for mapped memory (OFF)
[2023.03.05-21.56.26:629][  0]LogInit:  -ksmmergeall - marks all mmap'd memory pages suitable for KSM (OFF)
[2023.03.05-21.56.26:629][  0]LogInit:  -preloadmodulesymbols - Loads the main module symbols file into memory (OFF)
[2023.03.05-21.56.26:629][  0]LogInit:  -sigdfl=SIGNAL - Allows a specific signal to be set to its default handler rather then ignoring the signal
[2023.03.05-21.56.26:629][  0]LogInit:  -httpproxy=ADDRESS:PORT - redirects HTTP requests to a proxy (only supported if compiled with libcurl)
[2023.03.05-21.56.26:629][error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
Error: error building at STEP "RUN ./Engine/Binaries/Linux/UE4Editor": error while running runtime: exit status 1
d7e0a1f12a4b27378b2c427d27550236b5ed9b1f6cf0f33f6ca17f2d830fe2fc
```
3/6/2023 12:20:20 PM: Rebuild without using previous data. Check files and file permissions of /UnrealEngine_4.26/Engine/Binaries/Linux/. Next TODO: modify Dockerfile: create nsambhu account before copying the UnrealEngine_4.26 folder.  
```
STEP 32/33: RUN ls -lh /UnrealEngine_4.26/Engine/Binaries/Linux/
total 9.1G
-rw-r--r--. 1 root root   12K Mar  6 17:32 AgentInterface.dll
drwxr-xr-x. 2 root root  4.0K Mar  6 17:47 Android
-rwxr-xr-x. 1 root root 1002K Mar  6 17:08 BreakpadSymbolEncoder
-rwxr-xr-x. 1 root root   61K Mar  6 17:08 BreakpadSymbolEncoder.exe
-rwxr-xr-x. 1 root root   27M Mar  6 17:31 CrashReportClient
-rw-r--r--. 1 root root   31K Mar  6 17:31 CrashReportClient-Linux-Shipping.target
-rw-r--r--. 1 root root  252M Mar  6 17:31 CrashReportClient.debug
-rw-r--r--. 1 root root   14M Mar  6 17:31 CrashReportClient.sym
-rwxr-xr-x. 1 root root   27M Mar  6 17:32 CrashReportClientEditor
-rw-r--r--. 1 root root   31K Mar  6 17:32 CrashReportClientEditor-Linux-Shipping.target
-rw-r--r--. 1 root root  252M Mar  6 17:32 CrashReportClientEditor.debug
-rw-r--r--. 1 root root   14M Mar  6 17:32 CrashReportClientEditor.sym
drwxr-xr-x. 2 root root  4.0K Mar  6 17:47 Linux
-rwxr-xr-x. 1 root root  197K Mar  6 17:32 ShaderCompileWorker
-rw-r--r--. 1 root root  3.2M Mar  6 17:32 ShaderCompileWorker.debug
-rw-r--r--. 1 root root  1.8K Mar  6 17:32 ShaderCompileWorker.modules
-rw-r--r--. 1 root root  158K Mar  6 17:32 ShaderCompileWorker.sym
-rw-r--r--. 1 root root   41K Mar  6 17:32 ShaderCompileWorker.target
-rw-r--r--. 1 root root   253 Mar  6 17:32 ShaderCompileWorker.version
-rwxr-xr-x. 1 root root  495K Mar  6 17:46 UE4Editor
-rwxr-xr-x. 1 root root  495K Mar  6 17:46 UE4Editor-Cmd
-rw-r--r--. 1 root root  6.4M Mar  6 17:46 UE4Editor-Cmd.debug
-rw-r--r--. 1 root root  268K Mar  6 17:46 UE4Editor-Cmd.sym
-rw-r--r--. 1 root root  6.4M Mar  6 17:46 UE4Editor.debug
-rw-r--r--. 1 root root   21K Mar  6 17:47 UE4Editor.modules
-rw-r--r--. 1 root root  268K Mar  6 17:46 UE4Editor.sym
-rw-r--r--. 1 root root  746K Mar  6 17:47 UE4Editor.target
-rw-r--r--. 1 root root   253 Mar  6 17:47 UE4Editor.version
-rwxr-xr-x. 1 root root   46M Mar  6 17:11 UnrealCEFSubProcess
-rwxr-xr-x. 1 root root  151K Mar  6 17:34 UnrealFrontend
-rw-r--r--. 1 root root  2.5M Mar  6 17:34 UnrealFrontend.debug
-rw-r--r--. 1 root root  4.3K Mar  6 17:34 UnrealFrontend.modules
-rw-r--r--. 1 root root  101K Mar  6 17:34 UnrealFrontend.sym
-rw-r--r--. 1 root root   62K Mar  6 17:34 UnrealFrontend.target
-rw-r--r--. 1 root root   253 Mar  6 17:34 UnrealFrontend.version
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:30 UnrealHeaderTool
-rw-r--r--. 1 root root   17M Mar  6 17:30 UnrealHeaderTool.debug
-rw-r--r--. 1 root root   367 Mar  6 17:30 UnrealHeaderTool.modules
-rw-r--r--. 1 root root  1.2M Mar  6 17:30 UnrealHeaderTool.sym
-rw-r--r--. 1 root root  3.1K Mar  6 17:30 UnrealHeaderTool.target
-rw-r--r--. 1 root root   253 Mar  6 17:30 UnrealHeaderTool.version
-rwxr-xr-x. 1 root root  111K Mar  6 17:49 UnrealInsights
-rw-r--r--. 1 root root  2.0M Mar  6 17:49 UnrealInsights.debug
-rw-r--r--. 1 root root  2.7K Mar  6 17:49 UnrealInsights.modules
-rw-r--r--. 1 root root   69K Mar  6 17:49 UnrealInsights.sym
-rw-r--r--. 1 root root   50K Mar  6 17:49 UnrealInsights.target
-rw-r--r--. 1 root root   253 Mar  6 17:49 UnrealInsights.version
-rwxr-xr-x. 1 root root  968K Mar  6 17:33 UnrealLightmass
-rw-r--r--. 1 root root   14M Mar  6 17:33 UnrealLightmass.debug
-rw-r--r--. 1 root root   779 Mar  6 17:33 UnrealLightmass.modules
-rw-r--r--. 1 root root  872K Mar  6 17:33 UnrealLightmass.sym
-rw-r--r--. 1 root root  6.5K Mar  6 17:33 UnrealLightmass.target
-rw-r--r--. 1 root root   253 Mar  6 17:33 UnrealLightmass.version
-rwxr-xr-x. 1 root root   15M Mar  6 17:10 UnrealVersionSelector-Linux-Shipping
-rw-r--r--. 1 root root  136M Mar  6 17:08 UnrealVersionSelector-Linux-Shipping.debug
-rw-r--r--. 1 root root  9.2M Mar  6 17:07 UnrealVersionSelector-Linux-Shipping.sym
-rw-r--r--. 1 root root   27K Mar  6 17:11 UnrealVersionSelector-Linux-Shipping.target
-rwxr-xr-x. 1 root root  5.5M Mar  6 17:08 dump_syms
-rwxr-xr-x. 1 root root  366K Mar  6 17:07 dump_syms.exe
-rw-r--r--. 1 root root  9.1M Mar  6 17:32 libShaderCompileWorker-ApplicationCore.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:32 libShaderCompileWorker-ApplicationCore.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:32 libShaderCompileWorker-ApplicationCore.sym
-rw-r--r--. 1 root root  734K Mar  6 17:32 libShaderCompileWorker-AudioPlatformConfiguration.debug
-rwxr-xr-x. 1 root root   25K Mar  6 17:32 libShaderCompileWorker-AudioPlatformConfiguration.so
-rw-r--r--. 1 root root   17K Mar  6 17:32 libShaderCompileWorker-AudioPlatformConfiguration.sym
-rw-r--r--. 1 root root   17K Mar  6 17:32 libShaderCompileWorker-BuildSettings.debug
-rwxr-xr-x. 1 root root  5.0K Mar  6 17:32 libShaderCompileWorker-BuildSettings.so
-rw-r--r--. 1 root root   868 Mar  6 17:32 libShaderCompileWorker-BuildSettings.sym
-rw-r--r--. 1 root root   87M Mar  6 17:32 libShaderCompileWorker-Core.debug
-rwxr-xr-x. 1 root root  8.5M Mar  6 17:32 libShaderCompileWorker-Core.so
-rw-r--r--. 1 root root  5.7M Mar  6 17:32 libShaderCompileWorker-Core.sym
-rw-r--r--. 1 root root   65M Mar  6 17:32 libShaderCompileWorker-CoreUObject.debug
-rwxr-xr-x. 1 root root  5.9M Mar  6 17:32 libShaderCompileWorker-CoreUObject.so
-rw-r--r--. 1 root root  4.2M Mar  6 17:32 libShaderCompileWorker-CoreUObject.sym
-rw-r--r--. 1 root root   11M Mar  6 17:32 libShaderCompileWorker-DesktopPlatform.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:32 libShaderCompileWorker-DesktopPlatform.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:32 libShaderCompileWorker-DesktopPlatform.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:32 libShaderCompileWorker-DirectoryWatcher.debug
-rwxr-xr-x. 1 root root  286K Mar  6 17:32 libShaderCompileWorker-DirectoryWatcher.so
-rw-r--r--. 1 root root  238K Mar  6 17:32 libShaderCompileWorker-DirectoryWatcher.sym
-rw-r--r--. 1 root root  4.4M Mar  6 17:32 libShaderCompileWorker-EditorStyle.debug
-rwxr-xr-x. 1 root root  694K Mar  6 17:32 libShaderCompileWorker-EditorStyle.so
-rw-r--r--. 1 root root  194K Mar  6 17:32 libShaderCompileWorker-EditorStyle.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:32 libShaderCompileWorker-ImageWrapper.debug
-rwxr-xr-x. 1 root root  4.2M Mar  6 17:32 libShaderCompileWorker-ImageWrapper.so
-rw-r--r--. 1 root root  571K Mar  6 17:32 libShaderCompileWorker-ImageWrapper.sym
-rw-r--r--. 1 root root  2.4M Mar  6 17:32 libShaderCompileWorker-InputCore.debug
-rwxr-xr-x. 1 root root  329K Mar  6 17:32 libShaderCompileWorker-InputCore.so
-rw-r--r--. 1 root root  107K Mar  6 17:32 libShaderCompileWorker-InputCore.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:32 libShaderCompileWorker-Json.debug
-rwxr-xr-x. 1 root root  190K Mar  6 17:32 libShaderCompileWorker-Json.so
-rw-r--r--. 1 root root  124K Mar  6 17:32 libShaderCompileWorker-Json.sym
-rw-r--r--. 1 root root  282K Mar  6 17:32 libShaderCompileWorker-LauncherPlatform.debug
-rwxr-xr-x. 1 root root   11K Mar  6 17:32 libShaderCompileWorker-LauncherPlatform.so
-rw-r--r--. 1 root root  3.4K Mar  6 17:32 libShaderCompileWorker-LauncherPlatform.sym
-rw-r--r--. 1 root root  4.4M Mar  6 17:32 libShaderCompileWorker-Projects.debug
-rwxr-xr-x. 1 root root  341K Mar  6 17:32 libShaderCompileWorker-Projects.so
-rw-r--r--. 1 root root  237K Mar  6 17:32 libShaderCompileWorker-Projects.sym
-rw-r--r--. 1 root root   11M Mar  6 17:32 libShaderCompileWorker-RHI.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:32 libShaderCompileWorker-RHI.so
-rw-r--r--. 1 root root  786K Mar  6 17:32 libShaderCompileWorker-RHI.sym
-rw-r--r--. 1 root root   24M Mar  6 17:32 libShaderCompileWorker-RenderCore.debug
-rwxr-xr-x. 1 root root  2.3M Mar  6 17:32 libShaderCompileWorker-RenderCore.so
-rw-r--r--. 1 root root  1.8M Mar  6 17:32 libShaderCompileWorker-RenderCore.sym
-rw-r--r--. 1 root root  865K Mar  6 17:32 libShaderCompileWorker-SandboxFile.debug
-rwxr-xr-x. 1 root root   63K Mar  6 17:32 libShaderCompileWorker-SandboxFile.so
-rw-r--r--. 1 root root   36K Mar  6 17:32 libShaderCompileWorker-SandboxFile.sym
-rw-r--r--. 1 root root  5.0M Mar  6 17:32 libShaderCompileWorker-ShaderCompilerCommon.debug
-rwxr-xr-x. 1 root root  433K Mar  6 17:32 libShaderCompileWorker-ShaderCompilerCommon.so
-rw-r--r--. 1 root root  341K Mar  6 17:32 libShaderCompileWorker-ShaderCompilerCommon.sym
-rw-r--r--. 1 root root   16M Mar  6 17:32 libShaderCompileWorker-ShaderFormatOpenGL.debug
-rwxr-xr-x. 1 root root  3.2M Mar  6 17:32 libShaderCompileWorker-ShaderFormatOpenGL.so
-rw-r--r--. 1 root root  2.2M Mar  6 17:32 libShaderCompileWorker-ShaderFormatOpenGL.sym
-rw-r--r--. 1 root root  9.8M Mar  6 17:32 libShaderCompileWorker-ShaderFormatVectorVM.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:32 libShaderCompileWorker-ShaderFormatVectorVM.so
-rw-r--r--. 1 root root  1.1M Mar  6 17:32 libShaderCompileWorker-ShaderFormatVectorVM.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:32 libShaderCompileWorker-ShaderPreprocessor.debug
-rwxr-xr-x. 1 root root  191K Mar  6 17:32 libShaderCompileWorker-ShaderPreprocessor.so
-rw-r--r--. 1 root root   50K Mar  6 17:32 libShaderCompileWorker-ShaderPreprocessor.sym
-rw-r--r--. 1 root root   58M Mar  6 17:32 libShaderCompileWorker-Slate.debug
-rwxr-xr-x. 1 root root  5.3M Mar  6 17:32 libShaderCompileWorker-Slate.so
-rw-r--r--. 1 root root  3.3M Mar  6 17:32 libShaderCompileWorker-Slate.sym
-rw-r--r--. 1 root root   23M Mar  6 17:32 libShaderCompileWorker-SlateCore.debug
-rwxr-xr-x. 1 root root  3.2M Mar  6 17:32 libShaderCompileWorker-SlateCore.so
-rw-r--r--. 1 root root  1.7M Mar  6 17:32 libShaderCompileWorker-SlateCore.sym
-rw-r--r--. 1 root root  6.5M Mar  6 17:32 libShaderCompileWorker-SlateFileDialogs.debug
-rwxr-xr-x. 1 root root  579K Mar  6 17:32 libShaderCompileWorker-SlateFileDialogs.so
-rw-r--r--. 1 root root  359K Mar  6 17:32 libShaderCompileWorker-SlateFileDialogs.sym
-rw-r--r--. 1 root root  3.1M Mar  6 17:32 libShaderCompileWorker-TargetPlatform.debug
-rwxr-xr-x. 1 root root  189K Mar  6 17:32 libShaderCompileWorker-TargetPlatform.so
-rw-r--r--. 1 root root  123K Mar  6 17:32 libShaderCompileWorker-TargetPlatform.sym
-rw-r--r--. 1 root root  407K Mar  6 17:32 libShaderCompileWorker-TraceLog.debug
-rwxr-xr-x. 1 root root   85K Mar  6 17:32 libShaderCompileWorker-TraceLog.so
-rw-r--r--. 1 root root   12K Mar  6 17:32 libShaderCompileWorker-TraceLog.sym
-rw-r--r--. 1 root root  346K Mar  6 17:32 libShaderCompileWorker-UELibSampleRate.debug
-rwxr-xr-x. 1 root root  1.5M Mar  6 17:32 libShaderCompileWorker-UELibSampleRate.so
-rw-r--r--. 1 root root   28K Mar  6 17:32 libShaderCompileWorker-UELibSampleRate.sym
-rw-r--r--. 1 root root  5.3M Mar  6 17:32 libShaderCompileWorker-VectorVM.debug
-rwxr-xr-x. 1 root root  465K Mar  6 17:32 libShaderCompileWorker-VectorVM.so
-rw-r--r--. 1 root root  446K Mar  6 17:32 libShaderCompileWorker-VectorVM.sym
-rw-r--r--. 1 root root   13M Mar  6 17:32 libShaderCompileWorker-VulkanShaderFormat.debug
-rwxr-xr-x. 1 root root  6.3M Mar  6 17:32 libShaderCompileWorker-VulkanShaderFormat.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:32 libShaderCompileWorker-VulkanShaderFormat.sym
-rw-r--r--. 1 root root  5.9M Mar  6 17:42 libUE4Editor-AIGraph.debug
-rwxr-xr-x. 1 root root  478K Mar  6 17:42 libUE4Editor-AIGraph.so
-rw-r--r--. 1 root root  293K Mar  6 17:42 libUE4Editor-AIGraph.sym
-rw-r--r--. 1 root root   38M Mar  6 17:40 libUE4Editor-AIModule.debug
-rwxr-xr-x. 1 root root  5.0M Mar  6 17:40 libUE4Editor-AIModule.so
-rw-r--r--. 1 root root  2.7M Mar  6 17:40 libUE4Editor-AIModule.sym
-rw-r--r--. 1 root root  5.1M Mar  6 17:46 libUE4Editor-AITestSuite.debug
-rwxr-xr-x. 1 root root  775K Mar  6 17:39 libUE4Editor-AITestSuite.so
-rw-r--r--. 1 root root  291K Mar  6 17:46 libUE4Editor-AITestSuite.sym
-rw-r--r--. 1 root root  1.8M Mar  6 17:46 libUE4Editor-AVEncoder.debug
-rwxr-xr-x. 1 root root  300K Mar  6 17:46 libUE4Editor-AVEncoder.so
-rw-r--r--. 1 root root  109K Mar  6 17:46 libUE4Editor-AVEncoder.sym
-rw-r--r--. 1 root root  945K Mar  6 17:39 libUE4Editor-AVIWriter.debug
-rwxr-xr-x. 1 root root  283K Mar  6 17:39 libUE4Editor-AVIWriter.so
-rw-r--r--. 1 root root   81K Mar  6 17:39 libUE4Editor-AVIWriter.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:39 libUE4Editor-ActorPickerMode.debug
-rwxr-xr-x. 1 root root   79K Mar  6 17:39 libUE4Editor-ActorPickerMode.so
-rw-r--r--. 1 root root   47K Mar  6 17:39 libUE4Editor-ActorPickerMode.sym
-rw-r--r--. 1 root root   12M Mar  6 17:38 libUE4Editor-AddContentDialog.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:38 libUE4Editor-AddContentDialog.so
-rw-r--r--. 1 root root  685K Mar  6 17:38 libUE4Editor-AddContentDialog.sym
-rw-r--r--. 1 root root  3.5M Mar  6 17:39 libUE4Editor-AdvancedPreviewScene.debug
-rwxr-xr-x. 1 root root  283K Mar  6 17:39 libUE4Editor-AdvancedPreviewScene.so
-rw-r--r--. 1 root root  152K Mar  6 17:39 libUE4Editor-AdvancedPreviewScene.sym
-rw-r--r--. 1 root root  375K Mar  6 17:46 libUE4Editor-Advertising.debug
-rwxr-xr-x. 1 root root  238K Mar  6 17:46 libUE4Editor-Advertising.so
-rw-r--r--. 1 root root   51K Mar  6 17:46 libUE4Editor-Advertising.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:46 libUE4Editor-AllDesktopTargetPlatform.debug
-rwxr-xr-x. 1 root root   29K Mar  6 17:46 libUE4Editor-AllDesktopTargetPlatform.so
-rw-r--r--. 1 root root   18K Mar  6 17:46 libUE4Editor-AllDesktopTargetPlatform.sym
-rw-r--r--. 1 root root  449K Mar  6 17:35 libUE4Editor-Analytics.debug
-rwxr-xr-x. 1 root root  248K Mar  6 17:35 libUE4Editor-Analytics.so
-rw-r--r--. 1 root root   59K Mar  6 17:35 libUE4Editor-Analytics.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:35 libUE4Editor-AnalyticsET.debug
-rwxr-xr-x. 1 root root  176K Mar  6 17:35 libUE4Editor-AnalyticsET.so
-rw-r--r--. 1 root root  131K Mar  6 17:35 libUE4Editor-AnalyticsET.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:46 libUE4Editor-AnalyticsSwrve.debug
-rwxr-xr-x. 1 root root  136K Mar  6 17:46 libUE4Editor-AnalyticsSwrve.so
-rw-r--r--. 1 root root   87K Mar  6 17:46 libUE4Editor-AnalyticsSwrve.sym
-rw-r--r--. 1 root root  1.4M Mar  6 17:41 libUE4Editor-AnalyticsVisualEditing.debug
-rwxr-xr-x. 1 root root   52K Mar  6 17:41 libUE4Editor-AnalyticsVisualEditing.so
-rw-r--r--. 1 root root   18K Mar  6 17:41 libUE4Editor-AnalyticsVisualEditing.sym
-rw-r--r--. 1 root root   47M Mar  6 17:40 libUE4Editor-AnimGraph.debug
-rwxr-xr-x. 1 root root  4.8M Mar  6 17:40 libUE4Editor-AnimGraph.so
-rw-r--r--. 1 root root  2.7M Mar  6 17:40 libUE4Editor-AnimGraph.sym
-rw-r--r--. 1 root root   26M Mar  6 17:39 libUE4Editor-AnimGraphRuntime.debug
-rwxr-xr-x. 1 root root  2.4M Mar  6 17:39 libUE4Editor-AnimGraphRuntime.so
-rw-r--r--. 1 root root  1.6M Mar  6 17:39 libUE4Editor-AnimGraphRuntime.sym
-rw-r--r--. 1 root root   11M Mar  6 17:42 libUE4Editor-AnimationBlueprintEditor.debug
-rwxr-xr-x. 1 root root  925K Mar  6 17:42 libUE4Editor-AnimationBlueprintEditor.so
-rw-r--r--. 1 root root  566K Mar  6 17:42 libUE4Editor-AnimationBlueprintEditor.sym
-rw-r--r--. 1 root root  3.0M Mar  6 17:39 libUE4Editor-AnimationCore.debug
-rwxr-xr-x. 1 root root  485K Mar  6 17:39 libUE4Editor-AnimationCore.so
-rw-r--r--. 1 root root  287K Mar  6 17:39 libUE4Editor-AnimationCore.sym
-rw-r--r--. 1 root root  4.6M Mar  6 17:41 libUE4Editor-AnimationEditor.debug
-rwxr-xr-x. 1 root root  340K Mar  6 17:41 libUE4Editor-AnimationEditor.so
-rw-r--r--. 1 root root  202K Mar  6 17:41 libUE4Editor-AnimationEditor.sym
-rw-r--r--. 1 root root   11M Mar  6 17:41 libUE4Editor-AnimationModifiers.debug
-rwxr-xr-x. 1 root root 1008K Mar  6 17:41 libUE4Editor-AnimationModifiers.so
-rw-r--r--. 1 root root  636K Mar  6 17:41 libUE4Editor-AnimationModifiers.sym
-rw-r--r--. 1 root root   41M Mar  6 17:38 libUE4Editor-AppFramework.debug
-rwxr-xr-x. 1 root root  5.0M Mar  6 17:38 libUE4Editor-AppFramework.so
-rw-r--r--. 1 root root  3.2M Mar  6 17:38 libUE4Editor-AppFramework.sym
-rw-r--r--. 1 root root  9.7M Mar  6 17:35 libUE4Editor-ApplicationCore.debug
-rwxr-xr-x. 1 root root  3.0M Mar  6 17:35 libUE4Editor-ApplicationCore.so
-rw-r--r--. 1 root root  1.6M Mar  6 17:35 libUE4Editor-ApplicationCore.sym
-rw-r--r--. 1 root root   13M Mar  6 17:36 libUE4Editor-AssetRegistry.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:36 libUE4Editor-AssetRegistry.so
-rw-r--r--. 1 root root  899K Mar  6 17:36 libUE4Editor-AssetRegistry.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:38 libUE4Editor-AssetTagsEditor.debug
-rwxr-xr-x. 1 root root  161K Mar  6 17:38 libUE4Editor-AssetTagsEditor.so
-rw-r--r--. 1 root root   71K Mar  6 17:38 libUE4Editor-AssetTagsEditor.sym
-rw-r--r--. 1 root root   36M Mar  6 17:40 libUE4Editor-AssetTools.debug
-rwxr-xr-x. 1 root root  3.6M Mar  6 17:40 libUE4Editor-AssetTools.so
-rw-r--r--. 1 root root  2.6M Mar  6 17:40 libUE4Editor-AssetTools.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:42 libUE4Editor-AudioAnalyzer.debug
-rwxr-xr-x. 1 root root  102K Mar  6 17:42 libUE4Editor-AudioAnalyzer.so
-rw-r--r--. 1 root root   56K Mar  6 17:42 libUE4Editor-AudioAnalyzer.sym
-rw-r--r--. 1 root root  414K Mar  6 17:42 libUE4Editor-AudioCaptureCore.debug
-rwxr-xr-x. 1 root root   28K Mar  6 17:42 libUE4Editor-AudioCaptureCore.so
-rw-r--r--. 1 root root   15K Mar  6 17:42 libUE4Editor-AudioCaptureCore.sym
-rw-r--r--. 1 root root  358K Mar  6 17:46 libUE4Editor-AudioCaptureRtAudio.debug
-rwxr-xr-x. 1 root root  237K Mar  6 17:46 libUE4Editor-AudioCaptureRtAudio.so
-rw-r--r--. 1 root root   52K Mar  6 17:46 libUE4Editor-AudioCaptureRtAudio.sym
-rw-r--r--. 1 root root   20M Mar  6 17:46 libUE4Editor-AudioEditor.debug
-rwxr-xr-x. 1 root root  2.2M Mar  6 17:41 libUE4Editor-AudioEditor.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:46 libUE4Editor-AudioEditor.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:37 libUE4Editor-AudioExtensions.debug
-rwxr-xr-x. 1 root root  142K Mar  6 17:37 libUE4Editor-AudioExtensions.so
-rw-r--r--. 1 root root   60K Mar  6 17:37 libUE4Editor-AudioExtensions.sym
-rw-r--r--. 1 root root  763K Mar  6 17:46 libUE4Editor-AudioFormatADPCM.debug
-rwxr-xr-x. 1 root root  258K Mar  6 17:46 libUE4Editor-AudioFormatADPCM.so
-rw-r--r--. 1 root root   71K Mar  6 17:46 libUE4Editor-AudioFormatADPCM.sym
-rw-r--r--. 1 root root  866K Mar  6 17:46 libUE4Editor-AudioFormatOgg.debug
-rwxr-xr-x. 1 root root  3.3M Mar  6 17:46 libUE4Editor-AudioFormatOgg.so
-rw-r--r--. 1 root root   76K Mar  6 17:46 libUE4Editor-AudioFormatOgg.sym
-rw-r--r--. 1 root root  831K Mar  6 17:46 libUE4Editor-AudioFormatOpus.debug
-rwxr-xr-x. 1 root root  670K Mar  6 17:46 libUE4Editor-AudioFormatOpus.so
-rw-r--r--. 1 root root   92K Mar  6 17:46 libUE4Editor-AudioFormatOpus.sym
-rw-r--r--. 1 root root   15M Mar  6 17:46 libUE4Editor-AudioMixer.debug
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:37 libUE4Editor-AudioMixer.so
-rw-r--r--. 1 root root 1006K Mar  6 17:46 libUE4Editor-AudioMixer.sym
-rw-r--r--. 1 root root  759K Mar  6 17:35 libUE4Editor-AudioMixerCore.debug
-rwxr-xr-x. 1 root root  284K Mar  6 17:35 libUE4Editor-AudioMixerCore.so
-rw-r--r--. 1 root root   80K Mar  6 17:35 libUE4Editor-AudioMixerCore.sym
-rw-r--r--. 1 root root  7.6M Mar  6 17:46 libUE4Editor-AudioMixerSDL.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:46 libUE4Editor-AudioMixerSDL.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:46 libUE4Editor-AudioMixerSDL.sym
-rw-r--r--. 1 root root  746K Mar  6 17:35 libUE4Editor-AudioPlatformConfiguration.debug
-rwxr-xr-x. 1 root root   31K Mar  6 17:35 libUE4Editor-AudioPlatformConfiguration.so
-rw-r--r--. 1 root root   18K Mar  6 17:35 libUE4Editor-AudioPlatformConfiguration.sym
-rw-r--r--. 1 root root  4.2M Mar  6 17:42 libUE4Editor-AudioSettingsEditor.debug
-rwxr-xr-x. 1 root root  363K Mar  6 17:42 libUE4Editor-AudioSettingsEditor.so
-rw-r--r--. 1 root root  239K Mar  6 17:42 libUE4Editor-AudioSettingsEditor.sym
-rw-r--r--. 1 root root   11M Mar  6 17:39 libUE4Editor-AugmentedReality.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:39 libUE4Editor-AugmentedReality.so
-rw-r--r--. 1 root root  706K Mar  6 17:39 libUE4Editor-AugmentedReality.sym
-rw-r--r--. 1 root root  5.3M Mar  6 17:40 libUE4Editor-AutomationController.debug
-rwxr-xr-x. 1 root root  447K Mar  6 17:40 libUE4Editor-AutomationController.so
-rw-r--r--. 1 root root  348K Mar  6 17:40 libUE4Editor-AutomationController.sym
-rw-r--r--. 1 root root   19M Mar  6 17:46 libUE4Editor-AutomationDriver.debug
-rwxr-xr-x. 1 root root  2.0M Mar  6 17:46 libUE4Editor-AutomationDriver.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:46 libUE4Editor-AutomationDriver.sym
-rw-r--r--. 1 root root  1.6M Mar  6 17:39 libUE4Editor-AutomationMessages.debug
-rwxr-xr-x. 1 root root  414K Mar  6 17:39 libUE4Editor-AutomationMessages.so
-rw-r--r--. 1 root root  243K Mar  6 17:39 libUE4Editor-AutomationMessages.sym
-rw-r--r--. 1 root root   20M Mar  6 17:43 libUE4Editor-AutomationWindow.debug
-rwxr-xr-x. 1 root root  2.0M Mar  6 17:43 libUE4Editor-AutomationWindow.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:43 libUE4Editor-AutomationWindow.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:42 libUE4Editor-AutomationWorker.debug
-rwxr-xr-x. 1 root root  149K Mar  6 17:42 libUE4Editor-AutomationWorker.so
-rw-r--r--. 1 root root  106K Mar  6 17:42 libUE4Editor-AutomationWorker.sym
-rw-r--r--. 1 root root  1.6M Mar  6 17:46 libUE4Editor-BackgroundHTTP.debug
-rwxr-xr-x. 1 root root  126K Mar  6 17:46 libUE4Editor-BackgroundHTTP.so
-rw-r--r--. 1 root root   93K Mar  6 17:46 libUE4Editor-BackgroundHTTP.sym
-rw-r--r--. 1 root root  775K Mar  6 17:46 libUE4Editor-BackgroundHTTPFileHash.debug
-rwxr-xr-x. 1 root root  265K Mar  6 17:46 libUE4Editor-BackgroundHTTPFileHash.so
-rw-r--r--. 1 root root   78K Mar  6 17:46 libUE4Editor-BackgroundHTTPFileHash.sym
-rw-r--r--. 1 root root   22M Mar  6 17:46 libUE4Editor-BehaviorTreeEditor.debug
-rwxr-xr-x. 1 root root  2.9M Mar  6 17:46 libUE4Editor-BehaviorTreeEditor.so
-rw-r--r--. 1 root root  1.7M Mar  6 17:46 libUE4Editor-BehaviorTreeEditor.sym
-rw-r--r--. 1 root root   98K Mar  6 17:46 libUE4Editor-BlankModule.debug
-rwxr-xr-x. 1 root root  232K Mar  6 17:46 libUE4Editor-BlankModule.so
-rw-r--r--. 1 root root   48K Mar  6 17:46 libUE4Editor-BlankModule.sym
-rw-r--r--. 1 root root   10M Mar  6 17:44 libUE4Editor-BlueprintCompilerCppBackend.debug
-rwxr-xr-x. 1 root root  798K Mar  6 17:44 libUE4Editor-BlueprintCompilerCppBackend.so
-rw-r--r--. 1 root root  671K Mar  6 17:44 libUE4Editor-BlueprintCompilerCppBackend.sym
-rw-r--r--. 1 root root   45M Mar  6 17:46 libUE4Editor-BlueprintGraph.debug
-rwxr-xr-x. 1 root root  5.2M Mar  6 17:38 libUE4Editor-BlueprintGraph.so
-rw-r--r--. 1 root root  3.0M Mar  6 17:46 libUE4Editor-BlueprintGraph.sym
-rw-r--r--. 1 root root  7.9M Mar  6 17:46 libUE4Editor-BlueprintNativeCodeGen.debug
-rwxr-xr-x. 1 root root  575K Mar  6 17:44 libUE4Editor-BlueprintNativeCodeGen.so
-rw-r--r--. 1 root root  426K Mar  6 17:46 libUE4Editor-BlueprintNativeCodeGen.sym
-rw-r--r--. 1 root root  929K Mar  6 17:46 libUE4Editor-BlueprintRuntime.debug
-rwxr-xr-x. 1 root root  266K Mar  6 17:46 libUE4Editor-BlueprintRuntime.so
-rw-r--r--. 1 root root   68K Mar  6 17:46 libUE4Editor-BlueprintRuntime.sym
-rw-r--r--. 1 root root  7.5M Mar  6 17:41 libUE4Editor-Blutility.debug
-rwxr-xr-x. 1 root root  760K Mar  6 17:41 libUE4Editor-Blutility.so
-rw-r--r--. 1 root root  390K Mar  6 17:41 libUE4Editor-Blutility.sym
-rw-r--r--. 1 root root   50M Mar  6 17:41 libUE4Editor-BuildPatchServices.debug
-rwxr-xr-x. 1 root root  4.4M Mar  6 17:41 libUE4Editor-BuildPatchServices.so
-rw-r--r--. 1 root root  3.5M Mar  6 17:41 libUE4Editor-BuildPatchServices.sym
-rw-r--r--. 1 root root   17K Mar  6 17:34 libUE4Editor-BuildSettings.debug
-rwxr-xr-x. 1 root root  5.0K Mar  6 17:34 libUE4Editor-BuildSettings.so
-rw-r--r--. 1 root root   868 Mar  6 17:34 libUE4Editor-BuildSettings.sym
-rw-r--r--. 1 root root  309K Mar  6 17:41 libUE4Editor-CEF3Utils.debug
-rwxr-xr-x. 1 root root   13K Mar  6 17:41 libUE4Editor-CEF3Utils.so
-rw-r--r--. 1 root root  4.3K Mar  6 17:41 libUE4Editor-CEF3Utils.sym
-rw-r--r--. 1 root root   14M Mar  6 17:46 libUE4Editor-Cascade.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:46 libUE4Editor-Cascade.so
-rw-r--r--. 1 root root  880K Mar  6 17:46 libUE4Editor-Cascade.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:38 libUE4Editor-Cbor.debug
-rwxr-xr-x. 1 root root  324K Mar  6 17:38 libUE4Editor-Cbor.so
-rw-r--r--. 1 root root  130K Mar  6 17:38 libUE4Editor-Cbor.sym
-rw-r--r--. 1 root root  127M Mar  6 17:38 libUE4Editor-Chaos.debug
-rwxr-xr-x. 1 root root   14M Mar  6 17:38 libUE4Editor-Chaos.so
-rw-r--r--. 1 root root   11M Mar  6 17:38 libUE4Editor-Chaos.sym
-rw-r--r--. 1 root root   98K Mar  6 17:35 libUE4Editor-ChaosCore.debug
-rwxr-xr-x. 1 root root  232K Mar  6 17:35 libUE4Editor-ChaosCore.so
-rw-r--r--. 1 root root   48K Mar  6 17:35 libUE4Editor-ChaosCore.sym
-rw-r--r--. 1 root root  7.4M Mar  6 17:39 libUE4Editor-ChaosSolverEngine.debug
-rwxr-xr-x. 1 root root  611K Mar  6 17:39 libUE4Editor-ChaosSolverEngine.so
-rw-r--r--. 1 root root  365K Mar  6 17:39 libUE4Editor-ChaosSolverEngine.sym
-rw-r--r--. 1 root root  657K Mar  6 17:41 libUE4Editor-ChaosVehiclesCore.debug
-rwxr-xr-x. 1 root root  270K Mar  6 17:41 libUE4Editor-ChaosVehiclesCore.so
-rw-r--r--. 1 root root   80K Mar  6 17:41 libUE4Editor-ChaosVehiclesCore.sym
-rw-r--r--. 1 root root 1018K Mar  6 17:42 libUE4Editor-ChaosVehiclesEngine.debug
-rwxr-xr-x. 1 root root   30K Mar  6 17:42 libUE4Editor-ChaosVehiclesEngine.so
-rw-r--r--. 1 root root   12K Mar  6 17:42 libUE4Editor-ChaosVehiclesEngine.sym
-rw-r--r--. 1 root root  3.1M Mar  6 17:46 libUE4Editor-CinematicCamera.debug
-rwxr-xr-x. 1 root root  509K Mar  6 17:37 libUE4Editor-CinematicCamera.so
-rw-r--r--. 1 root root  187K Mar  6 17:46 libUE4Editor-CinematicCamera.sym
-rw-r--r--. 1 root root   11M Mar  6 17:40 libUE4Editor-ClassViewer.debug
-rwxr-xr-x. 1 root root  966K Mar  6 17:40 libUE4Editor-ClassViewer.so
-rw-r--r--. 1 root root  656K Mar  6 17:40 libUE4Editor-ClassViewer.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:46 libUE4Editor-ClientPilot.debug
-rwxr-xr-x. 1 root root   60K Mar  6 17:46 libUE4Editor-ClientPilot.so
-rw-r--r--. 1 root root   30K Mar  6 17:46 libUE4Editor-ClientPilot.sym
-rw-r--r--. 1 root root   19M Mar  6 17:46 libUE4Editor-ClothPainter.debug
-rwxr-xr-x. 1 root root  2.2M Mar  6 17:46 libUE4Editor-ClothPainter.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:46 libUE4Editor-ClothPainter.sym
-rw-r--r--. 1 root root  6.0M Mar  6 17:46 libUE4Editor-ClothingSystemEditor.debug
-rwxr-xr-x. 1 root root  455K Mar  6 17:42 libUE4Editor-ClothingSystemEditor.so
-rw-r--r--. 1 root root  290K Mar  6 17:46 libUE4Editor-ClothingSystemEditor.sym
-rw-r--r--. 1 root root  840K Mar  6 17:37 libUE4Editor-ClothingSystemEditorInterface.debug
-rwxr-xr-x. 1 root root  259K Mar  6 17:37 libUE4Editor-ClothingSystemEditorInterface.so
-rw-r--r--. 1 root root   62K Mar  6 17:37 libUE4Editor-ClothingSystemEditorInterface.sym
-rw-r--r--. 1 root root  8.2M Mar  6 17:39 libUE4Editor-ClothingSystemRuntimeCommon.debug
-rwxr-xr-x. 1 root root  768K Mar  6 17:39 libUE4Editor-ClothingSystemRuntimeCommon.so
-rw-r--r--. 1 root root  535K Mar  6 17:39 libUE4Editor-ClothingSystemRuntimeCommon.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:38 libUE4Editor-ClothingSystemRuntimeInterface.debug
-rwxr-xr-x. 1 root root  701K Mar  6 17:38 libUE4Editor-ClothingSystemRuntimeInterface.so
-rw-r--r--. 1 root root  349K Mar  6 17:38 libUE4Editor-ClothingSystemRuntimeInterface.sym
-rw-r--r--. 1 root root  7.0M Mar  6 17:40 libUE4Editor-ClothingSystemRuntimeNv.debug
-rwxr-xr-x. 1 root root  829K Mar  6 17:40 libUE4Editor-ClothingSystemRuntimeNv.so
-rw-r--r--. 1 root root  496K Mar  6 17:40 libUE4Editor-ClothingSystemRuntimeNv.sym
-rw-r--r--. 1 root root  4.3M Mar  6 17:39 libUE4Editor-CollectionManager.debug
-rwxr-xr-x. 1 root root  352K Mar  6 17:39 libUE4Editor-CollectionManager.so
-rw-r--r--. 1 root root  260K Mar  6 17:39 libUE4Editor-CollectionManager.sym
-rw-r--r--. 1 root root  9.3M Mar  6 17:46 libUE4Editor-CollisionAnalyzer.debug
-rwxr-xr-x. 1 root root  941K Mar  6 17:37 libUE4Editor-CollisionAnalyzer.so
-rw-r--r--. 1 root root  648K Mar  6 17:46 libUE4Editor-CollisionAnalyzer.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:40 libUE4Editor-CommonMenuExtensions.debug
-rwxr-xr-x. 1 root root  123K Mar  6 17:40 libUE4Editor-CommonMenuExtensions.so
-rw-r--r--. 1 root root   83K Mar  6 17:40 libUE4Editor-CommonMenuExtensions.sym
-rw-r--r--. 1 root root  7.2M Mar  6 17:41 libUE4Editor-ComponentVisualizers.debug
-rwxr-xr-x. 1 root root  678K Mar  6 17:41 libUE4Editor-ComponentVisualizers.so
-rw-r--r--. 1 root root  345K Mar  6 17:41 libUE4Editor-ComponentVisualizers.sym
-rw-r--r--. 1 root root  3.5M Mar  6 17:42 libUE4Editor-ConfigEditor.debug
-rwxr-xr-x. 1 root root  272K Mar  6 17:42 libUE4Editor-ConfigEditor.so
-rw-r--r--. 1 root root  140K Mar  6 17:42 libUE4Editor-ConfigEditor.sym
-rw-r--r--. 1 root root   46M Mar  6 17:40 libUE4Editor-ContentBrowser.debug
-rwxr-xr-x. 1 root root  4.6M Mar  6 17:40 libUE4Editor-ContentBrowser.so
-rw-r--r--. 1 root root  3.3M Mar  6 17:40 libUE4Editor-ContentBrowser.sym
-rw-r--r--. 1 root root  4.6M Mar  6 17:39 libUE4Editor-ContentBrowserData.debug
-rwxr-xr-x. 1 root root  439K Mar  6 17:39 libUE4Editor-ContentBrowserData.so
-rw-r--r--. 1 root root  292K Mar  6 17:39 libUE4Editor-ContentBrowserData.sym
-rw-r--r--. 1 root root  722K Mar  6 17:42 libUE4Editor-CookedIterativeFile.debug
-rwxr-xr-x. 1 root root   47K Mar  6 17:42 libUE4Editor-CookedIterativeFile.so
-rw-r--r--. 1 root root   27K Mar  6 17:42 libUE4Editor-CookedIterativeFile.sym
-rw-r--r--. 1 root root  103M Mar  6 17:35 libUE4Editor-Core.debug
-rwxr-xr-x. 1 root root   15M Mar  6 17:35 libUE4Editor-Core.so
-rw-r--r--. 1 root root  7.7M Mar  6 17:35 libUE4Editor-Core.sym
-rw-r--r--. 1 root root   75M Mar  6 17:35 libUE4Editor-CoreUObject.debug
-rwxr-xr-x. 1 root root  7.4M Mar  6 17:35 libUE4Editor-CoreUObject.so
-rw-r--r--. 1 root root  5.0M Mar  6 17:35 libUE4Editor-CoreUObject.sym
-rw-r--r--. 1 root root  676K Mar  6 17:46 libUE4Editor-CrashDebugHelper.debug
-rwxr-xr-x. 1 root root  259K Mar  6 17:46 libUE4Editor-CrashDebugHelper.so
-rw-r--r--. 1 root root   67K Mar  6 17:46 libUE4Editor-CrashDebugHelper.sym
-rw-r--r--. 1 root root  3.3M Mar  6 17:46 libUE4Editor-CrashReportCore.debug
-rwxr-xr-x. 1 root root  301K Mar  6 17:46 libUE4Editor-CrashReportCore.so
-rw-r--r--. 1 root root  205K Mar  6 17:46 libUE4Editor-CrashReportCore.sym
-rw-r--r--. 1 root root  717K Mar  6 17:37 libUE4Editor-CrunchCompression.debug
-rwxr-xr-x. 1 root root  280K Mar  6 17:37 libUE4Editor-CrunchCompression.so
-rw-r--r--. 1 root root   93K Mar  6 17:37 libUE4Editor-CrunchCompression.sym
-rw-r--r--. 1 root root  5.3M Mar  6 17:39 libUE4Editor-CurveAssetEditor.debug
-rwxr-xr-x. 1 root root  418K Mar  6 17:39 libUE4Editor-CurveAssetEditor.so
-rw-r--r--. 1 root root  258K Mar  6 17:39 libUE4Editor-CurveAssetEditor.sym
-rw-r--r--. 1 root root   20M Mar  6 17:39 libUE4Editor-CurveEditor.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:39 libUE4Editor-CurveEditor.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:39 libUE4Editor-CurveEditor.sym
-rw-r--r--. 1 root root  6.7M Mar  6 17:46 libUE4Editor-CurveTableEditor.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:46 libUE4Editor-CurveTableEditor.so
-rw-r--r--. 1 root root  564K Mar  6 17:46 libUE4Editor-CurveTableEditor.sym
-rw-r--r--. 1 root root   13M Mar  6 17:44 libUE4Editor-DataTableEditor.debug
-rwxr-xr-x. 1 root root  1.3M Mar  6 17:44 libUE4Editor-DataTableEditor.so
-rw-r--r--. 1 root root  811K Mar  6 17:44 libUE4Editor-DataTableEditor.sym
-rw-r--r--. 1 root root   18M Mar  6 17:41 libUE4Editor-DatasmithCore.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:41 libUE4Editor-DatasmithCore.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:41 libUE4Editor-DatasmithCore.sym
-rw-r--r--. 1 root root  2.9M Mar  6 17:46 libUE4Editor-DatasmithExporter.debug
-rwxr-xr-x. 1 root root  201K Mar  6 17:46 libUE4Editor-DatasmithExporter.so
-rw-r--r--. 1 root root  162K Mar  6 17:46 libUE4Editor-DatasmithExporter.sym
-rw-r--r--. 1 root root  4.8M Mar  6 17:35 libUE4Editor-DerivedDataCache.debug
-rwxr-xr-x. 1 root root  4.2M Mar  6 17:35 libUE4Editor-DerivedDataCache.so
-rw-r--r--. 1 root root  655K Mar  6 17:35 libUE4Editor-DerivedDataCache.sym
-rw-r--r--. 1 root root   11M Mar  6 17:35 libUE4Editor-DesktopPlatform.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:35 libUE4Editor-DesktopPlatform.so
-rw-r--r--. 1 root root  1.5M Mar  6 17:35 libUE4Editor-DesktopPlatform.sym
-rw-r--r--. 1 root root  1.8M Mar  6 17:39 libUE4Editor-DesktopWidgets.debug
-rwxr-xr-x. 1 root root  124K Mar  6 17:39 libUE4Editor-DesktopWidgets.so
-rw-r--r--. 1 root root   65K Mar  6 17:39 libUE4Editor-DesktopWidgets.sym
-rw-r--r--. 1 root root  124M Mar  6 17:46 libUE4Editor-DetailCustomizations.debug
-rwxr-xr-x. 1 root root   12M Mar  6 17:42 libUE4Editor-DetailCustomizations.so
-rw-r--r--. 1 root root  8.2M Mar  6 17:46 libUE4Editor-DetailCustomizations.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:36 libUE4Editor-DeveloperSettings.debug
-rwxr-xr-x. 1 root root  269K Mar  6 17:36 libUE4Editor-DeveloperSettings.so
-rw-r--r--. 1 root root   71K Mar  6 17:36 libUE4Editor-DeveloperSettings.sym
-rw-r--r--. 1 root root   18M Mar  6 17:46 libUE4Editor-DeviceManager.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:46 libUE4Editor-DeviceManager.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:46 libUE4Editor-DeviceManager.sym
-rw-r--r--. 1 root root   12M Mar  6 17:44 libUE4Editor-DeviceProfileEditor.debug
-rwxr-xr-x. 1 root root  1.2M Mar  6 17:44 libUE4Editor-DeviceProfileEditor.so
-rw-r--r--. 1 root root  783K Mar  6 17:44 libUE4Editor-DeviceProfileEditor.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:39 libUE4Editor-DeviceProfileServices.debug
-rwxr-xr-x. 1 root root  274K Mar  6 17:39 libUE4Editor-DeviceProfileServices.so
-rw-r--r--. 1 root root   88K Mar  6 17:39 libUE4Editor-DeviceProfileServices.sym
-rw-r--r--. 1 root root  4.9M Mar  6 17:40 libUE4Editor-DirectLink.debug
-rwxr-xr-x. 1 root root  405K Mar  6 17:40 libUE4Editor-DirectLink.so
-rw-r--r--. 1 root root  391K Mar  6 17:40 libUE4Editor-DirectLink.sym
-rw-r--r--. 1 root root  4.4M Mar  6 17:38 libUE4Editor-DirectoryWatcher.debug
-rwxr-xr-x. 1 root root  562K Mar  6 17:38 libUE4Editor-DirectoryWatcher.so
-rw-r--r--. 1 root root  322K Mar  6 17:38 libUE4Editor-DirectoryWatcher.sym
-rw-r--r--. 1 root root  5.4M Mar  6 17:42 libUE4Editor-DistCurveEditor.debug
-rwxr-xr-x. 1 root root  451K Mar  6 17:42 libUE4Editor-DistCurveEditor.so
-rw-r--r--. 1 root root  256K Mar  6 17:42 libUE4Editor-DistCurveEditor.sym
-rw-r--r--. 1 root root  5.7M Mar  6 17:46 libUE4Editor-Documentation.debug
-rwxr-xr-x. 1 root root 1007K Mar  6 17:40 libUE4Editor-Documentation.so
-rw-r--r--. 1 root root  451K Mar  6 17:46 libUE4Editor-Documentation.sym
-rw-r--r--. 1 root root  1.7M Mar  6 17:37 libUE4Editor-EditorAnalyticsSession.debug
-rwxr-xr-x. 1 root root  135K Mar  6 17:37 libUE4Editor-EditorAnalyticsSession.so
-rw-r--r--. 1 root root   81K Mar  6 17:37 libUE4Editor-EditorAnalyticsSession.sym
-rw-r--r--. 1 root root  3.4M Mar  6 17:46 libUE4Editor-EditorInteractiveToolsFramework.debug
-rwxr-xr-x. 1 root root  649K Mar  6 17:40 libUE4Editor-EditorInteractiveToolsFramework.so
-rw-r--r--. 1 root root  261K Mar  6 17:46 libUE4Editor-EditorInteractiveToolsFramework.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:46 libUE4Editor-EditorSettingsViewer.debug
-rwxr-xr-x. 1 root root  587K Mar  6 17:46 libUE4Editor-EditorSettingsViewer.so
-rw-r--r--. 1 root root  204K Mar  6 17:46 libUE4Editor-EditorSettingsViewer.sym
-rw-r--r--. 1 root root  6.1M Mar  6 17:36 libUE4Editor-EditorStyle.debug
-rwxr-xr-x. 1 root root  2.3M Mar  6 17:36 libUE4Editor-EditorStyle.so
-rw-r--r--. 1 root root  1.2M Mar  6 17:36 libUE4Editor-EditorStyle.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:39 libUE4Editor-EditorSubsystem.debug
-rwxr-xr-x. 1 root root  255K Mar  6 17:39 libUE4Editor-EditorSubsystem.so
-rw-r--r--. 1 root root   57K Mar  6 17:39 libUE4Editor-EditorSubsystem.sym
-rw-r--r--. 1 root root   21M Mar  6 17:39 libUE4Editor-EditorWidgets.debug
-rwxr-xr-x. 1 root root  2.0M Mar  6 17:39 libUE4Editor-EditorWidgets.so
-rw-r--r--. 1 root root  1.5M Mar  6 17:39 libUE4Editor-EditorWidgets.sym
-rw-r--r--. 1 root root  595M Mar  6 17:39 libUE4Editor-Engine.debug
-rwxr-xr-x. 1 root root   73M Mar  6 17:39 libUE4Editor-Engine.so
-rw-r--r--. 1 root root   41M Mar  6 17:39 libUE4Editor-Engine.sym
-rw-r--r--. 1 root root  870K Mar  6 17:35 libUE4Editor-EngineMessages.debug
-rwxr-xr-x. 1 root root  290K Mar  6 17:35 libUE4Editor-EngineMessages.so
-rw-r--r--. 1 root root  109K Mar  6 17:35 libUE4Editor-EngineMessages.sym
-rw-r--r--. 1 root root  2.5M Mar  6 17:36 libUE4Editor-EngineSettings.debug
-rwxr-xr-x. 1 root root  389K Mar  6 17:36 libUE4Editor-EngineSettings.so
-rw-r--r--. 1 root root  104K Mar  6 17:36 libUE4Editor-EngineSettings.sym
-rw-r--r--. 1 root root  5.3M Mar  6 17:39 libUE4Editor-EnvironmentLightingViewer.debug
-rwxr-xr-x. 1 root root  502K Mar  6 17:39 libUE4Editor-EnvironmentLightingViewer.so
-rw-r--r--. 1 root root  318K Mar  6 17:39 libUE4Editor-EnvironmentLightingViewer.sym
-rw-r--r--. 1 root root  2.3M Mar  6 17:40 libUE4Editor-ExternalImagePicker.debug
-rwxr-xr-x. 1 root root  192K Mar  6 17:40 libUE4Editor-ExternalImagePicker.so
-rw-r--r--. 1 root root   92K Mar  6 17:40 libUE4Editor-ExternalImagePicker.sym
-rw-r--r--. 1 root root  1.7M Mar  6 17:46 libUE4Editor-ExternalRpcRegistry.debug
-rwxr-xr-x. 1 root root  106K Mar  6 17:46 libUE4Editor-ExternalRpcRegistry.so
-rw-r--r--. 1 root root   78K Mar  6 17:46 libUE4Editor-ExternalRpcRegistry.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:46 libUE4Editor-EyeTracker.debug
-rwxr-xr-x. 1 root root   66K Mar  6 17:46 libUE4Editor-EyeTracker.so
-rw-r--r--. 1 root root   33K Mar  6 17:46 libUE4Editor-EyeTracker.sym
-rw-r--r--. 1 root root  5.1M Mar  6 17:40 libUE4Editor-FieldSystemEngine.debug
-rwxr-xr-x. 1 root root  714K Mar  6 17:40 libUE4Editor-FieldSystemEngine.so
-rw-r--r--. 1 root root  203K Mar  6 17:40 libUE4Editor-FieldSystemEngine.sym
-rw-r--r--. 1 root root  510K Mar  6 17:46 libUE4Editor-FileUtilities.debug
-rwxr-xr-x. 1 root root  247K Mar  6 17:46 libUE4Editor-FileUtilities.so
-rw-r--r--. 1 root root   58K Mar  6 17:46 libUE4Editor-FileUtilities.sym
-rw-r--r--. 1 root root   12M Mar  6 17:39 libUE4Editor-Foliage.debug
-rwxr-xr-x. 1 root root  1.2M Mar  6 17:39 libUE4Editor-Foliage.so
-rw-r--r--. 1 root root  656K Mar  6 17:39 libUE4Editor-Foliage.sym
-rw-r--r--. 1 root root   23M Mar  6 17:44 libUE4Editor-FoliageEdit.debug
-rwxr-xr-x. 1 root root  2.2M Mar  6 17:44 libUE4Editor-FoliageEdit.so
-rw-r--r--. 1 root root  1.5M Mar  6 17:44 libUE4Editor-FoliageEdit.sym
-rw-r--r--. 1 root root   25M Mar  6 17:47 libUE4Editor-FontEditor.debug
-rwxr-xr-x. 1 root root  3.0M Mar  6 17:47 libUE4Editor-FontEditor.so
-rw-r--r--. 1 root root  1.9M Mar  6 17:47 libUE4Editor-FontEditor.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:46 libUE4Editor-FriendsAndChat.debug
-rwxr-xr-x. 1 root root  522K Mar  6 17:46 libUE4Editor-FriendsAndChat.so
-rw-r--r--. 1 root root  159K Mar  6 17:46 libUE4Editor-FriendsAndChat.sym
-rw-r--r--. 1 root root  9.9M Mar  6 17:41 libUE4Editor-FunctionalTesting.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:41 libUE4Editor-FunctionalTesting.so
-rw-r--r--. 1 root root  546K Mar  6 17:41 libUE4Editor-FunctionalTesting.sym
-rw-r--r--. 1 root root  3.8M Mar  6 17:46 libUE4Editor-GameMenuBuilder.debug
-rwxr-xr-x. 1 root root  338K Mar  6 17:46 libUE4Editor-GameMenuBuilder.so
-rw-r--r--. 1 root root  185K Mar  6 17:46 libUE4Editor-GameMenuBuilder.sym
-rw-r--r--. 1 root root   27M Mar  6 17:41 libUE4Editor-GameProjectGeneration.debug
-rwxr-xr-x. 1 root root  2.8M Mar  6 17:41 libUE4Editor-GameProjectGeneration.so
-rw-r--r--. 1 root root  1.9M Mar  6 17:41 libUE4Editor-GameProjectGeneration.sym
-rw-r--r--. 1 root root  9.7M Mar  6 17:40 libUE4Editor-GameplayDebugger.debug
-rwxr-xr-x. 1 root root  725K Mar  6 17:40 libUE4Editor-GameplayDebugger.so
-rw-r--r--. 1 root root  492K Mar  6 17:40 libUE4Editor-GameplayDebugger.sym
-rw-r--r--. 1 root root  6.9M Mar  6 17:46 libUE4Editor-GameplayTags.debug
-rwxr-xr-x. 1 root root  779K Mar  6 17:37 libUE4Editor-GameplayTags.so
-rw-r--r--. 1 root root  474K Mar  6 17:46 libUE4Editor-GameplayTags.sym
-rw-r--r--. 1 root root  2.9M Mar  6 17:39 libUE4Editor-GameplayTasks.debug
-rwxr-xr-x. 1 root root  486K Mar  6 17:39 libUE4Editor-GameplayTasks.so
-rw-r--r--. 1 root root  172K Mar  6 17:39 libUE4Editor-GameplayTasks.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:44 libUE4Editor-GameplayTasksEditor.debug
-rwxr-xr-x. 1 root root  111K Mar  6 17:44 libUE4Editor-GameplayTasksEditor.so
-rw-r--r--. 1 root root   65K Mar  6 17:44 libUE4Editor-GameplayTasksEditor.sym
-rw-r--r--. 1 root root  2.8M Mar  6 17:46 libUE4Editor-GammaUI.debug
-rwxr-xr-x. 1 root root  195K Mar  6 17:46 libUE4Editor-GammaUI.so
-rw-r--r--. 1 root root   92K Mar  6 17:46 libUE4Editor-GammaUI.sym
-rw-r--r--. 1 root root   19M Mar  6 17:40 libUE4Editor-GeometryCollectionEngine.debug
-rwxr-xr-x. 1 root root  2.1M Mar  6 17:40 libUE4Editor-GeometryCollectionEngine.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:40 libUE4Editor-GeometryCollectionEngine.sym
-rw-r--r--. 1 root root  439K Mar  6 17:39 libUE4Editor-GraphColor.debug
-rwxr-xr-x. 1 root root  251K Mar  6 17:39 libUE4Editor-GraphColor.so
-rw-r--r--. 1 root root   74K Mar  6 17:39 libUE4Editor-GraphColor.sym
-rw-r--r--. 1 root root   50M Mar  6 17:46 libUE4Editor-GraphEditor.debug
-rwxr-xr-x. 1 root root  5.1M Mar  6 17:40 libUE4Editor-GraphEditor.so
-rw-r--r--. 1 root root  3.3M Mar  6 17:46 libUE4Editor-GraphEditor.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:35 libUE4Editor-HTTP.debug
-rwxr-xr-x. 1 root root  4.5M Mar  6 17:35 libUE4Editor-HTTP.so
-rw-r--r--. 1 root root  570K Mar  6 17:35 libUE4Editor-HTTP.sym
-rw-r--r--. 1 root root  2.8M Mar  6 17:36 libUE4Editor-HTTPServer.debug
-rwxr-xr-x. 1 root root  423K Mar  6 17:36 libUE4Editor-HTTPServer.so
-rw-r--r--. 1 root root  225K Mar  6 17:36 libUE4Editor-HTTPServer.sym
-rw-r--r--. 1 root root  914K Mar  6 17:46 libUE4Editor-HardwareSurvey.debug
-rwxr-xr-x. 1 root root   64K Mar  6 17:46 libUE4Editor-HardwareSurvey.so
-rw-r--r--. 1 root root   28K Mar  6 17:46 libUE4Editor-HardwareSurvey.sym
-rw-r--r--. 1 root root  3.3M Mar  6 17:40 libUE4Editor-HardwareTargeting.debug
-rwxr-xr-x. 1 root root  249K Mar  6 17:40 libUE4Editor-HardwareTargeting.so
-rw-r--r--. 1 root root  144K Mar  6 17:40 libUE4Editor-HardwareTargeting.sym
-rw-r--r--. 1 root root   11M Mar  6 17:39 libUE4Editor-HeadMountedDisplay.debug
-rwxr-xr-x. 1 root root  944K Mar  6 17:39 libUE4Editor-HeadMountedDisplay.so
-rw-r--r--. 1 root root  521K Mar  6 17:39 libUE4Editor-HeadMountedDisplay.sym
-rw-r--r--. 1 root root  9.3M Mar  6 17:40 libUE4Editor-HierarchicalLODOutliner.debug
-rwxr-xr-x. 1 root root  915K Mar  6 17:40 libUE4Editor-HierarchicalLODOutliner.so
-rw-r--r--. 1 root root  664K Mar  6 17:40 libUE4Editor-HierarchicalLODOutliner.sym
-rw-r--r--. 1 root root  2.6M Mar  6 17:39 libUE4Editor-HierarchicalLODUtilities.debug
-rwxr-xr-x. 1 root root  143K Mar  6 17:39 libUE4Editor-HierarchicalLODUtilities.so
-rw-r--r--. 1 root root  112K Mar  6 17:39 libUE4Editor-HierarchicalLODUtilities.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:41 libUE4Editor-HotReload.debug
-rwxr-xr-x. 1 root root  290K Mar  6 17:41 libUE4Editor-HotReload.so
-rw-r--r--. 1 root root  236K Mar  6 17:41 libUE4Editor-HotReload.sym
-rw-r--r--. 1 root root  4.7M Mar  6 17:46 libUE4Editor-HttpNetworkReplayStreaming.debug
-rwxr-xr-x. 1 root root  477K Mar  6 17:46 libUE4Editor-HttpNetworkReplayStreaming.so
-rw-r--r--. 1 root root  361K Mar  6 17:46 libUE4Editor-HttpNetworkReplayStreaming.sym
-rw-r--r--. 1 root root  578K Mar  6 17:44 libUE4Editor-IESFile.debug
-rwxr-xr-x. 1 root root  254K Mar  6 17:44 libUE4Editor-IESFile.so
-rw-r--r--. 1 root root   63K Mar  6 17:44 libUE4Editor-IESFile.sym
-rw-r--r--. 1 root root   98K Mar  6 17:46 libUE4Editor-IPC.debug
-rwxr-xr-x. 1 root root  232K Mar  6 17:46 libUE4Editor-IPC.so
-rw-r--r--. 1 root root   48K Mar  6 17:46 libUE4Editor-IPC.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:44 libUE4Editor-Icmp.debug
-rwxr-xr-x. 1 root root  400K Mar  6 17:44 libUE4Editor-Icmp.so
-rw-r--r--. 1 root root  182K Mar  6 17:44 libUE4Editor-Icmp.sym
-rw-r--r--. 1 root root  877K Mar  6 17:35 libUE4Editor-ImageCore.debug
-rwxr-xr-x. 1 root root  281K Mar  6 17:35 libUE4Editor-ImageCore.so
-rw-r--r--. 1 root root   81K Mar  6 17:35 libUE4Editor-ImageCore.sym
-rw-r--r--. 1 root root 1017K Mar  6 17:46 libUE4Editor-ImageDownload.debug
-rwxr-xr-x. 1 root root   59K Mar  6 17:46 libUE4Editor-ImageDownload.so
-rw-r--r--. 1 root root   44K Mar  6 17:46 libUE4Editor-ImageDownload.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:35 libUE4Editor-ImageWrapper.debug
-rwxr-xr-x. 1 root root  4.3M Mar  6 17:35 libUE4Editor-ImageWrapper.so
-rw-r--r--. 1 root root  549K Mar  6 17:35 libUE4Editor-ImageWrapper.sym
-rw-r--r--. 1 root root  2.6M Mar  6 17:39 libUE4Editor-ImageWriteQueue.debug
-rwxr-xr-x. 1 root root  171K Mar  6 17:39 libUE4Editor-ImageWriteQueue.so
-rw-r--r--. 1 root root  105K Mar  6 17:39 libUE4Editor-ImageWriteQueue.sym
-rw-r--r--. 1 root root  2.8M Mar  6 17:46 libUE4Editor-InMemoryNetworkReplayStreaming.debug
-rwxr-xr-x. 1 root root  247K Mar  6 17:46 libUE4Editor-InMemoryNetworkReplayStreaming.so
-rw-r--r--. 1 root root  187K Mar  6 17:46 libUE4Editor-InMemoryNetworkReplayStreaming.sym
-rw-r--r--. 1 root root  4.2M Mar  6 17:46 libUE4Editor-InputBindingEditor.debug
-rwxr-xr-x. 1 root root  833K Mar  6 17:42 libUE4Editor-InputBindingEditor.so
-rw-r--r--. 1 root root  348K Mar  6 17:46 libUE4Editor-InputBindingEditor.sym
-rw-r--r--. 1 root root  2.6M Mar  6 17:35 libUE4Editor-InputCore.debug
-rwxr-xr-x. 1 root root  644K Mar  6 17:35 libUE4Editor-InputCore.so
-rw-r--r--. 1 root root  290K Mar  6 17:35 libUE4Editor-InputCore.sym
-rw-r--r--. 1 root root  578K Mar  6 17:40 libUE4Editor-InputDevice.debug
-rwxr-xr-x. 1 root root  235K Mar  6 17:40 libUE4Editor-InputDevice.so
-rw-r--r--. 1 root root   49K Mar  6 17:40 libUE4Editor-InputDevice.sym
-rw-r--r--. 1 root root  5.5M Mar  6 17:41 libUE4Editor-InstallBundleManager.debug
-rwxr-xr-x. 1 root root  447K Mar  6 17:41 libUE4Editor-InstallBundleManager.so
-rw-r--r--. 1 root root  383K Mar  6 17:41 libUE4Editor-InstallBundleManager.sym
-rw-r--r--. 1 root root   11M Mar  6 17:39 libUE4Editor-InteractiveToolsFramework.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:39 libUE4Editor-InteractiveToolsFramework.so
-rw-r--r--. 1 root root  662K Mar  6 17:39 libUE4Editor-InteractiveToolsFramework.sym
-rw-r--r--. 1 root root  6.3M Mar  6 17:41 libUE4Editor-InternationalizationSettings.debug
-rwxr-xr-x. 1 root root  588K Mar  6 17:41 libUE4Editor-InternationalizationSettings.so
-rw-r--r--. 1 root root  365K Mar  6 17:41 libUE4Editor-InternationalizationSettings.sym
-rw-r--r--. 1 root root   22M Mar  6 17:42 libUE4Editor-IntroTutorials.debug
-rwxr-xr-x. 1 root root  2.2M Mar  6 17:42 libUE4Editor-IntroTutorials.so
-rw-r--r--. 1 root root  1.5M Mar  6 17:42 libUE4Editor-IntroTutorials.sym
-rw-r--r--. 1 root root  9.4M Mar  6 17:44 libUE4Editor-IoStoreUtilities.debug
-rwxr-xr-x. 1 root root  609K Mar  6 17:44 libUE4Editor-IoStoreUtilities.so
-rw-r--r--. 1 root root  570K Mar  6 17:44 libUE4Editor-IoStoreUtilities.sym
-rw-r--r--. 1 root root  2.2M Mar  6 17:35 libUE4Editor-Json.debug
-rwxr-xr-x. 1 root root  453K Mar  6 17:35 libUE4Editor-Json.so
-rw-r--r--. 1 root root  204K Mar  6 17:35 libUE4Editor-Json.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:38 libUE4Editor-JsonUtilities.debug
-rwxr-xr-x. 1 root root  237K Mar  6 17:38 libUE4Editor-JsonUtilities.so
-rw-r--r--. 1 root root  177K Mar  6 17:38 libUE4Editor-JsonUtilities.sym
-rw-r--r--. 1 root root  136M Mar  6 17:46 libUE4Editor-Kismet.debug
-rwxr-xr-x. 1 root root   13M Mar  6 17:38 libUE4Editor-Kismet.so
-rw-r--r--. 1 root root  9.3M Mar  6 17:46 libUE4Editor-Kismet.sym
-rw-r--r--. 1 root root   12M Mar  6 17:46 libUE4Editor-KismetCompiler.debug
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:39 libUE4Editor-KismetCompiler.so
-rw-r--r--. 1 root root  946K Mar  6 17:46 libUE4Editor-KismetCompiler.sym
-rw-r--r--. 1 root root   14M Mar  6 17:40 libUE4Editor-KismetWidgets.debug
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:40 libUE4Editor-KismetWidgets.so
-rw-r--r--. 1 root root  912K Mar  6 17:40 libUE4Editor-KismetWidgets.sym
-rw-r--r--. 1 root root   51M Mar  6 17:46 libUE4Editor-Landscape.debug
-rwxr-xr-x. 1 root root  4.6M Mar  6 17:37 libUE4Editor-Landscape.so
-rw-r--r--. 1 root root  3.2M Mar  6 17:46 libUE4Editor-Landscape.sym
-rw-r--r--. 1 root root   36M Mar  6 17:43 libUE4Editor-LandscapeEditor.debug
-rwxr-xr-x. 1 root root  3.9M Mar  6 17:43 libUE4Editor-LandscapeEditor.so
-rw-r--r--. 1 root root  2.6M Mar  6 17:43 libUE4Editor-LandscapeEditor.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:41 libUE4Editor-LandscapeEditorUtilities.debug
-rwxr-xr-x. 1 root root   47K Mar  6 17:41 libUE4Editor-LandscapeEditorUtilities.so
-rw-r--r--. 1 root root   14K Mar  6 17:41 libUE4Editor-LandscapeEditorUtilities.sym
-rw-r--r--. 1 root root  705K Mar  6 17:44 libUE4Editor-LaunchDaemonMessages.debug
-rwxr-xr-x. 1 root root  258K Mar  6 17:44 libUE4Editor-LaunchDaemonMessages.so
-rw-r--r--. 1 root root   76K Mar  6 17:44 libUE4Editor-LaunchDaemonMessages.sym
-rw-r--r--. 1 root root  331K Mar  6 17:46 libUE4Editor-LauncherCheck.debug
-rwxr-xr-x. 1 root root  233K Mar  6 17:46 libUE4Editor-LauncherCheck.so
-rw-r--r--. 1 root root   49K Mar  6 17:46 libUE4Editor-LauncherCheck.sym
-rw-r--r--. 1 root root  347K Mar  6 17:35 libUE4Editor-LauncherPlatform.debug
-rwxr-xr-x. 1 root root  235K Mar  6 17:35 libUE4Editor-LauncherPlatform.so
-rw-r--r--. 1 root root   49K Mar  6 17:35 libUE4Editor-LauncherPlatform.sym
-rw-r--r--. 1 root root  4.9M Mar  6 17:41 libUE4Editor-LauncherServices.debug
-rwxr-xr-x. 1 root root  461K Mar  6 17:41 libUE4Editor-LauncherServices.so
-rw-r--r--. 1 root root  316K Mar  6 17:41 libUE4Editor-LauncherServices.sym
-rw-r--r--. 1 root root   11M Mar  6 17:42 libUE4Editor-Layers.debug
-rwxr-xr-x. 1 root root  983K Mar  6 17:42 libUE4Editor-Layers.so
-rw-r--r--. 1 root root  677K Mar  6 17:42 libUE4Editor-Layers.sym
-rw-r--r--. 1 root root   54M Mar  6 17:40 libUE4Editor-LevelEditor.debug
-rwxr-xr-x. 1 root root  5.1M Mar  6 17:40 libUE4Editor-LevelEditor.so
-rw-r--r--. 1 root root  3.0M Mar  6 17:40 libUE4Editor-LevelEditor.sym
-rw-r--r--. 1 root root  7.5M Mar  6 17:40 libUE4Editor-LevelSequence.debug
-rwxr-xr-x. 1 root root  600K Mar  6 17:40 libUE4Editor-LevelSequence.so
-rw-r--r--. 1 root root  353K Mar  6 17:40 libUE4Editor-LevelSequence.sym
-rw-r--r--. 1 root root  528K Mar  6 17:46 libUE4Editor-LinuxPlatformEditor.debug
-rwxr-xr-x. 1 root root   12K Mar  6 17:46 libUE4Editor-LinuxPlatformEditor.so
-rw-r--r--. 1 root root  2.8K Mar  6 17:46 libUE4Editor-LinuxPlatformEditor.sym
-rw-r--r--. 1 root root  4.5M Mar  6 17:39 libUE4Editor-LiveLinkInterface.debug
-rwxr-xr-x. 1 root root  795K Mar  6 17:39 libUE4Editor-LiveLinkInterface.so
-rw-r--r--. 1 root root  507K Mar  6 17:39 libUE4Editor-LiveLinkInterface.sym
-rw-r--r--. 1 root root  2.2M Mar  6 17:39 libUE4Editor-LiveLinkMessageBusFramework.debug
-rwxr-xr-x. 1 root root  146K Mar  6 17:39 libUE4Editor-LiveLinkMessageBusFramework.so
-rw-r--r--. 1 root root  137K Mar  6 17:39 libUE4Editor-LiveLinkMessageBusFramework.sym
-rw-r--r--. 1 root root  7.6M Mar  6 17:44 libUE4Editor-LocalFileNetworkReplayStreaming.debug
-rwxr-xr-x. 1 root root  796K Mar  6 17:44 libUE4Editor-LocalFileNetworkReplayStreaming.so
-rw-r--r--. 1 root root  586K Mar  6 17:44 libUE4Editor-LocalFileNetworkReplayStreaming.sym
-rw-r--r--. 1 root root   12M Mar  6 17:41 libUE4Editor-Localization.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:41 libUE4Editor-Localization.so
-rw-r--r--. 1 root root  758K Mar  6 17:41 libUE4Editor-Localization.sym
-rw-r--r--. 1 root root  7.1M Mar  6 17:42 libUE4Editor-LocalizationCommandletExecution.debug
-rwxr-xr-x. 1 root root  607K Mar  6 17:42 libUE4Editor-LocalizationCommandletExecution.so
-rw-r--r--. 1 root root  352K Mar  6 17:42 libUE4Editor-LocalizationCommandletExecution.sym
-rw-r--r--. 1 root root   22M Mar  6 17:47 libUE4Editor-LocalizationDashboard.debug
-rwxr-xr-x. 1 root root  2.2M Mar  6 17:47 libUE4Editor-LocalizationDashboard.so
-rw-r--r--. 1 root root  1.6M Mar  6 17:47 libUE4Editor-LocalizationDashboard.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:46 libUE4Editor-LocalizationService.debug
-rwxr-xr-x. 1 root root  723K Mar  6 17:41 libUE4Editor-LocalizationService.so
-rw-r--r--. 1 root root  283K Mar  6 17:46 libUE4Editor-LocalizationService.sym
-rw-r--r--. 1 root root   24M Mar  6 17:46 libUE4Editor-LogVisualizer.debug
-rwxr-xr-x. 1 root root  2.7M Mar  6 17:37 libUE4Editor-LogVisualizer.so
-rw-r--r--. 1 root root  1.6M Mar  6 17:46 libUE4Editor-LogVisualizer.sym
-rw-r--r--. 1 root root  5.8M Mar  6 17:39 libUE4Editor-MRMesh.debug
-rwxr-xr-x. 1 root root  580K Mar  6 17:39 libUE4Editor-MRMesh.so
-rw-r--r--. 1 root root  240K Mar  6 17:39 libUE4Editor-MRMesh.sym
-rw-r--r--. 1 root root  7.9M Mar  6 17:46 libUE4Editor-MainFrame.debug
-rwxr-xr-x. 1 root root  818K Mar  6 17:38 libUE4Editor-MainFrame.so
-rw-r--r--. 1 root root  430K Mar  6 17:46 libUE4Editor-MainFrame.sym
-rw-r--r--. 1 root root  7.8M Mar  6 17:40 libUE4Editor-MaterialBaking.debug
-rwxr-xr-x. 1 root root  527K Mar  6 17:40 libUE4Editor-MaterialBaking.so
-rw-r--r--. 1 root root  330K Mar  6 17:40 libUE4Editor-MaterialBaking.sym
-rw-r--r--. 1 root root   57M Mar  6 17:40 libUE4Editor-MaterialEditor.debug
-rwxr-xr-x. 1 root root  5.2M Mar  6 17:40 libUE4Editor-MaterialEditor.so
-rw-r--r--. 1 root root  3.6M Mar  6 17:40 libUE4Editor-MaterialEditor.sym
-rw-r--r--. 1 root root  5.3M Mar  6 17:46 libUE4Editor-MaterialShaderQualitySettings.debug
-rwxr-xr-x. 1 root root  442K Mar  6 17:36 libUE4Editor-MaterialShaderQualitySettings.so
-rw-r--r--. 1 root root  294K Mar  6 17:46 libUE4Editor-MaterialShaderQualitySettings.sym
-rw-r--r--. 1 root root  6.3M Mar  6 17:46 libUE4Editor-MaterialUtilities.debug
-rwxr-xr-x. 1 root root  807K Mar  6 17:38 libUE4Editor-MaterialUtilities.so
-rw-r--r--. 1 root root  434K Mar  6 17:46 libUE4Editor-MaterialUtilities.sym
-rw-r--r--. 1 root root   25M Mar  6 17:46 libUE4Editor-Matinee.debug
-rwxr-xr-x. 1 root root  3.6M Mar  6 17:46 libUE4Editor-Matinee.so
-rw-r--r--. 1 root root  2.7M Mar  6 17:46 libUE4Editor-Matinee.sym
-rw-r--r--. 1 root root  912K Mar  6 17:37 libUE4Editor-Media.debug
-rwxr-xr-x. 1 root root  276K Mar  6 17:37 libUE4Editor-Media.so
-rw-r--r--. 1 root root   80K Mar  6 17:37 libUE4Editor-Media.sym
-rw-r--r--. 1 root root  8.6M Mar  6 17:39 libUE4Editor-MediaAssets.debug
-rwxr-xr-x. 1 root root  885K Mar  6 17:39 libUE4Editor-MediaAssets.so
-rw-r--r--. 1 root root  440K Mar  6 17:39 libUE4Editor-MediaAssets.sym
-rw-r--r--. 1 root root  272K Mar  6 17:46 libUE4Editor-MediaInfo.debug
-rwxr-xr-x. 1 root root  9.1K Mar  6 17:46 libUE4Editor-MediaInfo.so
-rw-r--r--. 1 root root  2.4K Mar  6 17:46 libUE4Editor-MediaInfo.sym
-rw-r--r--. 1 root root  2.9M Mar  6 17:39 libUE4Editor-MediaUtils.debug
-rwxr-xr-x. 1 root root  254K Mar  6 17:39 libUE4Editor-MediaUtils.so
-rw-r--r--. 1 root root  197K Mar  6 17:39 libUE4Editor-MediaUtils.sym
-rw-r--r--. 1 root root  7.6M Mar  6 17:46 libUE4Editor-Merge.debug
-rwxr-xr-x. 1 root root  1.2M Mar  6 17:44 libUE4Editor-Merge.so
-rw-r--r--. 1 root root  583K Mar  6 17:46 libUE4Editor-Merge.sym
-rw-r--r--. 1 root root   13M Mar  6 17:46 libUE4Editor-MergeActors.debug
-rwxr-xr-x. 1 root root  1.8M Mar  6 17:46 libUE4Editor-MergeActors.so
-rw-r--r--. 1 root root  1.1M Mar  6 17:46 libUE4Editor-MergeActors.sym
-rw-r--r--. 1 root root  2.2M Mar  6 17:41 libUE4Editor-MeshBoneReduction.debug
-rwxr-xr-x. 1 root root  307K Mar  6 17:41 libUE4Editor-MeshBoneReduction.so
-rw-r--r--. 1 root root  110K Mar  6 17:41 libUE4Editor-MeshBoneReduction.sym
-rw-r--r--. 1 root root  3.6M Mar  6 17:41 libUE4Editor-MeshBuilder.debug
-rwxr-xr-x. 1 root root  130K Mar  6 17:41 libUE4Editor-MeshBuilder.so
-rw-r--r--. 1 root root  106K Mar  6 17:41 libUE4Editor-MeshBuilder.sym
-rw-r--r--. 1 root root  838K Mar  6 17:39 libUE4Editor-MeshBuilderCommon.debug
-rwxr-xr-x. 1 root root  306K Mar  6 17:39 libUE4Editor-MeshBuilderCommon.so
-rw-r--r--. 1 root root   80K Mar  6 17:39 libUE4Editor-MeshBuilderCommon.sym
-rw-r--r--. 1 root root  7.4M Mar  6 17:36 libUE4Editor-MeshDescription.debug
-rwxr-xr-x. 1 root root  893K Mar  6 17:36 libUE4Editor-MeshDescription.so
-rw-r--r--. 1 root root  556K Mar  6 17:36 libUE4Editor-MeshDescription.sym
-rw-r--r--. 1 root root  776K Mar  6 17:46 libUE4Editor-MeshDescriptionOperations.debug
-rwxr-xr-x. 1 root root   19K Mar  6 17:46 libUE4Editor-MeshDescriptionOperations.so
-rw-r--r--. 1 root root  7.0K Mar  6 17:46 libUE4Editor-MeshDescriptionOperations.sym
-rw-r--r--. 1 root root   13M Mar  6 17:44 libUE4Editor-MeshMergeUtilities.debug
-rwxr-xr-x. 1 root root  765K Mar  6 17:44 libUE4Editor-MeshMergeUtilities.so
-rw-r--r--. 1 root root  681K Mar  6 17:44 libUE4Editor-MeshMergeUtilities.sym
-rw-r--r--. 1 root root   12M Mar  6 17:46 libUE4Editor-MeshPaint.debug
-rwxr-xr-x. 1 root root  801K Mar  6 17:41 libUE4Editor-MeshPaint.so
-rw-r--r--. 1 root root  532K Mar  6 17:46 libUE4Editor-MeshPaint.sym
-rw-r--r--. 1 root root   12M Mar  6 17:46 libUE4Editor-MeshPaintMode.debug
-rwxr-xr-x. 1 root root  927K Mar  6 17:44 libUE4Editor-MeshPaintMode.so
-rw-r--r--. 1 root root  595K Mar  6 17:46 libUE4Editor-MeshPaintMode.sym
-rw-r--r--. 1 root root  710K Mar  6 17:41 libUE4Editor-MeshReductionInterface.debug
-rwxr-xr-x. 1 root root  251K Mar  6 17:41 libUE4Editor-MeshReductionInterface.so
-rw-r--r--. 1 root root   60K Mar  6 17:41 libUE4Editor-MeshReductionInterface.sym
-rw-r--r--. 1 root root  9.0M Mar  6 17:41 libUE4Editor-MeshUtilities.debug
-rwxr-xr-x. 1 root root  709K Mar  6 17:41 libUE4Editor-MeshUtilities.so
-rw-r--r--. 1 root root  569K Mar  6 17:41 libUE4Editor-MeshUtilities.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:35 libUE4Editor-MeshUtilitiesCommon.debug
-rwxr-xr-x. 1 root root  368K Mar  6 17:35 libUE4Editor-MeshUtilitiesCommon.so
-rw-r--r--. 1 root root  173K Mar  6 17:35 libUE4Editor-MeshUtilitiesCommon.sym
-rw-r--r--. 1 root root   12M Mar  6 17:38 libUE4Editor-MessageLog.debug
-rwxr-xr-x. 1 root root  1.2M Mar  6 17:38 libUE4Editor-MessageLog.so
-rw-r--r--. 1 root root  867K Mar  6 17:38 libUE4Editor-MessageLog.sym
-rw-r--r--. 1 root root  4.2M Mar  6 17:36 libUE4Editor-Messaging.debug
-rwxr-xr-x. 1 root root  514K Mar  6 17:36 libUE4Editor-Messaging.so
-rw-r--r--. 1 root root  310K Mar  6 17:36 libUE4Editor-Messaging.sym
-rw-r--r--. 1 root root   97K Mar  6 17:35 libUE4Editor-MessagingCommon.debug
-rwxr-xr-x. 1 root root  232K Mar  6 17:35 libUE4Editor-MessagingCommon.so
-rw-r--r--. 1 root root   48K Mar  6 17:35 libUE4Editor-MessagingCommon.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:35 libUE4Editor-MessagingRpc.debug
-rwxr-xr-x. 1 root root  348K Mar  6 17:35 libUE4Editor-MessagingRpc.so
-rw-r--r--. 1 root root  144K Mar  6 17:35 libUE4Editor-MessagingRpc.sym
-rw-r--r--. 1 root root  4.8M Mar  6 17:46 libUE4Editor-ModuleUI.debug
-rwxr-xr-x. 1 root root  425K Mar  6 17:46 libUE4Editor-ModuleUI.so
-rw-r--r--. 1 root root  283K Mar  6 17:46 libUE4Editor-ModuleUI.sym
-rw-r--r--. 1 root root  4.3M Mar  6 17:41 libUE4Editor-MoviePlayer.debug
-rwxr-xr-x. 1 root root  330K Mar  6 17:41 libUE4Editor-MoviePlayer.so
-rw-r--r--. 1 root root  169K Mar  6 17:41 libUE4Editor-MoviePlayer.sym
-rw-r--r--. 1 root root   37M Mar  6 17:39 libUE4Editor-MovieScene.debug
-rwxr-xr-x. 1 root root  3.4M Mar  6 17:39 libUE4Editor-MovieScene.so
-rw-r--r--. 1 root root  3.0M Mar  6 17:39 libUE4Editor-MovieScene.sym
-rw-r--r--. 1 root root  6.8M Mar  6 17:40 libUE4Editor-MovieSceneCapture.debug
-rwxr-xr-x. 1 root root  741K Mar  6 17:40 libUE4Editor-MovieSceneCapture.so
-rw-r--r--. 1 root root  409K Mar  6 17:40 libUE4Editor-MovieSceneCapture.sym
-rw-r--r--. 1 root root  3.7M Mar  6 17:41 libUE4Editor-MovieSceneCaptureDialog.debug
-rwxr-xr-x. 1 root root  327K Mar  6 17:41 libUE4Editor-MovieSceneCaptureDialog.so
-rw-r--r--. 1 root root  188K Mar  6 17:41 libUE4Editor-MovieSceneCaptureDialog.sym
-rw-r--r--. 1 root root   77M Mar  6 17:46 libUE4Editor-MovieSceneTools.debug
-rwxr-xr-x. 1 root root  7.8M Mar  6 17:40 libUE4Editor-MovieSceneTools.so
-rw-r--r--. 1 root root  6.2M Mar  6 17:46 libUE4Editor-MovieSceneTools.sym
-rw-r--r--. 1 root root   40M Mar  6 17:39 libUE4Editor-MovieSceneTracks.debug
-rwxr-xr-x. 1 root root  3.8M Mar  6 17:39 libUE4Editor-MovieSceneTracks.so
-rw-r--r--. 1 root root  3.3M Mar  6 17:39 libUE4Editor-MovieSceneTracks.sym
-rw-r--r--. 1 root root   26M Mar  6 17:39 libUE4Editor-NavigationSystem.debug
-rwxr-xr-x. 1 root root  2.9M Mar  6 17:39 libUE4Editor-NavigationSystem.so
-rw-r--r--. 1 root root  1.7M Mar  6 17:39 libUE4Editor-NavigationSystem.sym
-rw-r--r--. 1 root root  3.0M Mar  6 17:39 libUE4Editor-Navmesh.debug
-rwxr-xr-x. 1 root root  738K Mar  6 17:39 libUE4Editor-Navmesh.so
-rw-r--r--. 1 root root  462K Mar  6 17:39 libUE4Editor-Navmesh.sym
-rw-r--r--. 1 root root   98K Mar  6 17:35 libUE4Editor-NetCommon.debug
-rwxr-xr-x. 1 root root  232K Mar  6 17:35 libUE4Editor-NetCommon.so
-rw-r--r--. 1 root root   48K Mar  6 17:35 libUE4Editor-NetCommon.sym
-rw-r--r--. 1 root root  3.0M Mar  6 17:35 libUE4Editor-NetCore.debug
-rwxr-xr-x. 1 root root  207K Mar  6 17:35 libUE4Editor-NetCore.so
-rw-r--r--. 1 root root  166K Mar  6 17:35 libUE4Editor-NetCore.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:41 libUE4Editor-NetworkFile.debug
-rwxr-xr-x. 1 root root  377K Mar  6 17:41 libUE4Editor-NetworkFile.so
-rw-r--r--. 1 root root  150K Mar  6 17:41 libUE4Editor-NetworkFile.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:44 libUE4Editor-NetworkFileSystem.debug
-rwxr-xr-x. 1 root root  163K Mar  6 17:44 libUE4Editor-NetworkFileSystem.so
-rw-r--r--. 1 root root  130K Mar  6 17:44 libUE4Editor-NetworkFileSystem.sym
-rw-r--r--. 1 root root  560K Mar  6 17:37 libUE4Editor-NetworkReplayStreaming.debug
-rwxr-xr-x. 1 root root   31K Mar  6 17:37 libUE4Editor-NetworkReplayStreaming.so
-rw-r--r--. 1 root root   18K Mar  6 17:37 libUE4Editor-NetworkReplayStreaming.sym
-rw-r--r--. 1 root root  534K Mar  6 17:35 libUE4Editor-Networking.debug
-rwxr-xr-x. 1 root root  256K Mar  6 17:35 libUE4Editor-Networking.so
-rw-r--r--. 1 root root   62K Mar  6 17:35 libUE4Editor-Networking.sym
-rw-r--r--. 1 root root  2.8M Mar  6 17:44 libUE4Editor-NewLevelDialog.debug
-rwxr-xr-x. 1 root root  203K Mar  6 17:44 libUE4Editor-NewLevelDialog.so
-rw-r--r--. 1 root root   99K Mar  6 17:44 libUE4Editor-NewLevelDialog.sym
-rw-r--r--. 1 root root  677K Mar  6 17:46 libUE4Editor-NonRealtimeAudioRenderer.debug
-rwxr-xr-x. 1 root root   30K Mar  6 17:40 libUE4Editor-NonRealtimeAudioRenderer.so
-rw-r--r--. 1 root root   17K Mar  6 17:46 libUE4Editor-NonRealtimeAudioRenderer.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:46 libUE4Editor-NullDrv.debug
-rwxr-xr-x. 1 root root  327K Mar  6 17:46 libUE4Editor-NullDrv.so
-rw-r--r--. 1 root root  108K Mar  6 17:46 libUE4Editor-NullDrv.sym
-rw-r--r--. 1 root root  802K Mar  6 17:46 libUE4Editor-NullInstallBundleManager.debug
-rwxr-xr-x. 1 root root  248K Mar  6 17:46 libUE4Editor-NullInstallBundleManager.so
-rw-r--r--. 1 root root   66K Mar  6 17:46 libUE4Editor-NullInstallBundleManager.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:46 libUE4Editor-NullNetworkReplayStreaming.debug
-rwxr-xr-x. 1 root root  241K Mar  6 17:46 libUE4Editor-NullNetworkReplayStreaming.so
-rw-r--r--. 1 root root  175K Mar  6 17:46 libUE4Editor-NullNetworkReplayStreaming.sym
-rw-r--r--. 1 root root   24M Mar  6 17:44 libUE4Editor-OpenGLDrv.debug
-rwxr-xr-x. 1 root root  3.4M Mar  6 17:44 libUE4Editor-OpenGLDrv.so
-rw-r--r--. 1 root root  2.5M Mar  6 17:44 libUE4Editor-OpenGLDrv.sym
-rw-r--r--. 1 root root  8.2M Mar  6 17:46 libUE4Editor-OutputLog.debug
-rwxr-xr-x. 1 root root  1.3M Mar  6 17:46 libUE4Editor-OutputLog.so
-rw-r--r--. 1 root root  712K Mar  6 17:46 libUE4Editor-OutputLog.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:41 libUE4Editor-Overlay.debug
-rwxr-xr-x. 1 root root   82K Mar  6 17:41 libUE4Editor-Overlay.so
-rw-r--r--. 1 root root   39K Mar  6 17:41 libUE4Editor-Overlay.sym
-rw-r--r--. 1 root root  1.4M Mar  6 17:46 libUE4Editor-OverlayEditor.debug
-rwxr-xr-x. 1 root root  819K Mar  6 17:46 libUE4Editor-OverlayEditor.so
-rw-r--r--. 1 root root  253K Mar  6 17:46 libUE4Editor-OverlayEditor.sym
-rw-r--r--. 1 root root  6.2M Mar  6 17:41 libUE4Editor-PIEPreviewDeviceProfileSelector.debug
-rwxr-xr-x. 1 root root  574K Mar  6 17:41 libUE4Editor-PIEPreviewDeviceProfileSelector.so
-rw-r--r--. 1 root root  327K Mar  6 17:41 libUE4Editor-PIEPreviewDeviceProfileSelector.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:40 libUE4Editor-PIEPreviewDeviceSpecification.debug
-rwxr-xr-x. 1 root root  313K Mar  6 17:40 libUE4Editor-PIEPreviewDeviceSpecification.so
-rw-r--r--. 1 root root  120K Mar  6 17:40 libUE4Editor-PIEPreviewDeviceSpecification.sym
-rw-r--r--. 1 root root  9.3M Mar  6 17:46 libUE4Editor-PListEditor.debug
-rwxr-xr-x. 1 root root  1.5M Mar  6 17:46 libUE4Editor-PListEditor.so
-rw-r--r--. 1 root root  758K Mar  6 17:46 libUE4Editor-PListEditor.sym
-rw-r--r--. 1 root root  6.3M Mar  6 17:46 libUE4Editor-PackagesDialog.debug
-rwxr-xr-x. 1 root root  576K Mar  6 17:46 libUE4Editor-PackagesDialog.so
-rw-r--r--. 1 root root  360K Mar  6 17:46 libUE4Editor-PackagesDialog.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:35 libUE4Editor-PacketHandler.debug
-rwxr-xr-x. 1 root root  101K Mar  6 17:35 libUE4Editor-PacketHandler.so
-rw-r--r--. 1 root root   55K Mar  6 17:35 libUE4Editor-PacketHandler.sym
-rw-r--r--. 1 root root  5.0M Mar  6 17:35 libUE4Editor-PakFile.debug
-rwxr-xr-x. 1 root root  496K Mar  6 17:35 libUE4Editor-PakFile.so
-rw-r--r--. 1 root root  402K Mar  6 17:35 libUE4Editor-PakFile.sym
-rw-r--r--. 1 root root  6.6M Mar  6 17:35 libUE4Editor-PakFileUtilities.debug
-rwxr-xr-x. 1 root root  547K Mar  6 17:35 libUE4Editor-PakFileUtilities.so
-rw-r--r--. 1 root root  455K Mar  6 17:35 libUE4Editor-PakFileUtilities.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:37 libUE4Editor-PerfCounters.debug
-rwxr-xr-x. 1 root root  106K Mar  6 17:37 libUE4Editor-PerfCounters.so
-rw-r--r--. 1 root root   78K Mar  6 17:37 libUE4Editor-PerfCounters.sym
-rw-r--r--. 1 root root  147M Mar  6 17:41 libUE4Editor-Persona.debug
-rwxr-xr-x. 1 root root   14M Mar  6 17:41 libUE4Editor-Persona.so
-rw-r--r--. 1 root root  9.4M Mar  6 17:41 libUE4Editor-Persona.sym
-rw-r--r--. 1 root root  4.8M Mar  6 17:44 libUE4Editor-PhysXCooking.debug
-rwxr-xr-x. 1 root root  944K Mar  6 17:44 libUE4Editor-PhysXCooking.so
-rw-r--r--. 1 root root  538K Mar  6 17:44 libUE4Editor-PhysXCooking.sym
-rw-r--r--. 1 root root   24M Mar  6 17:46 libUE4Editor-PhysicsAssetEditor.debug
-rwxr-xr-x. 1 root root  2.5M Mar  6 17:46 libUE4Editor-PhysicsAssetEditor.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:46 libUE4Editor-PhysicsAssetEditor.sym
-rw-r--r--. 1 root root   98M Mar  6 17:38 libUE4Editor-PhysicsCore.debug
-rwxr-xr-x. 1 root root  9.3M Mar  6 17:38 libUE4Editor-PhysicsCore.so
-rw-r--r--. 1 root root  8.0M Mar  6 17:38 libUE4Editor-PhysicsCore.sym
-rw-r--r--. 1 root root  3.2M Mar  6 17:39 libUE4Editor-PinnedCommandList.debug
-rwxr-xr-x. 1 root root  231K Mar  6 17:39 libUE4Editor-PinnedCommandList.so
-rw-r--r--. 1 root root  144K Mar  6 17:39 libUE4Editor-PinnedCommandList.sym
-rw-r--r--. 1 root root   10M Mar  6 17:40 libUE4Editor-PixelInspectorModule.debug
-rwxr-xr-x. 1 root root  672K Mar  6 17:40 libUE4Editor-PixelInspectorModule.so
-rw-r--r--. 1 root root  389K Mar  6 17:40 libUE4Editor-PixelInspectorModule.sym
-rw-r--r--. 1 root root  7.7M Mar  6 17:40 libUE4Editor-PlacementMode.debug
-rwxr-xr-x. 1 root root  659K Mar  6 17:40 libUE4Editor-PlacementMode.so
-rw-r--r--. 1 root root  442K Mar  6 17:40 libUE4Editor-PlacementMode.sym
-rw-r--r--. 1 root root  2.5M Mar  6 17:46 libUE4Editor-PluginWarden.debug
-rwxr-xr-x. 1 root root  707K Mar  6 17:44 libUE4Editor-PluginWarden.so
-rw-r--r--. 1 root root  272K Mar  6 17:46 libUE4Editor-PluginWarden.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:44 libUE4Editor-PortalMessages.debug
-rwxr-xr-x. 1 root root   97K Mar  6 17:44 libUE4Editor-PortalMessages.so
-rw-r--r--. 1 root root  117K Mar  6 17:44 libUE4Editor-PortalMessages.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:46 libUE4Editor-PortalProxies.debug
-rwxr-xr-x. 1 root root  307K Mar  6 17:46 libUE4Editor-PortalProxies.so
-rw-r--r--. 1 root root  111K Mar  6 17:46 libUE4Editor-PortalProxies.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:37 libUE4Editor-PortalRpc.debug
-rwxr-xr-x. 1 root root   86K Mar  6 17:37 libUE4Editor-PortalRpc.so
-rw-r--r--. 1 root root   57K Mar  6 17:37 libUE4Editor-PortalRpc.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:35 libUE4Editor-PortalServices.debug
-rwxr-xr-x. 1 root root  275K Mar  6 17:35 libUE4Editor-PortalServices.so
-rw-r--r--. 1 root root   85K Mar  6 17:35 libUE4Editor-PortalServices.sym
-rw-r--r--. 1 root root  5.0M Mar  6 17:41 libUE4Editor-PreLoadScreen.debug
-rwxr-xr-x. 1 root root  327K Mar  6 17:41 libUE4Editor-PreLoadScreen.so
-rw-r--r--. 1 root root  209K Mar  6 17:41 libUE4Editor-PreLoadScreen.sym
-rw-r--r--. 1 root root   34M Mar  6 17:43 libUE4Editor-Profiler.debug
-rwxr-xr-x. 1 root root  3.3M Mar  6 17:43 libUE4Editor-Profiler.so
-rw-r--r--. 1 root root  2.5M Mar  6 17:43 libUE4Editor-Profiler.sym
-rw-r--r--. 1 root root  4.4M Mar  6 17:41 libUE4Editor-ProfilerClient.debug
-rwxr-xr-x. 1 root root  288K Mar  6 17:41 libUE4Editor-ProfilerClient.so
-rw-r--r--. 1 root root  235K Mar  6 17:41 libUE4Editor-ProfilerClient.sym
-rw-r--r--. 1 root root  997K Mar  6 17:41 libUE4Editor-ProfilerMessages.debug
-rwxr-xr-x. 1 root root  315K Mar  6 17:41 libUE4Editor-ProfilerMessages.so
-rw-r--r--. 1 root root  144K Mar  6 17:41 libUE4Editor-ProfilerMessages.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:46 libUE4Editor-ProfilerService.debug
-rwxr-xr-x. 1 root root  164K Mar  6 17:46 libUE4Editor-ProfilerService.so
-rw-r--r--. 1 root root  116K Mar  6 17:46 libUE4Editor-ProfilerService.sym
-rw-r--r--. 1 root root   31M Mar  6 17:47 libUE4Editor-ProjectLauncher.debug
-rwxr-xr-x. 1 root root  3.7M Mar  6 17:47 libUE4Editor-ProjectLauncher.so
-rw-r--r--. 1 root root  2.6M Mar  6 17:47 libUE4Editor-ProjectLauncher.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:46 libUE4Editor-ProjectSettingsViewer.debug
-rwxr-xr-x. 1 root root  576K Mar  6 17:46 libUE4Editor-ProjectSettingsViewer.so
-rw-r--r--. 1 root root  200K Mar  6 17:46 libUE4Editor-ProjectSettingsViewer.sym
-rw-r--r--. 1 root root  2.2M Mar  6 17:44 libUE4Editor-ProjectTargetPlatformEditor.debug
-rwxr-xr-x. 1 root root  181K Mar  6 17:44 libUE4Editor-ProjectTargetPlatformEditor.so
-rw-r--r--. 1 root root   93K Mar  6 17:44 libUE4Editor-ProjectTargetPlatformEditor.sym
-rw-r--r--. 1 root root  5.6M Mar  6 17:35 libUE4Editor-Projects.debug
-rwxr-xr-x. 1 root root  478K Mar  6 17:35 libUE4Editor-Projects.so
-rw-r--r--. 1 root root  342K Mar  6 17:35 libUE4Editor-Projects.sym
-rw-r--r--. 1 root root  2.4M Mar  6 17:37 libUE4Editor-PropertyAccess.debug
-rwxr-xr-x. 1 root root  197K Mar  6 17:37 libUE4Editor-PropertyAccess.so
-rw-r--r--. 1 root root  154K Mar  6 17:37 libUE4Editor-PropertyAccess.sym
-rw-r--r--. 1 root root   98M Mar  6 17:46 libUE4Editor-PropertyEditor.debug
-rwxr-xr-x. 1 root root  8.3M Mar  6 17:40 libUE4Editor-PropertyEditor.so
-rw-r--r--. 1 root root  5.8M Mar  6 17:46 libUE4Editor-PropertyEditor.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:36 libUE4Editor-PropertyPath.debug
-rwxr-xr-x. 1 root root  308K Mar  6 17:36 libUE4Editor-PropertyPath.so
-rw-r--r--. 1 root root  108K Mar  6 17:36 libUE4Editor-PropertyPath.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:39 libUE4Editor-QuadricMeshReduction.debug
-rwxr-xr-x. 1 root root  139K Mar  6 17:39 libUE4Editor-QuadricMeshReduction.so
-rw-r--r--. 1 root root  134K Mar  6 17:39 libUE4Editor-QuadricMeshReduction.sym
-rw-r--r--. 1 root root   12M Mar  6 17:35 libUE4Editor-RHI.debug
-rwxr-xr-x. 1 root root  1.3M Mar  6 17:35 libUE4Editor-RHI.so
-rw-r--r--. 1 root root  884K Mar  6 17:35 libUE4Editor-RHI.sym
-rw-r--r--. 1 root root  787K Mar  6 17:35 libUE4Editor-RSA.debug
-rwxr-xr-x. 1 root root  4.0M Mar  6 17:35 libUE4Editor-RSA.so
-rw-r--r--. 1 root root  339K Mar  6 17:35 libUE4Editor-RSA.sym
-rw-r--r--. 1 root root  654K Mar  6 17:35 libUE4Editor-RawMesh.debug
-rwxr-xr-x. 1 root root  269K Mar  6 17:35 libUE4Editor-RawMesh.so
-rw-r--r--. 1 root root   75K Mar  6 17:35 libUE4Editor-RawMesh.sym
-rw-r--r--. 1 root root  3.0M Mar  6 17:46 libUE4Editor-RealtimeProfiler.debug
-rwxr-xr-x. 1 root root  250K Mar  6 17:46 libUE4Editor-RealtimeProfiler.so
-rw-r--r--. 1 root root  131K Mar  6 17:46 libUE4Editor-RealtimeProfiler.sym
-rw-r--r--. 1 root root  572K Mar  6 17:46 libUE4Editor-ReliabilityHandlerComponent.debug
-rwxr-xr-x. 1 root root  246K Mar  6 17:35 libUE4Editor-ReliabilityHandlerComponent.so
-rw-r--r--. 1 root root   59K Mar  6 17:46 libUE4Editor-ReliabilityHandlerComponent.sym
-rw-r--r--. 1 root root  869K Mar  6 17:42 libUE4Editor-RemoteImportMessaging.debug
-rwxr-xr-x. 1 root root  286K Mar  6 17:42 libUE4Editor-RemoteImportMessaging.so
-rw-r--r--. 1 root root  107K Mar  6 17:42 libUE4Editor-RemoteImportMessaging.sym
-rw-r--r--. 1 root root   29M Mar  6 17:36 libUE4Editor-RenderCore.debug
-rwxr-xr-x. 1 root root  2.9M Mar  6 17:36 libUE4Editor-RenderCore.so
-rw-r--r--. 1 root root  2.2M Mar  6 17:36 libUE4Editor-RenderCore.sym
-rw-r--r--. 1 root root  168M Mar  6 17:39 libUE4Editor-Renderer.debug
-rwxr-xr-x. 1 root root   16M Mar  6 17:39 libUE4Editor-Renderer.so
-rw-r--r--. 1 root root   16M Mar  6 17:39 libUE4Editor-Renderer.sym
-rw-r--r--. 1 root root  5.5M Mar  6 17:40 libUE4Editor-RigVM.debug
-rwxr-xr-x. 1 root root  813K Mar  6 17:40 libUE4Editor-RigVM.so
-rw-r--r--. 1 root root  518K Mar  6 17:40 libUE4Editor-RigVM.sym
-rw-r--r--. 1 root root   14M Mar  6 17:41 libUE4Editor-RigVMDeveloper.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:41 libUE4Editor-RigVMDeveloper.so
-rw-r--r--. 1 root root  1.2M Mar  6 17:41 libUE4Editor-RigVMDeveloper.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:46 libUE4Editor-RuntimeAssetCache.debug
-rwxr-xr-x. 1 root root  429K Mar  6 17:46 libUE4Editor-RuntimeAssetCache.so
-rw-r--r--. 1 root root  165K Mar  6 17:46 libUE4Editor-RuntimeAssetCache.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:35 libUE4Editor-SSL.debug
-rwxr-xr-x. 1 root root  4.0M Mar  6 17:35 libUE4Editor-SSL.so
-rw-r--r--. 1 root root  370K Mar  6 17:35 libUE4Editor-SSL.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:41 libUE4Editor-SandboxFile.debug
-rwxr-xr-x. 1 root root  301K Mar  6 17:41 libUE4Editor-SandboxFile.so
-rw-r--r--. 1 root root   92K Mar  6 17:41 libUE4Editor-SandboxFile.sym
-rw-r--r--. 1 root root  5.8M Mar  6 17:46 libUE4Editor-SaveGameNetworkReplayStreaming.debug
-rwxr-xr-x. 1 root root  627K Mar  6 17:46 libUE4Editor-SaveGameNetworkReplayStreaming.so
-rw-r--r--. 1 root root  471K Mar  6 17:46 libUE4Editor-SaveGameNetworkReplayStreaming.sym
-rw-r--r--. 1 root root  1.7M Mar  6 17:41 libUE4Editor-SceneDepthPickerMode.debug
-rwxr-xr-x. 1 root root   61K Mar  6 17:41 libUE4Editor-SceneDepthPickerMode.so
-rw-r--r--. 1 root root   30K Mar  6 17:41 libUE4Editor-SceneDepthPickerMode.sym
-rw-r--r--. 1 root root   23M Mar  6 17:39 libUE4Editor-SceneOutliner.debug
-rwxr-xr-x. 1 root root  2.1M Mar  6 17:39 libUE4Editor-SceneOutliner.so
-rw-r--r--. 1 root root  1.6M Mar  6 17:39 libUE4Editor-SceneOutliner.sym
-rw-r--r--. 1 root root  7.7M Mar  6 17:42 libUE4Editor-ScreenShotComparison.debug
-rwxr-xr-x. 1 root root  771K Mar  6 17:42 libUE4Editor-ScreenShotComparison.so
-rw-r--r--. 1 root root  459K Mar  6 17:42 libUE4Editor-ScreenShotComparison.sym
-rw-r--r--. 1 root root  3.6M Mar  6 17:40 libUE4Editor-ScreenShotComparisonTools.debug
-rwxr-xr-x. 1 root root  311K Mar  6 17:40 libUE4Editor-ScreenShotComparisonTools.so
-rw-r--r--. 1 root root  197K Mar  6 17:40 libUE4Editor-ScreenShotComparisonTools.sym
-rw-r--r--. 1 root root  768K Mar  6 17:43 libUE4Editor-ScriptDisassembler.debug
-rwxr-xr-x. 1 root root  268K Mar  6 17:43 libUE4Editor-ScriptDisassembler.so
-rw-r--r--. 1 root root   71K Mar  6 17:43 libUE4Editor-ScriptDisassembler.sym
-rw-r--r--. 1 root root   20M Mar  6 17:40 libUE4Editor-SequenceRecorder.debug
-rwxr-xr-x. 1 root root  1.8M Mar  6 17:40 libUE4Editor-SequenceRecorder.so
-rw-r--r--. 1 root root  1.2M Mar  6 17:40 libUE4Editor-SequenceRecorder.sym
-rw-r--r--. 1 root root  1.7M Mar  6 17:46 libUE4Editor-SequenceRecorderSections.debug
-rwxr-xr-x. 1 root root   90K Mar  6 17:46 libUE4Editor-SequenceRecorderSections.so
-rw-r--r--. 1 root root   47K Mar  6 17:46 libUE4Editor-SequenceRecorderSections.sym
-rw-r--r--. 1 root root   92M Mar  6 17:46 libUE4Editor-Sequencer.debug
-rwxr-xr-x. 1 root root  9.1M Mar  6 17:40 libUE4Editor-Sequencer.so
-rw-r--r--. 1 root root  7.2M Mar  6 17:46 libUE4Editor-Sequencer.sym
-rw-r--r--. 1 root root  3.6M Mar  6 17:39 libUE4Editor-SequencerWidgets.debug
-rwxr-xr-x. 1 root root  283K Mar  6 17:39 libUE4Editor-SequencerWidgets.so
-rw-r--r--. 1 root root  132K Mar  6 17:39 libUE4Editor-SequencerWidgets.sym
-rw-r--r--. 1 root root  5.7M Mar  6 17:39 libUE4Editor-Serialization.debug
-rwxr-xr-x. 1 root root  495K Mar  6 17:39 libUE4Editor-Serialization.so
-rw-r--r--. 1 root root  408K Mar  6 17:39 libUE4Editor-Serialization.sym
-rw-r--r--. 1 root root  715K Mar  6 17:39 libUE4Editor-SerializedRecorderInterface.debug
-rwxr-xr-x. 1 root root   15K Mar  6 17:39 libUE4Editor-SerializedRecorderInterface.so
-rw-r--r--. 1 root root  2.6K Mar  6 17:39 libUE4Editor-SerializedRecorderInterface.sym
-rw-r--r--. 1 root root   19M Mar  6 17:44 libUE4Editor-SessionFrontend.debug
-rwxr-xr-x. 1 root root  2.0M Mar  6 17:44 libUE4Editor-SessionFrontend.so
-rw-r--r--. 1 root root  1.5M Mar  6 17:44 libUE4Editor-SessionFrontend.sym
-rw-r--r--. 1 root root  780K Mar  6 17:39 libUE4Editor-SessionMessages.debug
-rwxr-xr-x. 1 root root  277K Mar  6 17:39 libUE4Editor-SessionMessages.so
-rw-r--r--. 1 root root   93K Mar  6 17:39 libUE4Editor-SessionMessages.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:40 libUE4Editor-SessionServices.debug
-rwxr-xr-x. 1 root root  157K Mar  6 17:40 libUE4Editor-SessionServices.so
-rw-r--r--. 1 root root  112K Mar  6 17:40 libUE4Editor-SessionServices.sym
-rw-r--r--. 1 root root  1.4M Mar  6 17:38 libUE4Editor-Settings.debug
-rwxr-xr-x. 1 root root  299K Mar  6 17:38 libUE4Editor-Settings.so
-rw-r--r--. 1 root root  102K Mar  6 17:38 libUE4Editor-Settings.sym
-rw-r--r--. 1 root root  3.9M Mar  6 17:41 libUE4Editor-SettingsEditor.debug
-rwxr-xr-x. 1 root root  357K Mar  6 17:41 libUE4Editor-SettingsEditor.so
-rw-r--r--. 1 root root  208K Mar  6 17:41 libUE4Editor-SettingsEditor.sym
-rw-r--r--. 1 root root  5.5M Mar  6 17:41 libUE4Editor-ShaderCompilerCommon.debug
-rwxr-xr-x. 1 root root  490K Mar  6 17:41 libUE4Editor-ShaderCompilerCommon.so
-rw-r--r--. 1 root root  390K Mar  6 17:41 libUE4Editor-ShaderCompilerCommon.sym
-rw-r--r--. 1 root root   16M Mar  6 17:46 libUE4Editor-ShaderFormatOpenGL.debug
-rwxr-xr-x. 1 root root  3.1M Mar  6 17:46 libUE4Editor-ShaderFormatOpenGL.so
-rw-r--r--. 1 root root  2.2M Mar  6 17:46 libUE4Editor-ShaderFormatOpenGL.sym
-rw-r--r--. 1 root root  9.9M Mar  6 17:41 libUE4Editor-ShaderFormatVectorVM.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:41 libUE4Editor-ShaderFormatVectorVM.so
-rw-r--r--. 1 root root 1015K Mar  6 17:41 libUE4Editor-ShaderFormatVectorVM.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:41 libUE4Editor-ShaderPreprocessor.debug
-rwxr-xr-x. 1 root root  421K Mar  6 17:41 libUE4Editor-ShaderPreprocessor.so
-rw-r--r--. 1 root root  100K Mar  6 17:41 libUE4Editor-ShaderPreprocessor.sym
-rw-r--r--. 1 root root  3.3M Mar  6 17:40 libUE4Editor-SharedSettingsWidgets.debug
-rwxr-xr-x. 1 root root  302K Mar  6 17:40 libUE4Editor-SharedSettingsWidgets.so
-rw-r--r--. 1 root root  159K Mar  6 17:40 libUE4Editor-SharedSettingsWidgets.sym
-rw-r--r--. 1 root root  5.4M Mar  6 17:35 libUE4Editor-SignalProcessing.debug
-rwxr-xr-x. 1 root root  4.1M Mar  6 17:35 libUE4Editor-SignalProcessing.so
-rw-r--r--. 1 root root  623K Mar  6 17:35 libUE4Editor-SignalProcessing.sym
-rw-r--r--. 1 root root  9.4M Mar  6 17:42 libUE4Editor-SkeletalMeshEditor.debug
-rwxr-xr-x. 1 root root  808K Mar  6 17:42 libUE4Editor-SkeletalMeshEditor.so
-rw-r--r--. 1 root root  513K Mar  6 17:42 libUE4Editor-SkeletalMeshEditor.sym
-rw-r--r--. 1 root root  5.7M Mar  6 17:39 libUE4Editor-SkeletalMeshUtilitiesCommon.debug
-rwxr-xr-x. 1 root root  353K Mar  6 17:39 libUE4Editor-SkeletalMeshUtilitiesCommon.so
-rw-r--r--. 1 root root  337K Mar  6 17:39 libUE4Editor-SkeletalMeshUtilitiesCommon.sym
-rw-r--r--. 1 root root   18M Mar  6 17:41 libUE4Editor-SkeletonEditor.debug
-rwxr-xr-x. 1 root root  1.8M Mar  6 17:41 libUE4Editor-SkeletonEditor.so
-rw-r--r--. 1 root root  1.2M Mar  6 17:41 libUE4Editor-SkeletonEditor.sym
-rw-r--r--. 1 root root  477K Mar  6 17:46 libUE4Editor-SlackIntegrations.debug
-rwxr-xr-x. 1 root root  246K Mar  6 17:46 libUE4Editor-SlackIntegrations.so
-rw-r--r--. 1 root root   62K Mar  6 17:46 libUE4Editor-SlackIntegrations.sym
-rw-r--r--. 1 root root   64M Mar  6 17:36 libUE4Editor-Slate.debug
-rwxr-xr-x. 1 root root  6.6M Mar  6 17:36 libUE4Editor-Slate.so
-rw-r--r--. 1 root root  4.1M Mar  6 17:36 libUE4Editor-Slate.sym
-rw-r--r--. 1 root root   25M Mar  6 17:35 libUE4Editor-SlateCore.debug
-rwxr-xr-x. 1 root root  5.2M Mar  6 17:35 libUE4Editor-SlateCore.so
-rw-r--r--. 1 root root  2.2M Mar  6 17:35 libUE4Editor-SlateCore.sym
-rw-r--r--. 1 root root  7.2M Mar  6 17:46 libUE4Editor-SlateFileDialogs.debug
-rwxr-xr-x. 1 root root  739K Mar  6 17:46 libUE4Editor-SlateFileDialogs.so
-rw-r--r--. 1 root root  489K Mar  6 17:46 libUE4Editor-SlateFileDialogs.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:46 libUE4Editor-SlateNullRenderer.debug
-rwxr-xr-x. 1 root root  281K Mar  6 17:46 libUE4Editor-SlateNullRenderer.so
-rw-r--r--. 1 root root   77K Mar  6 17:46 libUE4Editor-SlateNullRenderer.sym
-rw-r--r--. 1 root root   11M Mar  6 17:44 libUE4Editor-SlateRHIRenderer.debug
-rwxr-xr-x. 1 root root  984K Mar  6 17:44 libUE4Editor-SlateRHIRenderer.so
-rw-r--r--. 1 root root  708K Mar  6 17:44 libUE4Editor-SlateRHIRenderer.sym
-rw-r--r--. 1 root root   31M Mar  6 17:44 libUE4Editor-SlateReflector.debug
-rwxr-xr-x. 1 root root  3.1M Mar  6 17:44 libUE4Editor-SlateReflector.so
-rw-r--r--. 1 root root  2.3M Mar  6 17:44 libUE4Editor-SlateReflector.sym
-rw-r--r--. 1 root root  2.4M Mar  6 17:35 libUE4Editor-Sockets.debug
-rwxr-xr-x. 1 root root  227K Mar  6 17:35 libUE4Editor-Sockets.so
-rw-r--r--. 1 root root  173K Mar  6 17:35 libUE4Editor-Sockets.sym
-rw-r--r--. 1 root root  801K Mar  6 17:46 libUE4Editor-SoundFieldRendering.debug
-rwxr-xr-x. 1 root root  266K Mar  6 17:41 libUE4Editor-SoundFieldRendering.so
-rw-r--r--. 1 root root   72K Mar  6 17:46 libUE4Editor-SoundFieldRendering.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:39 libUE4Editor-SourceCodeAccess.debug
-rwxr-xr-x. 1 root root   59K Mar  6 17:39 libUE4Editor-SourceCodeAccess.so
-rw-r--r--. 1 root root   36K Mar  6 17:39 libUE4Editor-SourceCodeAccess.sym
-rw-r--r--. 1 root root  5.6M Mar  6 17:46 libUE4Editor-SourceControl.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:37 libUE4Editor-SourceControl.so
-rw-r--r--. 1 root root  456K Mar  6 17:46 libUE4Editor-SourceControl.sym
-rw-r--r--. 1 root root   14M Mar  6 17:40 libUE4Editor-SourceControlWindows.debug
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:40 libUE4Editor-SourceControlWindows.so
-rw-r--r--. 1 root root  993K Mar  6 17:40 libUE4Editor-SourceControlWindows.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:41 libUE4Editor-StageDataCore.debug
-rwxr-xr-x. 1 root root  329K Mar  6 17:41 libUE4Editor-StageDataCore.so
-rw-r--r--. 1 root root  149K Mar  6 17:41 libUE4Editor-StageDataCore.sym
-rw-r--r--. 1 root root  9.0M Mar  6 17:41 libUE4Editor-StandaloneRenderer.debug
-rwxr-xr-x. 1 root root  1.8M Mar  6 17:41 libUE4Editor-StandaloneRenderer.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:41 libUE4Editor-StandaloneRenderer.sym
-rw-r--r--. 1 root root  6.3M Mar  6 17:36 libUE4Editor-StaticMeshDescription.debug
-rwxr-xr-x. 1 root root  470K Mar  6 17:36 libUE4Editor-StaticMeshDescription.so
-rw-r--r--. 1 root root  347K Mar  6 17:36 libUE4Editor-StaticMeshDescription.sym
-rw-r--r--. 1 root root   24M Mar  6 17:42 libUE4Editor-StaticMeshEditor.debug
-rwxr-xr-x. 1 root root  2.5M Mar  6 17:42 libUE4Editor-StaticMeshEditor.so
-rw-r--r--. 1 root root  1.6M Mar  6 17:42 libUE4Editor-StaticMeshEditor.sym
-rw-r--r--. 1 root root  8.8M Mar  6 17:39 libUE4Editor-StatsViewer.debug
-rwxr-xr-x. 1 root root  852K Mar  6 17:39 libUE4Editor-StatsViewer.so
-rw-r--r--. 1 root root  525K Mar  6 17:39 libUE4Editor-StatsViewer.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:46 libUE4Editor-Stomp.debug
-rwxr-xr-x. 1 root root  361K Mar  6 17:46 libUE4Editor-Stomp.so
-rw-r--r--. 1 root root  159K Mar  6 17:46 libUE4Editor-Stomp.sym
-rw-r--r--. 1 root root  928K Mar  6 17:42 libUE4Editor-StreamingFile.debug
-rwxr-xr-x. 1 root root   78K Mar  6 17:42 libUE4Editor-StreamingFile.so
-rw-r--r--. 1 root root   44K Mar  6 17:42 libUE4Editor-StreamingFile.sym
-rw-r--r--. 1 root root  2.4M Mar  6 17:46 libUE4Editor-StreamingPauseRendering.debug
-rwxr-xr-x. 1 root root   99K Mar  6 17:46 libUE4Editor-StreamingPauseRendering.so
-rw-r--r--. 1 root root   42K Mar  6 17:46 libUE4Editor-StreamingPauseRendering.sym
-rw-r--r--. 1 root root  8.1M Mar  6 17:46 libUE4Editor-StringTableEditor.debug
-rwxr-xr-x. 1 root root  1.2M Mar  6 17:46 libUE4Editor-StringTableEditor.so
-rw-r--r--. 1 root root  619K Mar  6 17:46 libUE4Editor-StringTableEditor.sym
-rw-r--r--. 1 root root  8.9M Mar  6 17:46 libUE4Editor-StructViewer.debug
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:46 libUE4Editor-StructViewer.so
-rw-r--r--. 1 root root  744K Mar  6 17:46 libUE4Editor-StructViewer.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:44 libUE4Editor-SwarmInterface.debug
-rwxr-xr-x. 1 root root  201K Mar  6 17:44 libUE4Editor-SwarmInterface.so
-rw-r--r--. 1 root root  177K Mar  6 17:44 libUE4Editor-SwarmInterface.sym
-rw-r--r--. 1 root root  614K Mar  6 17:37 libUE4Editor-SynthBenchmark.debug
-rwxr-xr-x. 1 root root   31K Mar  6 17:37 libUE4Editor-SynthBenchmark.so
-rw-r--r--. 1 root root   21K Mar  6 17:37 libUE4Editor-SynthBenchmark.sym
-rw-r--r--. 1 root root  4.4M Mar  6 17:44 libUE4Editor-TargetDeviceServices.debug
-rwxr-xr-x. 1 root root  630K Mar  6 17:44 libUE4Editor-TargetDeviceServices.so
-rw-r--r--. 1 root root  394K Mar  6 17:44 libUE4Editor-TargetDeviceServices.sym
-rw-r--r--. 1 root root  3.3M Mar  6 17:36 libUE4Editor-TargetPlatform.debug
-rwxr-xr-x. 1 root root  228K Mar  6 17:36 libUE4Editor-TargetPlatform.so
-rw-r--r--. 1 root root  152K Mar  6 17:36 libUE4Editor-TargetPlatform.sym
-rw-r--r--. 1 root root  8.6M Mar  6 17:44 libUE4Editor-TaskGraph.debug
-rwxr-xr-x. 1 root root  894K Mar  6 17:44 libUE4Editor-TaskGraph.so
-rw-r--r--. 1 root root  591K Mar  6 17:44 libUE4Editor-TaskGraph.sym
-rw-r--r--. 1 root root  1.8M Mar  6 17:46 libUE4Editor-TextureCompressor.debug
-rwxr-xr-x. 1 root root  149K Mar  6 17:46 libUE4Editor-TextureCompressor.so
-rw-r--r--. 1 root root   79K Mar  6 17:46 libUE4Editor-TextureCompressor.sym
-rw-r--r--. 1 root root   10M Mar  6 17:40 libUE4Editor-TextureEditor.debug
-rwxr-xr-x. 1 root root  910K Mar  6 17:40 libUE4Editor-TextureEditor.so
-rw-r--r--. 1 root root  498K Mar  6 17:40 libUE4Editor-TextureEditor.sym
-rw-r--r--. 1 root root  395K Mar  6 17:46 libUE4Editor-TextureFormatASTC.debug
-rwxr-xr-x. 1 root root   16K Mar  6 17:46 libUE4Editor-TextureFormatASTC.so
-rw-r--r--. 1 root root  4.8K Mar  6 17:46 libUE4Editor-TextureFormatASTC.sym
-rw-r--r--. 1 root root  768K Mar  6 17:46 libUE4Editor-TextureFormatDXT.debug
-rwxr-xr-x. 1 root root   57K Mar  6 17:46 libUE4Editor-TextureFormatDXT.so
-rw-r--r--. 1 root root   25K Mar  6 17:46 libUE4Editor-TextureFormatDXT.sym
-rw-r--r--. 1 root root  437K Mar  6 17:46 libUE4Editor-TextureFormatETC2.debug
-rwxr-xr-x. 1 root root   18K Mar  6 17:46 libUE4Editor-TextureFormatETC2.so
-rw-r--r--. 1 root root  7.9K Mar  6 17:46 libUE4Editor-TextureFormatETC2.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:44 libUE4Editor-TextureFormatIntelISPCTexComp.debug
-rwxr-xr-x. 1 root root   93K Mar  6 17:44 libUE4Editor-TextureFormatIntelISPCTexComp.so
-rw-r--r--. 1 root root   56K Mar  6 17:44 libUE4Editor-TextureFormatIntelISPCTexComp.sym
-rw-r--r--. 1 root root  571K Mar  6 17:46 libUE4Editor-TextureFormatPVR.debug
-rwxr-xr-x. 1 root root   30K Mar  6 17:46 libUE4Editor-TextureFormatPVR.so
-rw-r--r--. 1 root root   17K Mar  6 17:46 libUE4Editor-TextureFormatPVR.sym
-rw-r--r--. 1 root root  455K Mar  6 17:46 libUE4Editor-TextureFormatUncompressed.debug
-rwxr-xr-x. 1 root root   22K Mar  6 17:46 libUE4Editor-TextureFormatUncompressed.so
-rw-r--r--. 1 root root   13K Mar  6 17:46 libUE4Editor-TextureFormatUncompressed.sym
-rw-r--r--. 1 root root  4.7M Mar  6 17:39 libUE4Editor-TimeManagement.debug
-rwxr-xr-x. 1 root root  651K Mar  6 17:39 libUE4Editor-TimeManagement.so
-rw-r--r--. 1 root root  281K Mar  6 17:39 libUE4Editor-TimeManagement.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:44 libUE4Editor-TimeManagementEditor.debug
-rwxr-xr-x. 1 root root  318K Mar  6 17:44 libUE4Editor-TimeManagementEditor.so
-rw-r--r--. 1 root root  165K Mar  6 17:44 libUE4Editor-TimeManagementEditor.sym
-rw-r--r--. 1 root root  6.4M Mar  6 17:38 libUE4Editor-ToolMenus.debug
-rwxr-xr-x. 1 root root  650K Mar  6 17:38 libUE4Editor-ToolMenus.so
-rw-r--r--. 1 root root  441K Mar  6 17:38 libUE4Editor-ToolMenus.sym
-rw-r--r--. 1 root root  6.8M Mar  6 17:46 libUE4Editor-ToolMenusEditor.debug
-rwxr-xr-x. 1 root root  1.2M Mar  6 17:44 libUE4Editor-ToolMenusEditor.so
-rw-r--r--. 1 root root  547K Mar  6 17:46 libUE4Editor-ToolMenusEditor.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:46 libUE4Editor-Toolbox.debug
-rwxr-xr-x. 1 root root  103K Mar  6 17:46 libUE4Editor-Toolbox.so
-rw-r--r--. 1 root root   46K Mar  6 17:46 libUE4Editor-Toolbox.sym
-rw-r--r--. 1 root root  3.7M Mar  6 17:40 libUE4Editor-TraceAnalysis.debug
-rwxr-xr-x. 1 root root  937K Mar  6 17:40 libUE4Editor-TraceAnalysis.so
-rw-r--r--. 1 root root  492K Mar  6 17:40 libUE4Editor-TraceAnalysis.sym
-rw-r--r--. 1 root root   95M Mar  6 17:42 libUE4Editor-TraceInsights.debug
-rwxr-xr-x. 1 root root  9.2M Mar  6 17:42 libUE4Editor-TraceInsights.so
-rw-r--r--. 1 root root  7.2M Mar  6 17:42 libUE4Editor-TraceInsights.sym
-rw-r--r--. 1 root root  828K Mar  6 17:35 libUE4Editor-TraceLog.debug
-rwxr-xr-x. 1 root root  340K Mar  6 17:35 libUE4Editor-TraceLog.so
-rw-r--r--. 1 root root   82K Mar  6 17:35 libUE4Editor-TraceLog.sym
-rw-r--r--. 1 root root   13M Mar  6 17:41 libUE4Editor-TraceServices.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:41 libUE4Editor-TraceServices.so
-rw-r--r--. 1 root root  1.1M Mar  6 17:41 libUE4Editor-TraceServices.sym
-rw-r--r--. 1 root root   12M Mar  6 17:46 libUE4Editor-TranslationEditor.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:42 libUE4Editor-TranslationEditor.so
-rw-r--r--. 1 root root  569K Mar  6 17:46 libUE4Editor-TranslationEditor.sym
-rw-r--r--. 1 root root  3.7M Mar  6 17:42 libUE4Editor-TreeMap.debug
-rwxr-xr-x. 1 root root  246K Mar  6 17:42 libUE4Editor-TreeMap.so
-rw-r--r--. 1 root root  165K Mar  6 17:42 libUE4Editor-TreeMap.sym
-rw-r--r--. 1 root root  2.7M Mar  6 17:42 libUE4Editor-UATHelper.debug
-rwxr-xr-x. 1 root root  171K Mar  6 17:42 libUE4Editor-UATHelper.so
-rw-r--r--. 1 root root  108K Mar  6 17:42 libUE4Editor-UATHelper.sym
-rw-r--r--. 1 root root   97K Mar  6 17:46 libUE4Editor-UE4Game.debug
-rwxr-xr-x. 1 root root  232K Mar  6 17:46 libUE4Editor-UE4Game.so
-rw-r--r--. 1 root root   48K Mar  6 17:46 libUE4Editor-UE4Game.sym
-rw-r--r--. 1 root root  415K Mar  6 17:35 libUE4Editor-UELibSampleRate.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:35 libUE4Editor-UELibSampleRate.so
-rw-r--r--. 1 root root   73K Mar  6 17:35 libUE4Editor-UELibSampleRate.sym
-rw-r--r--. 1 root root   47M Mar  6 17:46 libUE4Editor-UMG.debug
-rwxr-xr-x. 1 root root  5.8M Mar  6 17:37 libUE4Editor-UMG.so
-rw-r--r--. 1 root root  3.0M Mar  6 17:46 libUE4Editor-UMG.sym
-rw-r--r--. 1 root root   52M Mar  6 17:46 libUE4Editor-UMGEditor.debug
-rwxr-xr-x. 1 root root  5.0M Mar  6 17:41 libUE4Editor-UMGEditor.so
-rw-r--r--. 1 root root  3.4M Mar  6 17:46 libUE4Editor-UMGEditor.sym
-rw-r--r--. 1 root root   11M Mar  6 17:41 libUE4Editor-UndoHistory.debug
-rwxr-xr-x. 1 root root  978K Mar  6 17:41 libUE4Editor-UndoHistory.so
-rw-r--r--. 1 root root  682K Mar  6 17:41 libUE4Editor-UndoHistory.sym
-rw-r--r--. 1 root root  590K Mar  6 17:42 libUE4Editor-UnixCommonStartup.debug
-rwxr-xr-x. 1 root root   21K Mar  6 17:42 libUE4Editor-UnixCommonStartup.so
-rw-r--r--. 1 root root  8.9K Mar  6 17:42 libUE4Editor-UnixCommonStartup.sym
-rw-r--r--. 1 root root   91K Mar  6 17:45 libUE4Editor-UnrealAudio.debug
-rwxr-xr-x. 1 root root  229K Mar  6 17:45 libUE4Editor-UnrealAudio.so
-rw-r--r--. 1 root root   47K Mar  6 17:45 libUE4Editor-UnrealAudio.sym
-rw-r--r--. 1 root root  351M Mar  6 17:46 libUE4Editor-UnrealEd.debug
-rwxr-xr-x. 1 root root   35M Mar  6 17:37 libUE4Editor-UnrealEd.so
-rw-r--r--. 1 root root   23M Mar  6 17:46 libUE4Editor-UnrealEd.sym
-rw-r--r--. 1 root root  805K Mar  6 17:39 libUE4Editor-UnrealEdMessages.debug
-rwxr-xr-x. 1 root root  253K Mar  6 17:39 libUE4Editor-UnrealEdMessages.so
-rw-r--r--. 1 root root   68K Mar  6 17:39 libUE4Editor-UnrealEdMessages.sym
-rw-r--r--. 1 root root   13M Mar  6 17:46 libUE4Editor-VREditor.debug
-rwxr-xr-x. 1 root root  1.5M Mar  6 17:39 libUE4Editor-VREditor.so
-rw-r--r--. 1 root root  711K Mar  6 17:46 libUE4Editor-VREditor.sym
-rw-r--r--. 1 root root  5.5M Mar  6 17:39 libUE4Editor-VectorVM.debug
-rwxr-xr-x. 1 root root  710K Mar  6 17:39 libUE4Editor-VectorVM.so
-rw-r--r--. 1 root root  501K Mar  6 17:39 libUE4Editor-VectorVM.sym
-rw-r--r--. 1 root root  6.3M Mar  6 17:46 libUE4Editor-ViewportInteraction.debug
-rwxr-xr-x. 1 root root  1.4M Mar  6 17:39 libUE4Editor-ViewportInteraction.so
-rw-r--r--. 1 root root  538K Mar  6 17:46 libUE4Editor-ViewportInteraction.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:44 libUE4Editor-ViewportSnapping.debug
-rwxr-xr-x. 1 root root  242K Mar  6 17:44 libUE4Editor-ViewportSnapping.so
-rw-r--r--. 1 root root   55K Mar  6 17:44 libUE4Editor-ViewportSnapping.sym
-rw-r--r--. 1 root root  4.9M Mar  6 17:46 libUE4Editor-VirtualTexturingEditor.debug
-rwxr-xr-x. 1 root root  350K Mar  6 17:46 libUE4Editor-VirtualTexturingEditor.so
-rw-r--r--. 1 root root  178K Mar  6 17:46 libUE4Editor-VirtualTexturingEditor.sym
-rw-r--r--. 1 root root  7.8M Mar  6 17:40 libUE4Editor-Voice.debug
-rwxr-xr-x. 1 root root  2.1M Mar  6 17:40 libUE4Editor-Voice.so
-rw-r--r--. 1 root root  1.3M Mar  6 17:40 libUE4Editor-Voice.sym
-rw-r--r--. 1 root root  2.5M Mar  6 17:35 libUE4Editor-Voronoi.debug
-rwxr-xr-x. 1 root root  533K Mar  6 17:35 libUE4Editor-Voronoi.so
-rw-r--r--. 1 root root  280K Mar  6 17:35 libUE4Editor-Voronoi.sym
-rw-r--r--. 1 root root   27M Mar  6 17:44 libUE4Editor-VulkanRHI.debug
-rwxr-xr-x. 1 root root  3.4M Mar  6 17:44 libUE4Editor-VulkanRHI.so
-rw-r--r--. 1 root root  2.8M Mar  6 17:44 libUE4Editor-VulkanRHI.sym
-rw-r--r--. 1 root root   14M Mar  6 17:46 libUE4Editor-VulkanShaderFormat.debug
-rwxr-xr-x. 1 root root  6.2M Mar  6 17:46 libUE4Editor-VulkanShaderFormat.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:46 libUE4Editor-VulkanShaderFormat.sym
-rw-r--r--. 1 root root  9.2M Mar  6 17:42 libUE4Editor-WebBrowser.debug
-rwxr-xr-x. 1 root root  1.3M Mar  6 17:42 libUE4Editor-WebBrowser.so
-rw-r--r--. 1 root root  777K Mar  6 17:42 libUE4Editor-WebBrowser.sym
-rw-r--r--. 1 root root  2.3M Mar  6 17:44 libUE4Editor-WebBrowserTexture.debug
-rwxr-xr-x. 1 root root  111K Mar  6 17:44 libUE4Editor-WebBrowserTexture.so
-rw-r--r--. 1 root root   47K Mar  6 17:44 libUE4Editor-WebBrowserTexture.sym
-rw-r--r--. 1 root root  1.8M Mar  6 17:42 libUE4Editor-WebSockets.debug
-rwxr-xr-x. 1 root root  4.1M Mar  6 17:42 libUE4Editor-WebSockets.so
-rw-r--r--. 1 root root  389K Mar  6 17:42 libUE4Editor-WebSockets.sym
-rw-r--r--. 1 root root  2.2M Mar  6 17:38 libUE4Editor-WidgetCarousel.debug
-rwxr-xr-x. 1 root root  152K Mar  6 17:38 libUE4Editor-WidgetCarousel.so
-rw-r--r--. 1 root root   82K Mar  6 17:38 libUE4Editor-WidgetCarousel.sym
-rw-r--r--. 1 root root  701K Mar  6 17:37 libUE4Editor-WorkspaceMenuStructure.debug
-rwxr-xr-x. 1 root root   40K Mar  6 17:37 libUE4Editor-WorkspaceMenuStructure.so
-rw-r--r--. 1 root root   20K Mar  6 17:37 libUE4Editor-WorkspaceMenuStructure.sym
-rw-r--r--. 1 root root   40M Mar  6 17:47 libUE4Editor-WorldBrowser.debug
-rwxr-xr-x. 1 root root  3.9M Mar  6 17:47 libUE4Editor-WorldBrowser.so
-rw-r--r--. 1 root root  2.8M Mar  6 17:47 libUE4Editor-WorldBrowser.sym
-rw-r--r--. 1 root root  5.2M Mar  6 17:46 libUE4Editor-XMPP.debug
-rwxr-xr-x. 1 root root  803K Mar  6 17:46 libUE4Editor-XMPP.so
-rw-r--r--. 1 root root  425K Mar  6 17:46 libUE4Editor-XMPP.sym
-rw-r--r--. 1 root root  884K Mar  6 17:39 libUE4Editor-XmlParser.debug
-rwxr-xr-x. 1 root root  283K Mar  6 17:39 libUE4Editor-XmlParser.so
-rw-r--r--. 1 root root   85K Mar  6 17:39 libUE4Editor-XmlParser.sym
-rw-r--r--. 1 root root  435K Mar  6 17:34 libUnrealFrontend-AllDesktopTargetPlatform.debug
-rwxr-xr-x. 1 root root   17K Mar  6 17:34 libUnrealFrontend-AllDesktopTargetPlatform.so
-rw-r--r--. 1 root root  9.9K Mar  6 17:34 libUnrealFrontend-AllDesktopTargetPlatform.sym
-rw-r--r--. 1 root root  9.1M Mar  6 17:33 libUnrealFrontend-ApplicationCore.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:33 libUnrealFrontend-ApplicationCore.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:33 libUnrealFrontend-ApplicationCore.sym
-rw-r--r--. 1 root root   12M Mar  6 17:34 libUnrealFrontend-AssetRegistry.debug
-rwxr-xr-x. 1 root root  909K Mar  6 17:34 libUnrealFrontend-AssetRegistry.so
-rw-r--r--. 1 root root  790K Mar  6 17:34 libUnrealFrontend-AssetRegistry.sym
-rw-r--r--. 1 root root  734K Mar  6 17:34 libUnrealFrontend-AudioPlatformConfiguration.debug
-rwxr-xr-x. 1 root root   25K Mar  6 17:34 libUnrealFrontend-AudioPlatformConfiguration.so
-rw-r--r--. 1 root root   17K Mar  6 17:34 libUnrealFrontend-AudioPlatformConfiguration.sym
-rw-r--r--. 1 root root  4.5M Mar  6 17:34 libUnrealFrontend-AutomationController.debug
-rwxr-xr-x. 1 root root  345K Mar  6 17:34 libUnrealFrontend-AutomationController.so
-rw-r--r--. 1 root root  288K Mar  6 17:34 libUnrealFrontend-AutomationController.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:34 libUnrealFrontend-AutomationMessages.debug
-rwxr-xr-x. 1 root root  155K Mar  6 17:34 libUnrealFrontend-AutomationMessages.so
-rw-r--r--. 1 root root  196K Mar  6 17:34 libUnrealFrontend-AutomationMessages.sym
-rw-r--r--. 1 root root   18M Mar  6 17:34 libUnrealFrontend-AutomationWindow.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:34 libUnrealFrontend-AutomationWindow.so
-rw-r--r--. 1 root root  1.1M Mar  6 17:34 libUnrealFrontend-AutomationWindow.sym
-rw-r--r--. 1 root root   17K Mar  6 17:33 libUnrealFrontend-BuildSettings.debug
-rwxr-xr-x. 1 root root  5.0K Mar  6 17:33 libUnrealFrontend-BuildSettings.so
-rw-r--r--. 1 root root   868 Mar  6 17:33 libUnrealFrontend-BuildSettings.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:33 libUnrealFrontend-Cbor.debug
-rwxr-xr-x. 1 root root   90K Mar  6 17:33 libUnrealFrontend-Cbor.so
-rw-r--r--. 1 root root   77K Mar  6 17:33 libUnrealFrontend-Cbor.sym
-rw-r--r--. 1 root root   91M Mar  6 17:33 libUnrealFrontend-Core.debug
-rwxr-xr-x. 1 root root   13M Mar  6 17:33 libUnrealFrontend-Core.so
-rw-r--r--. 1 root root  6.5M Mar  6 17:33 libUnrealFrontend-Core.sym
-rw-r--r--. 1 root root   65M Mar  6 17:34 libUnrealFrontend-CoreUObject.debug
-rwxr-xr-x. 1 root root  5.9M Mar  6 17:34 libUnrealFrontend-CoreUObject.so
-rw-r--r--. 1 root root  4.2M Mar  6 17:34 libUnrealFrontend-CoreUObject.sym
-rw-r--r--. 1 root root   11M Mar  6 17:33 libUnrealFrontend-DesktopPlatform.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:33 libUnrealFrontend-DesktopPlatform.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:33 libUnrealFrontend-DesktopPlatform.sym
-rw-r--r--. 1 root root  1.8M Mar  6 17:34 libUnrealFrontend-DesktopWidgets.debug
-rwxr-xr-x. 1 root root  109K Mar  6 17:34 libUnrealFrontend-DesktopWidgets.so
-rw-r--r--. 1 root root   50K Mar  6 17:34 libUnrealFrontend-DesktopWidgets.sym
-rw-r--r--. 1 root root   17M Mar  6 17:34 libUnrealFrontend-DeviceManager.debug
-rwxr-xr-x. 1 root root  1.5M Mar  6 17:34 libUnrealFrontend-DeviceManager.so
-rw-r--r--. 1 root root  1.1M Mar  6 17:34 libUnrealFrontend-DeviceManager.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:33 libUnrealFrontend-DirectoryWatcher.debug
-rwxr-xr-x. 1 root root  286K Mar  6 17:33 libUnrealFrontend-DirectoryWatcher.so
-rw-r--r--. 1 root root  238K Mar  6 17:33 libUnrealFrontend-DirectoryWatcher.sym
-rw-r--r--. 1 root root  5.2M Mar  6 17:34 libUnrealFrontend-EditorStyle.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:34 libUnrealFrontend-EditorStyle.so
-rw-r--r--. 1 root root  279K Mar  6 17:34 libUnrealFrontend-EditorStyle.sym
-rw-r--r--. 1 root root  792K Mar  6 17:34 libUnrealFrontend-EngineMessages.debug
-rwxr-xr-x. 1 root root   55K Mar  6 17:34 libUnrealFrontend-EngineMessages.so
-rw-r--r--. 1 root root   63K Mar  6 17:34 libUnrealFrontend-EngineMessages.sym
-rw-r--r--. 1 root root  3.4M Mar  6 17:33 libUnrealFrontend-HTTP.debug
-rwxr-xr-x. 1 root root  4.4M Mar  6 17:33 libUnrealFrontend-HTTP.so
-rw-r--r--. 1 root root  517K Mar  6 17:33 libUnrealFrontend-HTTP.sym
-rw-r--r--. 1 root root  781K Mar  6 17:33 libUnrealFrontend-ImageCore.debug
-rwxr-xr-x. 1 root root   52K Mar  6 17:33 libUnrealFrontend-ImageCore.so
-rw-r--r--. 1 root root   34K Mar  6 17:33 libUnrealFrontend-ImageCore.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:34 libUnrealFrontend-ImageWrapper.debug
-rwxr-xr-x. 1 root root  4.0M Mar  6 17:34 libUnrealFrontend-ImageWrapper.so
-rw-r--r--. 1 root root  501K Mar  6 17:34 libUnrealFrontend-ImageWrapper.sym
-rw-r--r--. 1 root root  2.4M Mar  6 17:34 libUnrealFrontend-InputCore.debug
-rwxr-xr-x. 1 root root  329K Mar  6 17:34 libUnrealFrontend-InputCore.so
-rw-r--r--. 1 root root  107K Mar  6 17:34 libUnrealFrontend-InputCore.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:33 libUnrealFrontend-Json.debug
-rwxr-xr-x. 1 root root  190K Mar  6 17:33 libUnrealFrontend-Json.so
-rw-r--r--. 1 root root  124K Mar  6 17:33 libUnrealFrontend-Json.sym
-rw-r--r--. 1 root root  2.5M Mar  6 17:34 libUnrealFrontend-JsonUtilities.debug
-rwxr-xr-x. 1 root root  200K Mar  6 17:34 libUnrealFrontend-JsonUtilities.so
-rw-r--r--. 1 root root  148K Mar  6 17:34 libUnrealFrontend-JsonUtilities.sym
-rw-r--r--. 1 root root  637K Mar  6 17:34 libUnrealFrontend-LaunchDaemonMessages.debug
-rwxr-xr-x. 1 root root   32K Mar  6 17:34 libUnrealFrontend-LaunchDaemonMessages.so
-rw-r--r--. 1 root root   30K Mar  6 17:34 libUnrealFrontend-LaunchDaemonMessages.sym
-rw-r--r--. 1 root root  282K Mar  6 17:33 libUnrealFrontend-LauncherPlatform.debug
-rwxr-xr-x. 1 root root   11K Mar  6 17:33 libUnrealFrontend-LauncherPlatform.so
-rw-r--r--. 1 root root  3.4K Mar  6 17:33 libUnrealFrontend-LauncherPlatform.sym
-rw-r--r--. 1 root root  4.3M Mar  6 17:34 libUnrealFrontend-LauncherServices.debug
-rwxr-xr-x. 1 root root  363K Mar  6 17:34 libUnrealFrontend-LauncherServices.so
-rw-r--r--. 1 root root  238K Mar  6 17:34 libUnrealFrontend-LauncherServices.sym
-rw-r--r--. 1 root root   11M Mar  6 17:34 libUnrealFrontend-MessageLog.debug
-rwxr-xr-x. 1 root root  964K Mar  6 17:34 libUnrealFrontend-MessageLog.so
-rw-r--r--. 1 root root  664K Mar  6 17:34 libUnrealFrontend-MessageLog.sym
-rw-r--r--. 1 root root  3.9M Mar  6 17:34 libUnrealFrontend-Messaging.debug
-rwxr-xr-x. 1 root root  250K Mar  6 17:34 libUnrealFrontend-Messaging.so
-rw-r--r--. 1 root root  233K Mar  6 17:34 libUnrealFrontend-Messaging.sym
-rw-r--r--. 1 root root   32K Mar  6 17:33 libUnrealFrontend-NetCommon.debug
-rwxr-xr-x. 1 root root  6.9K Mar  6 17:33 libUnrealFrontend-NetCommon.so
-rw-r--r--. 1 root root  2.3K Mar  6 17:33 libUnrealFrontend-NetCommon.sym
-rw-r--r--. 1 root root  444K Mar  6 17:33 libUnrealFrontend-Networking.debug
-rwxr-xr-x. 1 root root   27K Mar  6 17:33 libUnrealFrontend-Networking.so
-rw-r--r--. 1 root root   13K Mar  6 17:33 libUnrealFrontend-Networking.sym
-rw-r--r--. 1 root root  7.5M Mar  6 17:34 libUnrealFrontend-OutputLog.debug
-rwxr-xr-x. 1 root root  650K Mar  6 17:34 libUnrealFrontend-OutputLog.so
-rw-r--r--. 1 root root  421K Mar  6 17:34 libUnrealFrontend-OutputLog.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:34 libUnrealFrontend-PIEPreviewDeviceSpecification.debug
-rwxr-xr-x. 1 root root   77K Mar  6 17:34 libUnrealFrontend-PIEPreviewDeviceSpecification.so
-rw-r--r--. 1 root root   73K Mar  6 17:34 libUnrealFrontend-PIEPreviewDeviceSpecification.sym
-rw-r--r--. 1 root root   31M Mar  6 17:34 libUnrealFrontend-Profiler.debug
-rwxr-xr-x. 1 root root  2.7M Mar  6 17:34 libUnrealFrontend-Profiler.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:34 libUnrealFrontend-Profiler.sym
-rw-r--r--. 1 root root  4.1M Mar  6 17:34 libUnrealFrontend-ProfilerClient.debug
-rwxr-xr-x. 1 root root  234K Mar  6 17:34 libUnrealFrontend-ProfilerClient.so
-rw-r--r--. 1 root root  196K Mar  6 17:34 libUnrealFrontend-ProfilerClient.sym
-rw-r--r--. 1 root root  922K Mar  6 17:34 libUnrealFrontend-ProfilerMessages.debug
-rwxr-xr-x. 1 root root   80K Mar  6 17:34 libUnrealFrontend-ProfilerMessages.so
-rw-r--r--. 1 root root   98K Mar  6 17:34 libUnrealFrontend-ProfilerMessages.sym
-rw-r--r--. 1 root root   29M Mar  6 17:34 libUnrealFrontend-ProjectLauncher.debug
-rwxr-xr-x. 1 root root  2.9M Mar  6 17:34 libUnrealFrontend-ProjectLauncher.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:34 libUnrealFrontend-ProjectLauncher.sym
-rw-r--r--. 1 root root  4.9M Mar  6 17:33 libUnrealFrontend-Projects.debug
-rwxr-xr-x. 1 root root  378K Mar  6 17:33 libUnrealFrontend-Projects.so
-rw-r--r--. 1 root root  267K Mar  6 17:33 libUnrealFrontend-Projects.sym
-rw-r--r--. 1 root root   11M Mar  6 17:33 libUnrealFrontend-RHI.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:33 libUnrealFrontend-RHI.so
-rw-r--r--. 1 root root  786K Mar  6 17:33 libUnrealFrontend-RHI.sym
-rw-r--r--. 1 root root   24M Mar  6 17:33 libUnrealFrontend-RenderCore.debug
-rwxr-xr-x. 1 root root  2.3M Mar  6 17:33 libUnrealFrontend-RenderCore.so
-rw-r--r--. 1 root root  1.8M Mar  6 17:33 libUnrealFrontend-RenderCore.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:33 libUnrealFrontend-SSL.debug
-rwxr-xr-x. 1 root root  3.8M Mar  6 17:33 libUnrealFrontend-SSL.so
-rw-r--r--. 1 root root  317K Mar  6 17:33 libUnrealFrontend-SSL.sym
-rw-r--r--. 1 root root  7.2M Mar  6 17:34 libUnrealFrontend-ScreenShotComparison.debug
-rwxr-xr-x. 1 root root  636K Mar  6 17:34 libUnrealFrontend-ScreenShotComparison.so
-rw-r--r--. 1 root root  354K Mar  6 17:34 libUnrealFrontend-ScreenShotComparison.sym
-rw-r--r--. 1 root root  3.3M Mar  6 17:34 libUnrealFrontend-ScreenShotComparisonTools.debug
-rwxr-xr-x. 1 root root  256K Mar  6 17:34 libUnrealFrontend-ScreenShotComparisonTools.so
-rw-r--r--. 1 root root  165K Mar  6 17:34 libUnrealFrontend-ScreenShotComparisonTools.sym
-rw-r--r--. 1 root root  5.2M Mar  6 17:34 libUnrealFrontend-Serialization.debug
-rwxr-xr-x. 1 root root  415K Mar  6 17:34 libUnrealFrontend-Serialization.so
-rw-r--r--. 1 root root  352K Mar  6 17:34 libUnrealFrontend-Serialization.sym
-rw-r--r--. 1 root root   18M Mar  6 17:34 libUnrealFrontend-SessionFrontend.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:34 libUnrealFrontend-SessionFrontend.so
-rw-r--r--. 1 root root  1.2M Mar  6 17:34 libUnrealFrontend-SessionFrontend.sym
-rw-r--r--. 1 root root  709K Mar  6 17:34 libUnrealFrontend-SessionMessages.debug
-rwxr-xr-x. 1 root root   44K Mar  6 17:34 libUnrealFrontend-SessionMessages.so
-rw-r--r--. 1 root root   47K Mar  6 17:34 libUnrealFrontend-SessionMessages.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:34 libUnrealFrontend-SessionServices.debug
-rwxr-xr-x. 1 root root  132K Mar  6 17:34 libUnrealFrontend-SessionServices.so
-rw-r--r--. 1 root root   96K Mar  6 17:34 libUnrealFrontend-SessionServices.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:34 libUnrealFrontend-Settings.debug
-rwxr-xr-x. 1 root root   67K Mar  6 17:34 libUnrealFrontend-Settings.so
-rw-r--r--. 1 root root   51K Mar  6 17:34 libUnrealFrontend-Settings.sym
-rw-r--r--. 1 root root  5.0M Mar  6 17:33 libUnrealFrontend-ShaderCompilerCommon.debug
-rwxr-xr-x. 1 root root  433K Mar  6 17:33 libUnrealFrontend-ShaderCompilerCommon.so
-rw-r--r--. 1 root root  341K Mar  6 17:33 libUnrealFrontend-ShaderCompilerCommon.sym
-rw-r--r--. 1 root root   16M Mar  6 17:34 libUnrealFrontend-ShaderFormatOpenGL.debug
-rwxr-xr-x. 1 root root  3.0M Mar  6 17:34 libUnrealFrontend-ShaderFormatOpenGL.so
-rw-r--r--. 1 root root  2.1M Mar  6 17:34 libUnrealFrontend-ShaderFormatOpenGL.sym
-rw-r--r--. 1 root root  9.7M Mar  6 17:34 libUnrealFrontend-ShaderFormatVectorVM.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:34 libUnrealFrontend-ShaderFormatVectorVM.so
-rw-r--r--. 1 root root  997K Mar  6 17:34 libUnrealFrontend-ShaderFormatVectorVM.sym
-rw-r--r--. 1 root root  1.2M Mar  6 17:33 libUnrealFrontend-ShaderPreprocessor.debug
-rwxr-xr-x. 1 root root  191K Mar  6 17:33 libUnrealFrontend-ShaderPreprocessor.so
-rw-r--r--. 1 root root   50K Mar  6 17:33 libUnrealFrontend-ShaderPreprocessor.sym
-rw-r--r--. 1 root root   59M Mar  6 17:34 libUnrealFrontend-Slate.debug
-rwxr-xr-x. 1 root root  5.4M Mar  6 17:34 libUnrealFrontend-Slate.so
-rw-r--r--. 1 root root  3.3M Mar  6 17:34 libUnrealFrontend-Slate.sym
-rw-r--r--. 1 root root   24M Mar  6 17:34 libUnrealFrontend-SlateCore.debug
-rwxr-xr-x. 1 root root  4.7M Mar  6 17:34 libUnrealFrontend-SlateCore.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:34 libUnrealFrontend-SlateCore.sym
-rw-r--r--. 1 root root  6.6M Mar  6 17:34 libUnrealFrontend-SlateFileDialogs.debug
-rwxr-xr-x. 1 root root  603K Mar  6 17:34 libUnrealFrontend-SlateFileDialogs.so
-rw-r--r--. 1 root root  373K Mar  6 17:34 libUnrealFrontend-SlateFileDialogs.sym
-rw-r--r--. 1 root root   28M Mar  6 17:34 libUnrealFrontend-SlateReflector.debug
-rwxr-xr-x. 1 root root  2.5M Mar  6 17:34 libUnrealFrontend-SlateReflector.so
-rw-r--r--. 1 root root  1.8M Mar  6 17:34 libUnrealFrontend-SlateReflector.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:33 libUnrealFrontend-Sockets.debug
-rwxr-xr-x. 1 root root  189K Mar  6 17:33 libUnrealFrontend-Sockets.so
-rw-r--r--. 1 root root  149K Mar  6 17:33 libUnrealFrontend-Sockets.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:34 libUnrealFrontend-SourceCodeAccess.debug
-rwxr-xr-x. 1 root root   51K Mar  6 17:34 libUnrealFrontend-SourceCodeAccess.so
-rw-r--r--. 1 root root   32K Mar  6 17:34 libUnrealFrontend-SourceCodeAccess.sym
-rw-r--r--. 1 root root  4.6M Mar  6 17:34 libUnrealFrontend-SourceControl.debug
-rwxr-xr-x. 1 root root  412K Mar  6 17:34 libUnrealFrontend-SourceControl.so
-rw-r--r--. 1 root root  211K Mar  6 17:34 libUnrealFrontend-SourceControl.sym
-rw-r--r--. 1 root root  8.9M Mar  6 17:34 libUnrealFrontend-StandaloneRenderer.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:34 libUnrealFrontend-StandaloneRenderer.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:34 libUnrealFrontend-StandaloneRenderer.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:34 libUnrealFrontend-TargetDeviceServices.debug
-rwxr-xr-x. 1 root root  330K Mar  6 17:34 libUnrealFrontend-TargetDeviceServices.so
-rw-r--r--. 1 root root  321K Mar  6 17:34 libUnrealFrontend-TargetDeviceServices.sym
-rw-r--r--. 1 root root  3.1M Mar  6 17:34 libUnrealFrontend-TargetPlatform.debug
-rwxr-xr-x. 1 root root  189K Mar  6 17:34 libUnrealFrontend-TargetPlatform.so
-rw-r--r--. 1 root root  123K Mar  6 17:34 libUnrealFrontend-TargetPlatform.sym
-rw-r--r--. 1 root root  397K Mar  6 17:34 libUnrealFrontend-TextureFormatASTC.debug
-rwxr-xr-x. 1 root root   15K Mar  6 17:34 libUnrealFrontend-TextureFormatASTC.so
-rw-r--r--. 1 root root  4.9K Mar  6 17:34 libUnrealFrontend-TextureFormatASTC.sym
-rw-r--r--. 1 root root  705K Mar  6 17:34 libUnrealFrontend-TextureFormatDXT.debug
-rwxr-xr-x. 1 root root   45K Mar  6 17:34 libUnrealFrontend-TextureFormatDXT.so
-rw-r--r--. 1 root root   21K Mar  6 17:34 libUnrealFrontend-TextureFormatDXT.sym
-rw-r--r--. 1 root root  938K Mar  6 17:34 libUnrealFrontend-TextureFormatIntelISPCTexComp.debug
-rwxr-xr-x. 1 root root   68K Mar  6 17:34 libUnrealFrontend-TextureFormatIntelISPCTexComp.so
-rw-r--r--. 1 root root   49K Mar  6 17:34 libUnrealFrontend-TextureFormatIntelISPCTexComp.sym
-rw-r--r--. 1 root root  531K Mar  6 17:34 libUnrealFrontend-TextureFormatPVR.debug
-rwxr-xr-x. 1 root root   26K Mar  6 17:34 libUnrealFrontend-TextureFormatPVR.so
-rw-r--r--. 1 root root   14K Mar  6 17:34 libUnrealFrontend-TextureFormatPVR.sym
-rw-r--r--. 1 root root  424K Mar  6 17:33 libUnrealFrontend-TextureFormatUncompressed.debug
-rwxr-xr-x. 1 root root   19K Mar  6 17:33 libUnrealFrontend-TextureFormatUncompressed.so
-rw-r--r--. 1 root root   11K Mar  6 17:33 libUnrealFrontend-TextureFormatUncompressed.sym
-rw-r--r--. 1 root root  407K Mar  6 17:33 libUnrealFrontend-TraceLog.debug
-rwxr-xr-x. 1 root root   85K Mar  6 17:33 libUnrealFrontend-TraceLog.so
-rw-r--r--. 1 root root   12K Mar  6 17:33 libUnrealFrontend-TraceLog.sym
-rw-r--r--. 1 root root  346K Mar  6 17:33 libUnrealFrontend-UELibSampleRate.debug
-rwxr-xr-x. 1 root root  1.5M Mar  6 17:33 libUnrealFrontend-UELibSampleRate.so
-rw-r--r--. 1 root root   28K Mar  6 17:33 libUnrealFrontend-UELibSampleRate.sym
-rw-r--r--. 1 root root  580K Mar  6 17:34 libUnrealFrontend-UnixCommonStartup.debug
-rwxr-xr-x. 1 root root   19K Mar  6 17:34 libUnrealFrontend-UnixCommonStartup.so
-rw-r--r--. 1 root root  8.3K Mar  6 17:34 libUnrealFrontend-UnixCommonStartup.sym
-rw-r--r--. 1 root root  738K Mar  6 17:34 libUnrealFrontend-UnrealEdMessages.debug
-rwxr-xr-x. 1 root root   26K Mar  6 17:34 libUnrealFrontend-UnrealEdMessages.so
-rw-r--r--. 1 root root   22K Mar  6 17:34 libUnrealFrontend-UnrealEdMessages.sym
-rw-r--r--. 1 root root  5.3M Mar  6 17:34 libUnrealFrontend-VectorVM.debug
-rwxr-xr-x. 1 root root  465K Mar  6 17:34 libUnrealFrontend-VectorVM.so
-rw-r--r--. 1 root root  446K Mar  6 17:34 libUnrealFrontend-VectorVM.sym
-rw-r--r--. 1 root root   13M Mar  6 17:34 libUnrealFrontend-VulkanShaderFormat.debug
-rwxr-xr-x. 1 root root  6.1M Mar  6 17:34 libUnrealFrontend-VulkanShaderFormat.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:34 libUnrealFrontend-VulkanShaderFormat.sym
-rw-r--r--. 1 root root  644K Mar  6 17:34 libUnrealFrontend-WorkspaceMenuStructure.debug
-rwxr-xr-x. 1 root root   31K Mar  6 17:34 libUnrealFrontend-WorkspaceMenuStructure.so
-rw-r--r--. 1 root root   16K Mar  6 17:34 libUnrealFrontend-WorkspaceMenuStructure.sym
-rw-r--r--. 1 root root   17K Mar  6 17:29 libUnrealHeaderTool-BuildSettings.debug
-rwxr-xr-x. 1 root root  5.0K Mar  6 17:29 libUnrealHeaderTool-BuildSettings.so
-rw-r--r--. 1 root root   868 Mar  6 17:29 libUnrealHeaderTool-BuildSettings.sym
-rw-r--r--. 1 root root   81M Mar  6 17:30 libUnrealHeaderTool-Core.debug
-rwxr-xr-x. 1 root root  8.7M Mar  6 17:30 libUnrealHeaderTool-Core.so
-rw-r--r--. 1 root root  5.9M Mar  6 17:30 libUnrealHeaderTool-Core.sym
-rw-r--r--. 1 root root   57M Mar  6 17:30 libUnrealHeaderTool-CoreUObject.debug
-rwxr-xr-x. 1 root root  5.2M Mar  6 17:30 libUnrealHeaderTool-CoreUObject.so
-rw-r--r--. 1 root root  4.2M Mar  6 17:30 libUnrealHeaderTool-CoreUObject.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:30 libUnrealHeaderTool-Json.debug
-rwxr-xr-x. 1 root root  225K Mar  6 17:30 libUnrealHeaderTool-Json.so
-rw-r--r--. 1 root root  156K Mar  6 17:30 libUnrealHeaderTool-Json.sym
-rw-r--r--. 1 root root  5.4M Mar  6 17:30 libUnrealHeaderTool-Projects.debug
-rwxr-xr-x. 1 root root  457K Mar  6 17:30 libUnrealHeaderTool-Projects.so
-rw-r--r--. 1 root root  332K Mar  6 17:30 libUnrealHeaderTool-Projects.sym
-rw-r--r--. 1 root root  407K Mar  6 17:29 libUnrealHeaderTool-TraceLog.debug
-rwxr-xr-x. 1 root root   85K Mar  6 17:29 libUnrealHeaderTool-TraceLog.so
-rw-r--r--. 1 root root   12K Mar  6 17:29 libUnrealHeaderTool-TraceLog.sym
-rw-r--r--. 1 root root  358K Mar  6 17:48 libUnrealInsights-Analytics.debug
-rwxr-xr-x. 1 root root   19K Mar  6 17:48 libUnrealInsights-Analytics.so
-rw-r--r--. 1 root root  9.0K Mar  6 17:48 libUnrealInsights-Analytics.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:48 libUnrealInsights-AnalyticsET.debug
-rwxr-xr-x. 1 root root  139K Mar  6 17:48 libUnrealInsights-AnalyticsET.so
-rw-r--r--. 1 root root   97K Mar  6 17:48 libUnrealInsights-AnalyticsET.sym
-rw-r--r--. 1 root root   38M Mar  6 17:49 libUnrealInsights-AppFramework.debug
-rwxr-xr-x. 1 root root  4.0M Mar  6 17:49 libUnrealInsights-AppFramework.so
-rw-r--r--. 1 root root  2.5M Mar  6 17:49 libUnrealInsights-AppFramework.sym
-rw-r--r--. 1 root root  9.1M Mar  6 17:48 libUnrealInsights-ApplicationCore.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:48 libUnrealInsights-ApplicationCore.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:48 libUnrealInsights-ApplicationCore.sym
-rw-r--r--. 1 root root   12M Mar  6 17:48 libUnrealInsights-AssetRegistry.debug
-rwxr-xr-x. 1 root root  909K Mar  6 17:48 libUnrealInsights-AssetRegistry.so
-rw-r--r--. 1 root root  790K Mar  6 17:48 libUnrealInsights-AssetRegistry.sym
-rw-r--r--. 1 root root  4.5M Mar  6 17:48 libUnrealInsights-AutomationController.debug
-rwxr-xr-x. 1 root root  345K Mar  6 17:48 libUnrealInsights-AutomationController.so
-rw-r--r--. 1 root root  288K Mar  6 17:48 libUnrealInsights-AutomationController.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:48 libUnrealInsights-AutomationMessages.debug
-rwxr-xr-x. 1 root root  155K Mar  6 17:48 libUnrealInsights-AutomationMessages.so
-rw-r--r--. 1 root root  196K Mar  6 17:48 libUnrealInsights-AutomationMessages.sym
-rw-r--r--. 1 root root   18M Mar  6 17:48 libUnrealInsights-AutomationWindow.debug
-rwxr-xr-x. 1 root root  1.6M Mar  6 17:48 libUnrealInsights-AutomationWindow.so
-rw-r--r--. 1 root root  1.1M Mar  6 17:48 libUnrealInsights-AutomationWindow.sym
-rw-r--r--. 1 root root  1.5M Mar  6 17:48 libUnrealInsights-AutomationWorker.debug
-rwxr-xr-x. 1 root root  113K Mar  6 17:48 libUnrealInsights-AutomationWorker.so
-rw-r--r--. 1 root root   72K Mar  6 17:48 libUnrealInsights-AutomationWorker.sym
-rw-r--r--. 1 root root   17K Mar  6 17:47 libUnrealInsights-BuildSettings.debug
-rwxr-xr-x. 1 root root  5.0K Mar  6 17:47 libUnrealInsights-BuildSettings.so
-rw-r--r--. 1 root root   868 Mar  6 17:47 libUnrealInsights-BuildSettings.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:48 libUnrealInsights-Cbor.debug
-rwxr-xr-x. 1 root root   90K Mar  6 17:48 libUnrealInsights-Cbor.so
-rw-r--r--. 1 root root   77K Mar  6 17:48 libUnrealInsights-Cbor.sym
-rw-r--r--. 1 root root   91M Mar  6 17:48 libUnrealInsights-Core.debug
-rwxr-xr-x. 1 root root   13M Mar  6 17:48 libUnrealInsights-Core.so
-rw-r--r--. 1 root root  6.5M Mar  6 17:48 libUnrealInsights-Core.sym
-rw-r--r--. 1 root root   65M Mar  6 17:48 libUnrealInsights-CoreUObject.debug
-rwxr-xr-x. 1 root root  5.9M Mar  6 17:48 libUnrealInsights-CoreUObject.so
-rw-r--r--. 1 root root  4.2M Mar  6 17:48 libUnrealInsights-CoreUObject.sym
-rw-r--r--. 1 root root   11M Mar  6 17:48 libUnrealInsights-DesktopPlatform.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:48 libUnrealInsights-DesktopPlatform.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:48 libUnrealInsights-DesktopPlatform.sym
-rw-r--r--. 1 root root  4.0M Mar  6 17:48 libUnrealInsights-DirectoryWatcher.debug
-rwxr-xr-x. 1 root root  286K Mar  6 17:48 libUnrealInsights-DirectoryWatcher.so
-rw-r--r--. 1 root root  238K Mar  6 17:48 libUnrealInsights-DirectoryWatcher.sym
-rw-r--r--. 1 root root  5.2M Mar  6 17:48 libUnrealInsights-EditorStyle.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:48 libUnrealInsights-EditorStyle.so
-rw-r--r--. 1 root root  279K Mar  6 17:48 libUnrealInsights-EditorStyle.sym
-rw-r--r--. 1 root root  792K Mar  6 17:48 libUnrealInsights-EngineMessages.debug
-rwxr-xr-x. 1 root root   55K Mar  6 17:48 libUnrealInsights-EngineMessages.so
-rw-r--r--. 1 root root   63K Mar  6 17:48 libUnrealInsights-EngineMessages.sym
-rw-r--r--. 1 root root  3.4M Mar  6 17:48 libUnrealInsights-HTTP.debug
-rwxr-xr-x. 1 root root  4.4M Mar  6 17:48 libUnrealInsights-HTTP.so
-rw-r--r--. 1 root root  517K Mar  6 17:48 libUnrealInsights-HTTP.sym
-rw-r--r--. 1 root root  2.0M Mar  6 17:48 libUnrealInsights-ImageWrapper.debug
-rwxr-xr-x. 1 root root  4.0M Mar  6 17:48 libUnrealInsights-ImageWrapper.so
-rw-r--r--. 1 root root  501K Mar  6 17:48 libUnrealInsights-ImageWrapper.sym
-rw-r--r--. 1 root root  2.4M Mar  6 17:48 libUnrealInsights-InputCore.debug
-rwxr-xr-x. 1 root root  329K Mar  6 17:48 libUnrealInsights-InputCore.so
-rw-r--r--. 1 root root  107K Mar  6 17:48 libUnrealInsights-InputCore.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:48 libUnrealInsights-Json.debug
-rwxr-xr-x. 1 root root  190K Mar  6 17:48 libUnrealInsights-Json.so
-rw-r--r--. 1 root root  124K Mar  6 17:48 libUnrealInsights-Json.sym
-rw-r--r--. 1 root root  2.5M Mar  6 17:48 libUnrealInsights-JsonUtilities.debug
-rwxr-xr-x. 1 root root  200K Mar  6 17:48 libUnrealInsights-JsonUtilities.so
-rw-r--r--. 1 root root  148K Mar  6 17:48 libUnrealInsights-JsonUtilities.sym
-rw-r--r--. 1 root root   11M Mar  6 17:48 libUnrealInsights-MessageLog.debug
-rwxr-xr-x. 1 root root  964K Mar  6 17:48 libUnrealInsights-MessageLog.so
-rw-r--r--. 1 root root  664K Mar  6 17:48 libUnrealInsights-MessageLog.sym
-rw-r--r--. 1 root root  3.9M Mar  6 17:48 libUnrealInsights-Messaging.debug
-rwxr-xr-x. 1 root root  250K Mar  6 17:48 libUnrealInsights-Messaging.so
-rw-r--r--. 1 root root  233K Mar  6 17:48 libUnrealInsights-Messaging.sym
-rw-r--r--. 1 root root   32K Mar  6 17:48 libUnrealInsights-NetCommon.debug
-rwxr-xr-x. 1 root root  6.9K Mar  6 17:48 libUnrealInsights-NetCommon.so
-rw-r--r--. 1 root root  2.3K Mar  6 17:48 libUnrealInsights-NetCommon.sym
-rw-r--r--. 1 root root  4.9M Mar  6 17:48 libUnrealInsights-Projects.debug
-rwxr-xr-x. 1 root root  378K Mar  6 17:48 libUnrealInsights-Projects.so
-rw-r--r--. 1 root root  267K Mar  6 17:48 libUnrealInsights-Projects.sym
-rw-r--r--. 1 root root   11M Mar  6 17:48 libUnrealInsights-RHI.debug
-rwxr-xr-x. 1 root root  1.1M Mar  6 17:48 libUnrealInsights-RHI.so
-rw-r--r--. 1 root root  786K Mar  6 17:48 libUnrealInsights-RHI.sym
-rw-r--r--. 1 root root   24M Mar  6 17:48 libUnrealInsights-RenderCore.debug
-rwxr-xr-x. 1 root root  2.3M Mar  6 17:48 libUnrealInsights-RenderCore.so
-rw-r--r--. 1 root root  1.8M Mar  6 17:48 libUnrealInsights-RenderCore.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:48 libUnrealInsights-SSL.debug
-rwxr-xr-x. 1 root root  3.8M Mar  6 17:48 libUnrealInsights-SSL.so
-rw-r--r--. 1 root root  317K Mar  6 17:48 libUnrealInsights-SSL.sym
-rw-r--r--. 1 root root  3.3M Mar  6 17:48 libUnrealInsights-ScreenShotComparisonTools.debug
-rwxr-xr-x. 1 root root  256K Mar  6 17:48 libUnrealInsights-ScreenShotComparisonTools.so
-rw-r--r--. 1 root root  165K Mar  6 17:48 libUnrealInsights-ScreenShotComparisonTools.sym
-rw-r--r--. 1 root root  709K Mar  6 17:48 libUnrealInsights-SessionMessages.debug
-rwxr-xr-x. 1 root root   44K Mar  6 17:48 libUnrealInsights-SessionMessages.so
-rw-r--r--. 1 root root   47K Mar  6 17:48 libUnrealInsights-SessionMessages.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:48 libUnrealInsights-SessionServices.debug
-rwxr-xr-x. 1 root root  132K Mar  6 17:48 libUnrealInsights-SessionServices.so
-rw-r--r--. 1 root root   96K Mar  6 17:48 libUnrealInsights-SessionServices.sym
-rw-r--r--. 1 root root  1.3M Mar  6 17:48 libUnrealInsights-Settings.debug
-rwxr-xr-x. 1 root root   67K Mar  6 17:48 libUnrealInsights-Settings.so
-rw-r--r--. 1 root root   51K Mar  6 17:48 libUnrealInsights-Settings.sym
-rw-r--r--. 1 root root   59M Mar  6 17:48 libUnrealInsights-Slate.debug
-rwxr-xr-x. 1 root root  5.4M Mar  6 17:48 libUnrealInsights-Slate.so
-rw-r--r--. 1 root root  3.3M Mar  6 17:48 libUnrealInsights-Slate.sym
-rw-r--r--. 1 root root   24M Mar  6 17:48 libUnrealInsights-SlateCore.debug
-rwxr-xr-x. 1 root root  4.7M Mar  6 17:48 libUnrealInsights-SlateCore.so
-rw-r--r--. 1 root root  2.0M Mar  6 17:48 libUnrealInsights-SlateCore.sym
-rw-r--r--. 1 root root  6.6M Mar  6 17:48 libUnrealInsights-SlateFileDialogs.debug
-rwxr-xr-x. 1 root root  603K Mar  6 17:48 libUnrealInsights-SlateFileDialogs.so
-rw-r--r--. 1 root root  373K Mar  6 17:48 libUnrealInsights-SlateFileDialogs.sym
-rw-r--r--. 1 root root   28M Mar  6 17:48 libUnrealInsights-SlateReflector.debug
-rwxr-xr-x. 1 root root  2.5M Mar  6 17:48 libUnrealInsights-SlateReflector.so
-rw-r--r--. 1 root root  1.8M Mar  6 17:48 libUnrealInsights-SlateReflector.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:48 libUnrealInsights-Sockets.debug
-rwxr-xr-x. 1 root root  189K Mar  6 17:48 libUnrealInsights-Sockets.so
-rw-r--r--. 1 root root  149K Mar  6 17:48 libUnrealInsights-Sockets.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:48 libUnrealInsights-SourceCodeAccess.debug
-rwxr-xr-x. 1 root root   51K Mar  6 17:48 libUnrealInsights-SourceCodeAccess.so
-rw-r--r--. 1 root root   32K Mar  6 17:48 libUnrealInsights-SourceCodeAccess.sym
-rw-r--r--. 1 root root  8.9M Mar  6 17:48 libUnrealInsights-StandaloneRenderer.debug
-rwxr-xr-x. 1 root root  1.7M Mar  6 17:48 libUnrealInsights-StandaloneRenderer.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:48 libUnrealInsights-StandaloneRenderer.sym
-rw-r--r--. 1 root root  3.5M Mar  6 17:48 libUnrealInsights-TraceAnalysis.debug
-rwxr-xr-x. 1 root root  912K Mar  6 17:48 libUnrealInsights-TraceAnalysis.so
-rw-r--r--. 1 root root  471K Mar  6 17:48 libUnrealInsights-TraceAnalysis.sym
-rw-r--r--. 1 root root   87M Mar  6 17:49 libUnrealInsights-TraceInsights.debug
-rwxr-xr-x. 1 root root  7.5M Mar  6 17:49 libUnrealInsights-TraceInsights.so
-rw-r--r--. 1 root root  5.8M Mar  6 17:49 libUnrealInsights-TraceInsights.sym
-rw-r--r--. 1 root root  407K Mar  6 17:47 libUnrealInsights-TraceLog.debug
-rwxr-xr-x. 1 root root   85K Mar  6 17:47 libUnrealInsights-TraceLog.so
-rw-r--r--. 1 root root   12K Mar  6 17:47 libUnrealInsights-TraceLog.sym
-rw-r--r--. 1 root root   12M Mar  6 17:48 libUnrealInsights-TraceServices.debug
-rwxr-xr-x. 1 root root  778K Mar  6 17:48 libUnrealInsights-TraceServices.so
-rw-r--r--. 1 root root  915K Mar  6 17:48 libUnrealInsights-TraceServices.sym
-rw-r--r--. 1 root root  580K Mar  6 17:48 libUnrealInsights-UnixCommonStartup.debug
-rwxr-xr-x. 1 root root   19K Mar  6 17:48 libUnrealInsights-UnixCommonStartup.so
-rw-r--r--. 1 root root  8.3K Mar  6 17:48 libUnrealInsights-UnixCommonStartup.sym
-rw-r--r--. 1 root root  738K Mar  6 17:48 libUnrealInsights-UnrealEdMessages.debug
-rwxr-xr-x. 1 root root   26K Mar  6 17:48 libUnrealInsights-UnrealEdMessages.so
-rw-r--r--. 1 root root   22K Mar  6 17:48 libUnrealInsights-UnrealEdMessages.sym
-rw-r--r--. 1 root root  644K Mar  6 17:48 libUnrealInsights-WorkspaceMenuStructure.debug
-rwxr-xr-x. 1 root root   31K Mar  6 17:48 libUnrealInsights-WorkspaceMenuStructure.so
-rw-r--r--. 1 root root   16K Mar  6 17:48 libUnrealInsights-WorkspaceMenuStructure.sym
-rw-r--r--. 1 root root  736K Mar  6 17:48 libUnrealInsights-XmlParser.debug
-rwxr-xr-x. 1 root root   51K Mar  6 17:48 libUnrealInsights-XmlParser.so
-rw-r--r--. 1 root root   33K Mar  6 17:48 libUnrealInsights-XmlParser.sym
-rw-r--r--. 1 root root  9.1M Mar  6 17:33 libUnrealLightmass-ApplicationCore.debug
-rwxr-xr-x. 1 root root  1.9M Mar  6 17:33 libUnrealLightmass-ApplicationCore.so
-rw-r--r--. 1 root root  1.4M Mar  6 17:33 libUnrealLightmass-ApplicationCore.sym
-rw-r--r--. 1 root root   17K Mar  6 17:32 libUnrealLightmass-BuildSettings.debug
-rwxr-xr-x. 1 root root  5.0K Mar  6 17:32 libUnrealLightmass-BuildSettings.so
-rw-r--r--. 1 root root   868 Mar  6 17:32 libUnrealLightmass-BuildSettings.sym
-rw-r--r--. 1 root root  1.1M Mar  6 17:33 libUnrealLightmass-Cbor.debug
-rwxr-xr-x. 1 root root   90K Mar  6 17:33 libUnrealLightmass-Cbor.so
-rw-r--r--. 1 root root   77K Mar  6 17:33 libUnrealLightmass-Cbor.sym
-rw-r--r--. 1 root root   91M Mar  6 17:33 libUnrealLightmass-Core.debug
-rwxr-xr-x. 1 root root   13M Mar  6 17:33 libUnrealLightmass-Core.so
-rw-r--r--. 1 root root  6.5M Mar  6 17:33 libUnrealLightmass-Core.sym
-rw-r--r--. 1 root root   65M Mar  6 17:33 libUnrealLightmass-CoreUObject.debug
-rwxr-xr-x. 1 root root  5.9M Mar  6 17:33 libUnrealLightmass-CoreUObject.so
-rw-r--r--. 1 root root  4.2M Mar  6 17:33 libUnrealLightmass-CoreUObject.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:33 libUnrealLightmass-Json.debug
-rwxr-xr-x. 1 root root  190K Mar  6 17:33 libUnrealLightmass-Json.so
-rw-r--r--. 1 root root  124K Mar  6 17:33 libUnrealLightmass-Json.sym
-rw-r--r--. 1 root root  3.9M Mar  6 17:33 libUnrealLightmass-Messaging.debug
-rwxr-xr-x. 1 root root  250K Mar  6 17:33 libUnrealLightmass-Messaging.so
-rw-r--r--. 1 root root  233K Mar  6 17:33 libUnrealLightmass-Messaging.sym
-rw-r--r--. 1 root root   32K Mar  6 17:33 libUnrealLightmass-NetCommon.debug
-rwxr-xr-x. 1 root root  6.9K Mar  6 17:33 libUnrealLightmass-NetCommon.so
-rw-r--r--. 1 root root  2.3K Mar  6 17:33 libUnrealLightmass-NetCommon.sym
-rw-r--r--. 1 root root  444K Mar  6 17:33 libUnrealLightmass-Networking.debug
-rwxr-xr-x. 1 root root   27K Mar  6 17:33 libUnrealLightmass-Networking.so
-rw-r--r--. 1 root root   13K Mar  6 17:33 libUnrealLightmass-Networking.sym
-rw-r--r--. 1 root root  4.9M Mar  6 17:33 libUnrealLightmass-Projects.debug
-rwxr-xr-x. 1 root root  378K Mar  6 17:33 libUnrealLightmass-Projects.so
-rw-r--r--. 1 root root  267K Mar  6 17:33 libUnrealLightmass-Projects.sym
-rw-r--r--. 1 root root  5.2M Mar  6 17:33 libUnrealLightmass-Serialization.debug
-rwxr-xr-x. 1 root root  415K Mar  6 17:33 libUnrealLightmass-Serialization.so
-rw-r--r--. 1 root root  352K Mar  6 17:33 libUnrealLightmass-Serialization.sym
-rw-r--r--. 1 root root  2.1M Mar  6 17:33 libUnrealLightmass-Sockets.debug
-rwxr-xr-x. 1 root root  189K Mar  6 17:33 libUnrealLightmass-Sockets.so
-rw-r--r--. 1 root root  149K Mar  6 17:33 libUnrealLightmass-Sockets.sym
-rw-r--r--. 1 root root  1.9M Mar  6 17:33 libUnrealLightmass-SwarmInterface.debug
-rwxr-xr-x. 1 root root  172K Mar  6 17:33 libUnrealLightmass-SwarmInterface.so
-rw-r--r--. 1 root root  165K Mar  6 17:33 libUnrealLightmass-SwarmInterface.sym
-rw-r--r--. 1 root root  407K Mar  6 17:32 libUnrealLightmass-TraceLog.debug
-rwxr-xr-x. 1 root root   85K Mar  6 17:32 libUnrealLightmass-TraceLog.so
-rw-r--r--. 1 root root   12K Mar  6 17:32 libUnrealLightmass-TraceLog.sym
-rw-r--r--. 1 root root  2.2M Mar  6 17:34 libtbb.so.2
```
3/6/2023 2:32:19 PM: create nsambhu account before copying the UnrealEngine_4.26 folder. Delete container image before starting. 
```
STEP 33/37: RUN ./Setup.sh 
Registering git hooks... (this will override existing ones!)
./Setup.sh: line 30: .git/hooks/post-checkout: Permission denied
Error: error building at STEP "RUN ./Setup.sh": error while running runtime: exit status 1
0625dd24bf07b19625a9570379a2a755e555248ee31eaebca55f219651ec8eb4
```
3/6/2023 2:36:20 PM: see where "UnrealEngine_4.26" folder exists in container now that nsambhu user exists.
```
STEP 33/39: RUN pwd
/home/nsambhu/UnrealEngine_4.26
--> bc2e7a53c9d
STEP 34/39: RUN ls -lh
total 48K
drwxrwxr-x. 11 root root  144 Feb 21 20:39 Engine
-rwxrwxr-x.  1 root root  660 Feb 21 20:39 GenerateProjectFiles.bat
-rwxrwxr-x.  1 root root  231 Feb 21 20:39 GenerateProjectFiles.command
-rwxrwxr-x.  1 root root  736 Feb 21 20:39 GenerateProjectFiles.sh
-rw-rw-r--.  1 root root  195 Feb 21 20:39 LICENSE.md
-rw-rw-r--.  1 root root 9.5K Feb 21 20:39 README.md
drwxrwxr-x.  4 root root   56 Feb 21 20:39 Samples
-rwxrwxr-x.  1 root root 1.3K Feb 21 20:39 Setup.bat
-rwxrwxr-x.  1 root root  198 Feb 21 20:39 Setup.command
-rwxrwxr-x.  1 root root 1.7K Feb 21 20:39 Setup.sh
drwxrwxr-x. 42 root root 4.0K Feb 21 20:39 Templates
-rw-rw-r--.  1 root root  269 Feb 21 20:39 UE4Games.uprojectdirs
```
3/6/2023 2:43:13 PM: get Setup.sh to run. Try root user before running script.  
3/6/2023 3:05:31 PM: Setup.sh runs with root user in nsaambhu home directory.  
3/6/2023 3:07:26 PM: modify Dockerfile to cd into directory and run UE4Editor.  
3/6/2023 3:44:27 PM: error
```
STEP 39/39: RUN ./UE4Editor
/bin/sh: 1: ./UE4Editor: not found
```
3/6/2023 3:44:54 PM: find UE4Editor  
```
STEP 38/42: RUN cd $HOME/UnrealEngine_4.26/Engine/Binaries/Linux 
--> Using cache 93c02d4c2863ac72d455f7e57967e332f67e2787265860da1d73ace362088e12
--> 93c02d4c286
STEP 39/42: RUN pwd && echo ""
/home/nsambhu/UnrealEngine_4.26

--> 0741731ab0f
STEP 40/42: RUN ls -lh
total 4.7M
-rw-r--r--. 1 root root  57K Mar  6 20:07 CMakeLists.txt
drwxrwxr-x. 1 root root  100 Mar  6 20:06 Engine
drwxr-xr-x. 2 root root 4.0K Mar  6 19:49 FeaturePacks
-rwxrwxr-x. 1 root root  660 Feb 21 20:39 GenerateProjectFiles.bat
-rwxrwxr-x. 1 root root  231 Feb 21 20:39 GenerateProjectFiles.command
-rwxrwxr-x. 1 root root  736 Feb 21 20:39 GenerateProjectFiles.sh
-rw-rw-r--. 1 root root  195 Feb 21 20:39 LICENSE.md
-rw-r--r--. 1 root root  29K Mar  6 20:06 Makefile
-rw-rw-r--. 1 root root 9.5K Feb 21 20:39 README.md
drwxrwxr-x. 1 root root   56 Feb 21 20:39 Samples
-rwxrwxr-x. 1 root root 1.3K Feb 21 20:39 Setup.bat
-rwxrwxr-x. 1 root root  198 Feb 21 20:39 Setup.command
-rwxrwxr-x. 1 root root 1.7K Feb 21 20:39 Setup.sh
drwxrwxr-x. 1 root root 4.0K Mar  6 19:48 Templates
-rw-r--r--. 1 root root  271 Mar  6 20:06 UE4.code-workspace
-rw-r--r--. 1 root root   52 Mar  6 20:06 UE4.kdev4
-rw-r--r--. 1 root root  30K Mar  6 20:07 UE4.pro
-rw-r--r--. 1 root root 482K Mar  6 20:07 UE4.workspace
-rw-r--r--. 1 root root 371K Mar  6 20:07 UE4CodeCompletionFolders.txt
-rw-r--r--. 1 root root    0 Mar  6 20:07 UE4CodeLitePreProcessor.txt
-rw-r--r--. 1 root root 148K Mar  6 20:07 UE4Config.pri
-rw-r--r--. 1 root root   13 Mar  6 20:07 UE4Defines.pri
-rw-rw-r--. 1 root root  269 Feb 21 20:39 UE4Games.uprojectdirs
-rw-r--r--. 1 root root 1.9M Mar  6 20:07 UE4Header.pri
-rw-r--r--. 1 root root 241K Mar  6 20:07 UE4Includes.pri
-rw-r--r--. 1 root root 1.5M Mar  6 20:07 UE4Source.pri
-rw-r--r--. 1 root root  456 Mar  6 19:46 cpp.hint
--> 6387dad3915
STEP 41/42: RUN ls -lh $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/
total 9.1G
-rw-r--r--. 1 root root   12K Mar  6 20:12 AgentInterface.dll
drwxr-xr-x. 2 root root  4.0K Mar  6 20:27 Android
-rwxr-xr-x. 1 root root 1002K Mar  6 19:47 BreakpadSymbolEncoder
-rwxr-xr-x. 1 root root   61K Mar  6 19:47 BreakpadSymbolEncoder.exe
-rwxr-xr-x. 1 root root   27M Mar  6 20:11 CrashReportClient
-rw-r--r--. 1 root root   31K Mar  6 20:11 CrashReportClient-Linux-Shipping.target
-rw-r--r--. 1 root root  252M Mar  6 20:11 CrashReportClient.debug
-rw-r--r--. 1 root root   14M Mar  6 20:11 CrashReportClient.sym
-rwxr-xr-x. 1 root root   27M Mar  6 20:11 CrashReportClientEditor
-rw-r--r--. 1 root root   31K Mar  6 20:11 CrashReportClientEditor-Linux-Shipping.target
-rw-r--r--. 1 root root  252M Mar  6 20:11 CrashReportClientEditor.debug
-rw-r--r--. 1 root root   14M Mar  6 20:11 CrashReportClientEditor.sym
drwxr-xr-x. 2 root root  4.0K Mar  6 20:27 Linux
-rwxr-xr-x. 1 root root  197K Mar  6 20:12 ShaderCompileWorker
-rw-r--r--. 1 root root  3.2M Mar  6 20:12 ShaderCompileWorker.debug
-rw-r--r--. 1 root root  1.8K Mar  6 20:12 ShaderCompileWorker.modules
-rw-r--r--. 1 root root  158K Mar  6 20:12 ShaderCompileWorker.sym
-rw-r--r--. 1 root root   41K Mar  6 20:12 ShaderCompileWorker.target
-rw-r--r--. 1 root root   253 Mar  6 20:12 ShaderCompileWorker.version
-rwxr-xr-x. 1 root root  495K Mar  6 20:26 UE4Editor
```
3/6/2023 3:51:30 PM: call UE4Editor path directly
```
STEP 38/38: RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor
Refusing to run with the root privileges.
Error: error building at STEP "RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor": error while running runtime: exit status 1
```
TOOD: change to user nsambhu  
3/6/2023 3:57:40 PM: 
```
STEP 39/39: RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor
sh: 1: xdg-user-dir: not found
- Existing per-process limit (soft=1024, hard=1024) is enough for us (need only 1024)
Increasing per-process limit of core file size to infinity.
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogTaskGraph: Started task graph with 5 named threads and 74 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.102375
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: +0:00, Platform Override: ''
LogUnixPlatformFile: Warning: create dir('/home/nsambhu/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/home/nsambhu/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
```
TODO: call xhost local:root from within the Dockerfile.  
3/6/2023 3:59:27 PM: error
```
STEP 39/40: RUN xhost local:root
/bin/sh: 1: xhost: not found
Error: error building at STEP "RUN xhost local:root": error while running runtime: exit status 127
```
3/6/2023 4:03:30 PM: keep nsambhu before running UE4Editor. Remove previous build layers.  
3/6/2023 5:06:26 PM: error persists:
```
STEP 39/39: RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor
sh: 1: xdg-user-dir: not found
- Existing per-process limit (soft=1024, hard=1024) is enough for us (need only 1024)
Increasing per-process limit of core file size to infinity.
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogTaskGraph: Started task graph with 5 named threads and 74 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.297184
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: +0:00, Platform Override: ''
LogUnixPlatformFile: Warning: create dir('/home/nsambhu/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/home/nsambhu/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
```
3/7/2023 9:45:18 AM: disk space full  
3/7/2023 11:35:22 AM: chmod following https://forums.unrealengine.com/t/error-compiling-ue4-on-fedora-24/70267/2  
3/7/2023 12:33:43 PM: refusing to run with root privileges
```
STEP 44/44: RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor
Refusing to run with the root privileges.
Error: error building at STEP "RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor": error while running runtime: exit status 1
52b82b5b3b60242aa8b565e4e64a8868ed1614e6a0f047c28fd54f2a1599b4aa
```
3/7/2023 12:37:46 PM: change root to nsambhu
```
STEP 47/47: RUN $HOME/UnrealEngine_4.26/Engine/Binaries/Linux/UE4Editor
sh: 1: xdg-user-dir: not found
- Existing per-process limit (soft=1024, hard=1024) is enough for us (need only 1024)
Increasing per-process limit of core file size to infinity.
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogTaskGraph: Started task graph with 5 named threads and 74 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.104102
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: +0:00, Platform Override: ''
LogUnixPlatformFile: Warning: create dir('/home/nsambhu/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/home/nsambhu/UnrealEngine_4.26/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
```
# Ubuntu CARLA build from source
3/7/2023 1:34:12 PM: create anaconda environment
```
(carla-source) nsambhu@SAMBHU19:~/UnrealEngine_4.26/Engine/Binaries/Linux$ ./UE4Editor
Increasing per-process limit of core file size to infinity.
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogTaskGraph: Started task graph with 5 named threads and 74 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.093163
LogInit: NumberOfWorkerThreadsToSpawn:
LogInit:  - Number of physical cores available for the process: 24
LogInit:  - Number of logical cores available for the process: 48
LogInit:  - Worker number by default: 23 (you can change this number with the command line parameter '-workersthreadpool X', for a max of 26 threads)
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: -5:00, Platform Override: ''
LogPluginManager: Mounting plugin MeshPainting
LogPluginManager: Mounting plugin XGEController
LogPluginManager: Mounting plugin LauncherChunkInstaller
LogPluginManager: Mounting plugin RiderSourceCodeAccess
LogPluginManager: Mounting plugin NullSourceCodeAccess
LogPluginManager: Mounting plugin PerforceSourceControl
LogPluginManager: Mounting plugin GitSourceControl
LogPluginManager: Mounting plugin VisualStudioCodeSourceCodeAccess
LogPluginManager: Mounting plugin SubversionSourceControl
LogPluginManager: Mounting plugin CodeLiteSourceCodeAccess
LogPluginManager: Mounting plugin PropertyAccessNode
LogPluginManager: Mounting plugin XCodeSourceCodeAccess
LogPluginManager: Mounting plugin AnimationSharing
LogPluginManager: Mounting plugin PlasticSourceControl
LogPluginManager: Mounting plugin CLionSourceCodeAccess
LogPluginManager: Mounting plugin PluginUtils
LogPluginManager: Mounting plugin KDevelopSourceCodeAccess
LogPluginManager: Mounting plugin EnvironmentQueryEditor
LogPluginManager: Mounting plugin AISupport
LogPluginManager: Mounting plugin UObjectPlugin
LogPluginManager: Mounting plugin ScreenshotTools
LogPluginManager: Mounting plugin CameraShakePreviewer
LogPluginManager: Mounting plugin LightPropagationVolume
LogPluginManager: Mounting plugin ActorSequence
LogPluginManager: Mounting plugin VisualStudioSourceCodeAccess
LogPluginManager: Mounting plugin MatineeToLevelSequence
LogPluginManager: Mounting plugin GameplayTagsEditor
LogPluginManager: Mounting plugin TemplateSequence
LogPluginManager: Mounting plugin CryptoKeys
LogPluginManager: Mounting plugin FacialAnimation
LogPluginManager: Mounting plugin LevelSequenceEditor
LogPluginManager: Mounting plugin AssetManagerEditor
LogPluginManager: Mounting plugin DataValidation
LogPluginManager: Mounting plugin CurveEditorTools
LogPluginManager: Mounting plugin SpeedTreeImporter
LogPluginManager: Mounting plugin PluginBrowser
LogPluginManager: Mounting plugin GeometryMode
LogPluginManager: Mounting plugin MacGraphicsSwitching
LogPluginManager: Mounting plugin Paper2D
LogPluginManager: Mounting plugin MobileLauncherProfileWizard
LogPluginManager: Mounting plugin MaterialAnalyzer
LogPluginManager: Mounting plugin LuminPlatformFeatures
LogPluginManager: Mounting plugin MagicLeap
LogPluginManager: Mounting plugin MagicLeapMedia
LogPluginManager: Mounting plugin MagicLeapPassableWorld
LogPluginManager: Mounting plugin MagicLeapLightEstimation
LogPluginManager: Mounting plugin MediaPlayerEditor
LogPluginManager: Mounting plugin ChaosCloth
LogPluginManager: Mounting plugin VariantManagerContent
LogPluginManager: Mounting plugin DatasmithContent
LogPluginManager: Mounting plugin CharacterAI
LogPluginManager: Mounting plugin MLSDK
LogPluginManager: Mounting plugin AndroidMedia
LogPluginManager: Mounting plugin ImgMedia
LogPluginManager: Mounting plugin WebMMedia
LogPluginManager: Mounting plugin MotoSynth
LogPluginManager: Mounting plugin ChaosSolverPlugin
LogPluginManager: Mounting plugin Niagara
LogPluginManager: Mounting plugin SkeletalReduction
LogPluginManager: Mounting plugin BackChannel
LogPluginManager: Mounting plugin MediaCompositing
LogPluginManager: Mounting plugin AvfMedia
LogPluginManager: Mounting plugin GeometryCache
LogPluginManager: Mounting plugin GeometryCollectionPlugin
LogPluginManager: Mounting plugin GeometryProcessing
LogPluginManager: Mounting plugin OnlineSubsystemUtils
LogPluginManager: Mounting plugin TcpMessaging
LogPluginManager: Mounting plugin UdpMessaging
LogPluginManager: Mounting plugin AutomationUtils
LogPluginManager: Mounting plugin PlanarCut
LogPluginManager: Mounting plugin AlembicImporter
LogPluginManager: Mounting plugin OnlineSubsystem
LogPluginManager: Mounting plugin PlatformCrypto
LogPluginManager: Mounting plugin OnlineSubsystemNull
LogPluginManager: Mounting plugin ProxyLODPlugin
LogPluginManager: Mounting plugin ChaosEditor
LogPluginManager: Mounting plugin ChaosNiagara
LogPluginManager: Mounting plugin Synthesis
LogPluginManager: Mounting plugin CustomMeshComponent
LogPluginManager: Mounting plugin WmfMedia
LogPluginManager: Mounting plugin LocationServicesBPLibrary
LogPluginManager: Mounting plugin CableComponent
LogPluginManager: Mounting plugin PhysXVehicles
LogPluginManager: Mounting plugin GoogleCloudMessaging
LogPluginManager: Mounting plugin ProceduralMeshComponent
LogPluginManager: Mounting plugin IOSDeviceProfileSelector
LogPluginManager: Mounting plugin EditableMesh
LogPluginManager: Mounting plugin SoundFields
LogPluginManager: Mounting plugin ActorLayerUtilities
LogPluginManager: Mounting plugin SignificanceManager
LogPluginManager: Mounting plugin PropertyAccessEditor
LogPluginManager: Mounting plugin AudioSynesthesia
LogPluginManager: Mounting plugin PostSplashScreen
LogPluginManager: Mounting plugin ExampleDeviceProfileSelector
LogPluginManager: Mounting plugin AppleMoviePlayer
LogPluginManager: Mounting plugin AppleImageUtils
LogPluginManager: Mounting plugin GooglePAD
LogPluginManager: Mounting plugin MobilePatchingUtils
LogPluginManager: Mounting plugin AndroidMoviePlayer
LogPluginManager: Mounting plugin AudioCapture
LogPluginManager: Mounting plugin WindowsMoviePlayer
LogPluginManager: Mounting plugin ChaosClothEditor
LogPluginManager: Mounting plugin ChunkDownloader
LogPluginManager: Mounting plugin AndroidPermission
LogPluginManager: Mounting plugin WebMMoviePlayer
LogPluginManager: Mounting plugin RuntimePhysXCooking
LogPluginManager: Mounting plugin AndroidDeviceProfileSelector
LogPluginManager: Mounting plugin AssetTags
LogPluginManager: Mounting plugin LinuxDeviceProfileSelector
LogPluginManager: Mounting plugin ArchVisCharacter
LogPluginManager: Mounting plugin ContentBrowserAssetDataSource
LogPluginManager: Mounting plugin ContentBrowserClassDataSource
LogPluginManager: Mounting plugin OnlineSubsystemGooglePlay
LogPluginManager: Mounting plugin OnlineSubsystemIOS
LogPluginManager: Mounting plugin OculusVR
LogPluginManager: Mounting plugin SteamVR
LogInit: Using libcurl 7.65.3-DEV
LogInit:  - built for x86_64-unknown-linux-gnu
LogInit:  - supports SSL with OpenSSL/1.1.1c
LogInit:  - supports HTTP deflate (compression) using libz 1.2.8
LogInit:  - other features:
LogInit:      CURL_VERSION_SSL
LogInit:      CURL_VERSION_LIBZ
LogInit:      CURL_VERSION_IPV6
LogInit:      CURL_VERSION_ASYNCHDNS
LogInit:      CURL_VERSION_LARGEFILE
LogInit:      CURL_VERSION_TLSAUTH_SRP
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit:  - bVerifyPeer = true  - Libcurl will verify peer certificate
LogInit:  - bUseHttpProxy = false  - Libcurl will NOT use HTTP proxy
LogInit:  - bDontReuseConnections = false  - Libcurl will reuse connections
LogInit:  - MaxHostConnections = 16  - Libcurl will limit the number of connections to a host
LogInit:  - LocalHostAddr = Default
LogInit:  - BufferSize = 65536
LogOnline: OSS: Creating online subsystem instance for: NULL
LogOnline: OSS: TryLoadSubsystemAndSetDefault: Loaded subsystem for module [NULL]
LogInit: Build: ++UE4+Release-4.26-CL-0
LogInit: Engine Version: 4.26.2-0+++UE4+Release-4.26
LogInit: Compatible Engine Version: 4.26.0-0+++UE4+Release-4.26
LogInit: Net CL: 0
LogInit: OS: GenericOSVersionLabel (GenericOSSubVersionLabel), CPU: AMD Ryzen Threadripper 3960X 24-Core Processor , GPU: GenericGPUBrand
LogInit: Compiled (64-bit): Mar  7 2023 19:28:56
LogInit: Compiled with Clang: 10.0.1 
LogInit: Build Configuration: Development
LogInit: Branch Name: ++UE4+Release-4.26
LogInit: Command Line: 
LogInit: Base Directory: /home/nsambhu/UnrealEngine_4.26/Engine/Binaries/Linux/
LogInit: Allocator: binned2
LogInit: Installed Engine Build: 0
LogDevObjectVersion: Number of dev versions registered: 29
LogDevObjectVersion:   Dev-Blueprints (B0D832E4-1F89-4F0D-ACCF-7EB736FD4AA2): 10
LogDevObjectVersion:   Dev-Build (E1C64328-A22C-4D53-A36C-8E866417BD8C): 0
LogDevObjectVersion:   Dev-Core (375EC13C-06E4-48FB-B500-84F0262A717E): 4
LogDevObjectVersion:   Dev-Editor (E4B068ED-F494-42E9-A231-DA0B2E46BB41): 40
LogDevObjectVersion:   Dev-Framework (CFFC743F-43B0-4480-9391-14DF171D2073): 37
LogDevObjectVersion:   Dev-Mobile (B02B49B5-BB20-44E9-A304-32B752E40360): 3
LogDevObjectVersion:   Dev-Networking (A4E4105C-59A1-49B5-A7C5-40C4547EDFEE): 0
LogDevObjectVersion:   Dev-Online (39C831C9-5AE6-47DC-9A44-9C173E1C8E7C): 0
LogDevObjectVersion:   Dev-Physics (78F01B33-EBEA-4F98-B9B4-84EACCB95AA2): 4
LogDevObjectVersion:   Dev-Platform (6631380F-2D4D-43E0-8009-CF276956A95A): 0
LogDevObjectVersion:   Dev-Rendering (12F88B9F-8875-4AFC-A67C-D90C383ABD29): 44
LogDevObjectVersion:   Dev-Sequencer (7B5AE74C-D270-4C10-A958-57980B212A5A): 12
LogDevObjectVersion:   Dev-VR (D7296918-1DD6-4BDD-9DE2-64A83CC13884): 3
LogDevObjectVersion:   Dev-LoadTimes (C2A15278-BFE7-4AFE-6C17-90FF531DF755): 1
LogDevObjectVersion:   Private-Geometry (6EACA3D4-40EC-4CC1-B786-8BED09428FC5): 3
LogDevObjectVersion:   Dev-AnimPhys (29E575DD-E0A3-4627-9D10-D276232CDCEA): 17
LogDevObjectVersion:   Dev-Anim (AF43A65D-7FD3-4947-9873-3E8ED9C1BB05): 15
LogDevObjectVersion:   Dev-ReflectionCapture (6B266CEC-1EC7-4B8F-A30B-E4D90942FC07): 1
LogDevObjectVersion:   Dev-Automation (0DF73D61-A23F-47EA-B727-89E90C41499A): 1
LogDevObjectVersion:   FortniteMain (601D1886-AC64-4F84-AA16-D3DE0DEAC7D6): 43
LogDevObjectVersion:   FortniteRelease (E7086368-6B23-4C58-8439-1B7016265E91): 1
LogDevObjectVersion:   Dev-Enterprise (9DFFBCD6-494F-0158-E221-12823C92A888): 10
LogDevObjectVersion:   Dev-Niagara (F2AED0AC-9AFE-416F-8664-AA7FFA26D6FC): 1
LogDevObjectVersion:   Dev-Destruction (174F1F0B-B4C6-45A5-B13F-2EE8D0FB917D): 10
LogDevObjectVersion:   Dev-Physics-Ext (35F94A83-E258-406C-A318-09F59610247C): 40
LogDevObjectVersion:   Dev-PhysicsMaterial-Chaos (B68FC16E-8B1B-42E2-B453-215C058844FE): 1
LogDevObjectVersion:   Dev-CineCamera (B2E18506-4273-CFC2-A54E-F4BB758BBA07): 1
LogDevObjectVersion:   Dev-VirtualProduction (64F58936-FD1B-42BA-BA96-7289D5D0FA4E): 1
LogDevObjectVersion:   Dev-MediaFramework (6F0ED827-A609-4895-9C91-998D90180EA4): 2
LogInit: Presizing for max 25165824 objects, including 0 objects not considered by GC, pre-allocating 0 bytes for permanent pool.
LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
LogInit: Object subsystem initialized
LogConfig: Setting CVar [[con.DebugEarlyDefault:1]]
LogConfig: Setting CVar [[r.setres:1280x720]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[r.VSync:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[r.RHICmdBypass:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[r.GPUCrashDebugging:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererOverrideSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.35:969][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.GarbageCollectionSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.MaxObjectsNotConsideredByGC:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.SizeOfPermanentObjectPool:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.FlushStreamingOnGC:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.NumRetriesBeforeForcingGC:10]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.AllowParallelGC:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.TimeBetweenPurgingPendingKillObjects:61.1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.MaxObjectsInEditor:25165824]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.IncrementalBeginDestroyEnabled:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.CreateGCClusters:1]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.MinGCClusterSize:5]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.ActorClusteringEnabled:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.BlueprintClusteringEnabled:0]]
[2023.03.08-02.06.35:969][  0]LogConfig: Setting CVar [[gc.UseDisregardForGCOnDedicatedServers:0]]
[2023.03.08-02.06.35:970][  0]LogConfig: Setting CVar [[gc.MultithreadedDestructionEnabled:1]]
[2023.03.08-02.06.35:970][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.NetworkSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.35:970][  0]LogConfig: Applying CVar settings from Section [/Script/UnrealEd.CookerSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.35:970][  0]LogInit: Initializing SDL.
[2023.03.08-02.06.36:237][  0]LogInit: Initialized SDL 2.0.12 revision: 13609 (hg-13609:34cc7d3b69d3) (compiled against 2.0.12)
[2023.03.08-02.06.36:237][  0]LogInit: Using SDL video driver 'x11'
[2023.03.08-02.06.36:238][  0]LogInit: Display metrics:
[2023.03.08-02.06.36:238][  0]LogInit:   PrimaryDisplayWidth: 1920
[2023.03.08-02.06.36:238][  0]LogInit:   PrimaryDisplayHeight: 1080
[2023.03.08-02.06.36:238][  0]LogInit:   PrimaryDisplayWorkAreaRect:
[2023.03.08-02.06.36:238][  0]LogInit:     Left=67, Top=27, Right=1920, Bottom=1080
[2023.03.08-02.06.36:238][  0]LogInit:   VirtualDisplayRect:
[2023.03.08-02.06.36:238][  0]LogInit:     Left=67, Top=27, Right=1920, Bottom=1080
[2023.03.08-02.06.36:238][  0]LogInit:   TitleSafePaddingSize: X=0.000 Y=0.000 Z=0.000 W=0.000
[2023.03.08-02.06.36:238][  0]LogInit:   ActionSafePaddingSize: X=0.000 Y=0.000 Z=0.000 W=0.000
[2023.03.08-02.06.36:238][  0]LogInit:   Number of monitors: 1
[2023.03.08-02.06.36:238][  0]LogInit:     Monitor 0
[2023.03.08-02.06.36:238][  0]LogInit:       Name: Sceptre E24 24"
[2023.03.08-02.06.36:238][  0]LogInit:       ID: display0
[2023.03.08-02.06.36:238][  0]LogInit:       NativeWidth: 1920
[2023.03.08-02.06.36:238][  0]LogInit:       NativeHeight: 1080
[2023.03.08-02.06.36:238][  0]LogInit:       bIsPrimary: true
[2023.03.08-02.06.36:238][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2023.03.08-02.06.36:238][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2023.03.08-02.06.36:238][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2023.03.08-02.06.36:238][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2023.03.08-02.06.36:239][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2023.03.08-02.06.36:239][  0]LogLinux: Selected Device Profile: [Linux]
[2023.03.08-02.06.36:239][  0]LogInit: Applying CVar settings loaded from the selected device profile: [Linux]
[2023.03.08-02.06.36:239][  0]LogHAL: Display: Platform has ~ 4 GB [67345293312 / 4294967296 / 63], which maps to Smallest [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
[2023.03.08-02.06.36:239][  0]LogInit: Going up to parent DeviceProfile []
[2023.03.08-02.06.36:239][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2023.03.08-02.06.36:239][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2023.03.08-02.06.36:240][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2023.03.08-02.06.36:240][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2023.03.08-02.06.36:240][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2023.03.08-02.06.36:241][  0]LogConfig: Applying CVar settings from Section [Startup] File [../../../Engine/Config/ConsoleVariables.ini]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[net.UseAdaptiveNetUpdateFrequency:0]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[p.chaos.AllowCreatePhysxBodies:1]]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[fx.SkipVectorVMBackendOptimizations:1]]
[2023.03.08-02.06.36:241][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2023.03.08-02.06.36:241][  0]LogConfig: Setting CVar [[g.TimeoutForBlockOnRenderFence:60000]]
[2023.03.08-02.06.36:241][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Editor.ini]
[2023.03.08-02.06.36:241][  0]LogInit: Unix hardware info:
[2023.03.08-02.06.36:241][  0]LogInit:  - we are the first instance of this executable
[2023.03.08-02.06.36:241][  0]LogInit:  - this process' id (pid) is 43189, parent process' id (ppid) is 97147
[2023.03.08-02.06.36:241][  0]LogInit:  - we are not running under debugger
[2023.03.08-02.06.36:241][  0]LogInit:  - machine network name is 'SAMBHU19'
[2023.03.08-02.06.36:241][  0]LogInit:  - user name is 'nsambhu' (nsambhu)
[2023.03.08-02.06.36:241][  0]LogInit:  - we're logged in locally
[2023.03.08-02.06.36:241][  0]LogInit:  - we're running with rendering
[2023.03.08-02.06.36:241][  0]LogInit:  - CPU: AuthenticAMD 'AMD Ryzen Threadripper 3960X 24-Core Processor ' (signature: 0x830F10)
[2023.03.08-02.06.36:241][  0]LogInit:  - Number of physical cores available for the process: 24
[2023.03.08-02.06.36:241][  0]LogInit:  - Number of logical cores available for the process: 48
[2023.03.08-02.06.36:241][  0]LogInit:  - Cache line size: 64
[2023.03.08-02.06.36:241][  0]LogInit:  - Memory allocator used: binned2
[2023.03.08-02.06.36:241][  0]LogInit:  - This binary is optimized with LTO: no, PGO: no, instrumented for PGO data collection: no
[2023.03.08-02.06.36:241][  0]LogInit:  - This is an internal build.
[2023.03.08-02.06.36:241][  0]LogCore: Benchmarking clocks:
[2023.03.08-02.06.36:241][  0]LogCore:  - CLOCK_MONOTONIC (id=1) can sustain 46459952 (46460K, 46M) calls per second without zero deltas.
[2023.03.08-02.06.36:241][  0]LogCore:  - CLOCK_MONOTONIC_RAW (id=4) can sustain 46478075 (46478K, 46M) calls per second without zero deltas.
[2023.03.08-02.06.36:241][  0]LogCore:  - CLOCK_MONOTONIC_COARSE (id=6) can sustain 238650612 (238651K, 239M) calls per second with 99.999891% zero deltas.
[2023.03.08-02.06.36:241][  0]LogCore: Selected clock_id 4 (CLOCK_MONOTONIC_RAW) since it is the fastest support clock without zero deltas.
[2023.03.08-02.06.36:241][  0]LogInit: Unix-specific commandline switches:
[2023.03.08-02.06.36:241][  0]LogInit:  -ansimalloc - use malloc()/free() from libc (useful for tools like valgrind and electric fence)
[2023.03.08-02.06.36:241][  0]LogInit:  -jemalloc - use jemalloc for all memory allocation
[2023.03.08-02.06.36:241][  0]LogInit:  -binnedmalloc - use binned malloc  for all memory allocation
[2023.03.08-02.06.36:241][  0]LogInit:  -filemapcachesize=NUMBER - set the size for case-sensitive file mapping cache
[2023.03.08-02.06.36:241][  0]LogInit:  -useksm - uses kernel same-page mapping (KSM) for mapped memory (OFF)
[2023.03.08-02.06.36:241][  0]LogInit:  -ksmmergeall - marks all mmap'd memory pages suitable for KSM (OFF)
[2023.03.08-02.06.36:241][  0]LogInit:  -preloadmodulesymbols - Loads the main module symbols file into memory (OFF)
[2023.03.08-02.06.36:241][  0]LogInit:  -sigdfl=SIGNAL - Allows a specific signal to be set to its default handler rather then ignoring the signal
[2023.03.08-02.06.36:241][  0]LogInit:  -httpproxy=ADDRESS:PORT - redirects HTTP requests to a proxy (only supported if compiled with libcurl)
[2023.03.08-02.06.36:241][  0]LogInit:  -reuseconn - allow libcurl to reuse HTTP connections (only matters if compiled with libcurl)
[2023.03.08-02.06.36:241][  0]LogInit:  -virtmemkb=NUMBER - sets process virtual memory (address space) limit (overrides VirtualMemoryLimitInKB value from .ini)
[2023.03.08-02.06.36:241][  0]LogInit:  - Physical RAM available (not considering process quota): 63 GB (64225 MB, 65766888 KB, 67345293312 bytes)
[2023.03.08-02.06.36:242][  0]LogInit:  - VirtualMemoryAllocator pools will grow at scale 1.4
[2023.03.08-02.06.36:242][  0]LogInit:  - MemoryRangeDecommit() will be a no-op (re-run with -vmapoolevict to change)
[2023.03.08-02.06.36:261][  0]LogInit: Physics initialised using underlying interface: PhysX
[2023.03.08-02.06.36:281][  0]LogInit: Using OS detected language (en-US).
[2023.03.08-02.06.36:281][  0]LogInit: Using OS detected locale (en-US).
[2023.03.08-02.06.36:282][  0]LogTextLocalizationManager: No specific localization for 'en-US' exists, so the 'en' localization will be used.
X Error of failed request:  BadValue (integer parameter out of range for operation)
  Major opcode of failed request:  152 (GLX)
  Minor opcode of failed request:  3 (X_GLXCreateContext)
  Value in failed request:  0x0
  Serial number of failed request:  161
  Current serial number in output stream:  162
terminating with uncaught exception of type std::__1::system_error: mutex lock failed: Invalid argument
Signal 6 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
CommonUnixCrashHandler: Signal=6
Segmentation fault (core dumped)
```
TODO: get git authentication working for UnrealEngine_4.26 directory  
3/8/2023 11:12:19 AM: do TODO of git authentication on UnrealEngine_4.26  
3/8/2023 12:23:19 PM: git command to clone
```
git clone --depth 1 -b carla git@github.com:CarlaUnreal/UnrealEngine.git ~/UnrealEngine_4.26
```
3/8/2023 12:58:30 PM: Unreal Engine complete  
3/8/2023 1:27:56 PM: clone carla repository complete  
3/8/2023 2:05 PM: error: 'pyconfig.h' file not found
https://github.com/carla-simulator/carla/issues/199
```
sudo apt-get install python-dev
```
3/8/2023 2:08 PM: error persists  
3/8/2023 2:09 PM: comment anaconda in ~/.bashrc following https://github.com/carla-simulator/carla/issues/199#issuecomment-363036459  
3/8/2023 2:16 PM: try reboot  
3/8/2023 2:30 PM: 
```
Connecting to ftp.cixug.es (ftp.cixug.es)|193.144.61.75|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2023-03-08 14:22:44 ERROR 404: Not Found.

Util/BuildTools/Linux.mk:137: recipe for target 'setup' failed
make: *** [setup] Error 8
```
3/8/2023 2:33 PM: TODO: install system python packages.  
3/8/2023 2:33 PM: TODO: install system python 3.7.  
# Ubuntu CARLA build from source (reinstall)
3/13/2023 2:30:20 PM: Ubuntu installed, cuda toolkit installed, anaconda installed.  
3/13/2023 3:40 PM: need to use system python: https://github.com/carla-simulator/carla/issues/199  
3/13/2023 3:56 PM: configure system python3.6: https://askubuntu.com/a/1157104  
3/13/2023 4:20 PM: get carla make to work: https://github.com/carla-simulator/carla/issues/199#issuecomment-573385818  
3/14/2023 11:54 AM: carla make PythonAPI solution to pyconfig.h: https://stackoverflow.com/a/57244837  
3/14/2023 11:55 AM: 
```
Setup.sh: rpclib-v2.2.1_c5-c8 already installed.
Setup.sh: gtest-1.8.1-c8 already installed.
Setup.sh: recast-0b13b0-c8 already installed.
Setup.sh: Libpng already installed.
Setup.sh: Retrieving xerces-c.
--2023-03-14 11:53:29--  https://ftp.cixug.es/apache//xerces/c/3/sources/xerces-c-3.2.3.tar.gz
Resolving ftp.cixug.es (ftp.cixug.es)... 193.144.61.75
Connecting to ftp.cixug.es (ftp.cixug.es)|193.144.61.75|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2023-03-14 11:53:30 ERROR 404: Not Found.

Util/BuildTools/Linux.mk:137: recipe for target 'setup' failed
make: *** [setup] Error 8
```
3/14/2023 12:04 PM: implement solution https://github.com/carla-simulator/carla/issues/5846#issue-1413301411  
3/14/2023 12:16 PM: make launch failed
```
nsambhu@SAMBHU19:~/github/carla$ make launch
Setup.sh: llvm-8.0 already installed.
Setup.sh: boost-1.72.0-c8 already installed.
Setup.sh: rpclib-v2.2.1_c5-c8 already installed.
Setup.sh: gtest-1.8.1-c8 already installed.
Setup.sh: recast-0b13b0-c8 already installed.
Setup.sh: Libpng already installed.
Setup.sh: Xerces-c already installed.
cp: cannot create regular file '/home/nsambhu/github/carla/PythonAPI/carla/dependencies/lib/libxerces-c.a': Permission denied
Util/BuildTools/Linux.mk:137: recipe for target 'setup' failed
make: *** [setup] Error 1
```
```
nsambhu@SAMBHU19:~/github/carla$ sudo make launch
Setup.sh: llvm-8.0 already installed.
Setup.sh: boost-1.72.0-c8 already installed.
Setup.sh: rpclib-v2.2.1_c5-c8 already installed.
Setup.sh: gtest-1.8.1-c8 already installed.
Setup.sh: recast-0b13b0-c8 already installed.
Setup.sh: Libpng already installed.
Setup.sh: Xerces-c already installed.
Setup.sh: Sqlite already installed.
Setup.sh: PROJ already installed.
Setup.sh: Patchelf already installed.
Setup.sh: CARLA version 0.9.13-2-g99e3a78f7-dirty.
Setup.sh: Generating CMake configuration files.
Setup.sh: Success!
BuildLibCarla.sh: Building LibCarla "Server.Release" configuration.
ninja: no work to do.
[0/1] Install the project...
-- Install configuration: "Server"
BuildLibCarla.sh: Success!
BuildCarlaUE4.sh: ERROR: UE4_ROOT is not defined, or points to a non-existant directory, please set this environment variable.
Util/BuildTools/Linux.mk:7: recipe for target 'launch' failed
make: *** [launch] Error 2
```
3/14/2023 12:25 PM: change permissions
```
nsambhu@SAMBHU19:~/github$ sudo chmod -R 777 carla
```
3/14/2023 1:53 PM: carla add vehicle https://carla.readthedocs.io/en/0.9.13/tuto_A_add_vehicle/  
install Maya on Ubuntu:  https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/653FjR7SuamMJ5Y4v9XkXg.html  
```
nsambhu@SAMBHU19:~/github/carla$ sudo add-apt-repository ppa:zeehio/libxp
Traceback (most recent call last):
  File "/usr/bin/add-apt-repository", line 12, in <module>
    from softwareproperties.SoftwareProperties import SoftwareProperties, shortcut_handler
  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 28, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'
```
solution: https://stackoverflow.com/questions/13708180/python-dev-installation-error-importerror-no-module-named-apt-pkg  
"On Ubuntu 18.04, use this $ cd /usr/lib/python3/dist-packages $ sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.so"  
3/14/2023 2:03 PM:
```
nsambhu@SAMBHU19:/usr/lib/python3/dist-packages$ sudo add-apt-repository ppa:zeehio/libxp
Traceback (most recent call last):
  File "/usr/bin/add-apt-repository", line 12, in <module>
    from softwareproperties.SoftwareProperties import SoftwareProperties, shortcut_handler
  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 67, in <module>
    from gi.repository import Gio
  File "/usr/lib/python3/dist-packages/gi/__init__.py", line 42, in <module>
    from . import _gi
ImportError: cannot import name '_gi' from 'gi' (/usr/lib/python3/dist-packages/gi/__init__.py)
```
3/14/2023 2:08 PM: solution: https://stackoverflow.com/a/62672285  
## Blender (Maya alternative)
3/15/2023 12:58 PM: https://www.blender.org/download/  
3/15/2023 2:20 PM: TODO: get vehicle mesh  
3/16/2023 11:48 PM: add vehicle in CARLA: https://youtu.be/0F3ugwkISGk  
3/16/2023 12:33 PM: tutorial of mesh export from Unreal to Blender: https://youtu.be/iDz7X2RZDvM?t=314  
~3/16/2023 12:55:32 PM: tutorial on Carla Unreal and Blender: https://www.youtube.com/watch?v=ISOSVlrmVq4~  
3/16/2023 1:10:12 PM: export FBX: https://www.youtube.com/watch?v=fDmxIRV-j5g (source: https://bitbucket.org/yankagan/carla-content/wiki/Home )  
3/16/2023 1:35:54 PM: TODO: bind bones following https://carla.readthedocs.io/en/0.9.13/tuto_A_add_vehicle/  
3/16/2023 1:48:13 PM: TODO: blender bind bones understanding following https://www.youtube.com/watch?v=cRlb9tncJok  
3/16/2023 2:06:21 PM: follow carla tutorial on making a vehicle: https://carla.readthedocs.io/en/latest/tuto_content_authoring_vehicles/  
3/16/2023 4:05 PM: Blender to Unreal tutorial: https://www.youtube.com/watch?v=t9Y7YCexaGU  
3/23/2023 2:07 PM: find different methods of exporting vehicle from Unreal Engine. Goal: import vehicle model with availability to select wheels.  
3/23/2023 4:23:44 PM: material customization documentation: https://carla.readthedocs.io/en/0.9.13/tuto_A_material_customization/  
# Reinstall Unreal Engine
3/25/2023 3:29:59 PM: git clone command
```
git clone --depth 1 -b carla git@github.com:CarlaUnreal/UnrealEngine.git ~/UnrealEngine_4.26
```
