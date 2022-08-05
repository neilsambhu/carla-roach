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