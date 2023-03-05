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
