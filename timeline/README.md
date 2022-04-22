4/18/2022 4:28:42 PM: initial commit

4/18/2022 5:04:22 PM: anchor links sandbox start 
# example
4/18/2022 5:07:42 PM: anchor links sandbox end

4/18/2022 5:09:15 PM: start install using [INSTALL.md](../doc/INSTALL.md)

4/18/2022 5:10:48 PM: I'm going to try and use (1) CARLA 0.9.13 instead of (2) CARLA 0.9.11 as used in carla-roach

4/18/2022 5:18:43 PM: "wandb login" done

4/21/2022 11:32:07 AM: check arguments in "run/data_collect_bc.sh"

4/21/2022 11:57:39 AM: 
```
Traceback (most recent call last):
  File "data_collect.py", line 20, in <module>
    from agents.rl_birdview.utils.wandb_callback import WandbCallback
ModuleNotFoundError: No module named 'agents.rl_birdview'
```
"touch agents/__init__.py" resolved the issue

4/21/2022 12:04:53 PM:
```
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
[2022-04-21 11:58:27,057][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-21 11:58:27,977][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
[2022-04-21 11:58:29,630][__main__][INFO] - Start from env_idx: 0, task_idx 0
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/pathlib.py", line 1273, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/home/ubuntu/dataset/bc'
```
4/21/2022 12:05:32 PM: potential solution: create directory "carla-roach/dataset_root"

4/21/2022 1:20:03 PM:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh 
```
I'm not sure if this ran successfully. 

4/21/2022 1:20:44 PM: https://github.com/neilsambhu/carla-roach#benchmark > benchmark checkpoints

4/21/2022 8:55:59 PM: 
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh 
```
$ PYTHON_RETURN=1!!! Start Over!!!$

I'm going to see how python returns an int in a shell script.

4/21/2022 9:08:17 PM:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh 
run/data_collect_bc_NeilBranch0.sh: 47: run/data_collect_bc_NeilBranch0.sh: source: not found

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


rm: cannot remove 'outputs/checkpoint.txt': No such file or directory
rm: cannot remove 'outputs/wb_run_id.txt': No such file or directory
rm: cannot remove 'outputs/ep_stat_buffer_*.json': No such file or directory
run/data_collect_bc_NeilBranch0.sh: 59: [: 1: unexpected operator
Neil start here 1
/opt/carla-simulator/CarlaUE4.sh: line 2: 82126 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-21 21:03:04,099][utils.server_utils][INFO] - Kill Carla Servers!
CarlaUE4-Linux: no process found
[2022-04-21 21:03:05,113][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-21 21:03:05,113][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
[2022-04-21 21:03:10,707][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-21 21:03:11,464][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
[2022-04-21 21:03:12,920][__main__][INFO] - Start from env_idx: 0, task_idx 0
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run dataset_root/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/1knfon0k
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-21/21-03-02/wandb/run-20220421_210313-1knfon0k
wandb: Run `wandb offline` to turn off syncing.

/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
[2022-04-21 21:03:18,454][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 283, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 49, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 74, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles'])
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 35, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter))
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 377, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 83083
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-21/21-03-02/wandb/run-20220421_210313-1knfon0k/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-21/21-03-02/wandb/run-20220421_210313-1knfon0k/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced dataset_root/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/1knfon0k
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/21/2022 9:14:26 PM: I created "/home/ubuntu/dataset/bc" to account for default of "dataset_root=/home/ubuntu/dataset/bc" in "data_collect_bc.sh".

4/21/2022 9:16:35 PM:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh 
run/data_collect_bc_NeilBranch0.sh: 47: run/data_collect_bc_NeilBranch0.sh: source: not found

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


rm: cannot remove 'outputs/checkpoint.txt': No such file or directory
rm: cannot remove 'outputs/ep_stat_buffer_*.json': No such file or directory
run/data_collect_bc_NeilBranch0.sh: 59: [: 1: unexpected operator
Neil start here 1
/opt/carla-simulator/CarlaUE4.sh: line 2: 82816 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-21 21:15:03,880][utils.server_utils][INFO] - Kill Carla Servers!
CarlaUE4-Linux: no process found
[2022-04-21 21:15:04,893][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-21 21:15:04,894][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
[2022-04-21 21:15:10,213][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-21 21:15:11,036][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
[2022-04-21 21:15:12,368][__main__][INFO] - Start from env_idx: 0, task_idx 0
Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 233, in main
    dataset_dir.mkdir(parents=True, exist_ok=True)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/pathlib.py", line 1273, in mkdir
    self._accessor.mkdir(self, mode)
PermissionError: [Errno 13] Permission denied: '/home/ubuntu/dataset/bc/expert'

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
[2022-04-21 21:15:12,436][wandb.sdk.internal.internal][INFO] - Internal process exited
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/21/2022 9:59:20 PM: solution attempt: run with "sudo" prefix
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sudo sh run/data_collect_bc_NeilBranch0.sh 
[sudo] password for nsambhu: 
run/data_collect_bc_NeilBranch0.sh: 47: run/data_collect_bc_NeilBranch0.sh: source: not found
run/data_collect_bc_NeilBranch0.sh: 48: run/data_collect_bc_NeilBranch0.sh: conda: not found
rm: cannot remove 'outputs/checkpoint.txt': No such file or directory
rm: cannot remove 'outputs/wb_run_id.txt': No such file or directory
rm: cannot remove 'outputs/ep_stat_buffer_*.json': No such file or directory
run/data_collect_bc_NeilBranch0.sh: 59: [: 1: unexpected operator
run/data_collect_bc_NeilBranch0.sh: 8: run/data_collect_bc_NeilBranch0.sh: python: not found
$ PYTHON_RETURN=127!!! Start Over!!!$
```
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sudo python
sudo: python: command not found
```
4/21/2022 10:17:49 PM: Post Slack message:

     "data_collect_bc_NeilBranch0.sh" has the default parameter "dataset_root=/home/ubuntu/dataset/bc". I created a "carla-roach/dataset_root" folder and changed the parameter to "dataset_root=dataset_root". Running "$ sh data_collect_bc_NeilBranch0.sh" ended in an unspecified error (i.e. exit status not 0). I created the "/home/ubuntu/dataset/bc" folder and reset the parameter back to the default value. 
     How do I let the python file "data_collect_NeilBranch0.py" have super user access to write to "/home/ubuntu/dataset/bc"?
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh
Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 233, in main
    dataset_dir.mkdir(parents=True, exist_ok=True)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/pathlib.py", line 1273, in mkdir
    self._accessor.mkdir(self, mode)
PermissionError: [Errno 13] Permission denied: '/home/ubuntu/dataset/bc/expert'
```
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sudo sh run/data_collect_bc_NeilBranch0.sh 
[sudo] password for nsambhu: 
run/data_collect_bc_NeilBranch0.sh: 8: run/data_collect_bc_NeilBranch0.sh: python: not found
```
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sudo python
sudo: python: command not found
```
4/21/2022 10:25:25 PM:
```
(base) nsambhu@SAMBHU19:/home/ubuntu/dataset$ lsl
total 4.0K
drwxr-xr-x 2 root root 4.0K Apr 21 21:13 bc
```
```
(base) nsambhu@SAMBHU19:/home/ubuntu/dataset$ chmod 777 bc&&lsl
chmod: changing permissions of 'bc': Operation not permitted
```
```
(base) nsambhu@SAMBHU19:/home/ubuntu/dataset$ sudo chmod 777 bc&&lsl
[sudo] password for nsambhu: 
total 4.0K
drwxrwxrwx 2 root root 4.0K Apr 21 21:13 bc
```
4/21/2022 10:27:30 PM:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh 
run/data_collect_bc_NeilBranch0.sh: 47: run/data_collect_bc_NeilBranch0.sh: source: not found

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


rm: cannot remove 'outputs/checkpoint.txt': No such file or directory
rm: cannot remove 'outputs/wb_run_id.txt': No such file or directory
rm: cannot remove 'outputs/ep_stat_buffer_*.json': No such file or directory
run/data_collect_bc_NeilBranch0.sh: 59: [: 1: unexpected operator
Neil start here 1
/opt/carla-simulator/CarlaUE4.sh: line 2: 83859 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-21 22:25:58,924][utils.server_utils][INFO] - Kill Carla Servers!
CarlaUE4-Linux: no process found
[2022-04-21 22:25:59,938][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-21 22:25:59,939][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
[2022-04-21 22:26:05,277][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-21 22:26:06,162][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
[2022-04-21 22:26:07,506][__main__][INFO] - Start from env_idx: 0, task_idx 0
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/396bgoaw
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-21/22-25-57/wandb/run-20220421_222607-396bgoaw
wandb: Run `wandb offline` to turn off syncing.

/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
[2022-04-21 22:26:13,332][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 283, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 49, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 74, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles'])
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 35, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter))
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 377, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 89258
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-21/22-25-57/wandb/run-20220421_222607-396bgoaw/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-21/22-25-57/wandb/run-20220421_222607-396bgoaw/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/396bgoaw
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/21/2022 10:43:42 PM: use prints to find the line that causes the error
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ sh run/data_collect_bc_NeilBranch0.sh 
run/data_collect_bc_NeilBranch0.sh: 47: run/data_collect_bc_NeilBranch0.sh: source: not found

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


rm: cannot remove 'outputs/checkpoint.txt': No such file or directory
rm: cannot remove 'outputs/ep_stat_buffer_*.json': No such file or directory
run/data_collect_bc_NeilBranch0.sh: 59: [: 1: unexpected operator
Neil start here 1
Neil start here 2
/opt/carla-simulator/CarlaUE4.sh: line 2: 89010 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-21 22:45:13,011][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
CarlaUE4-Linux: no process found
[2022-04-21 22:45:14,025][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-21 22:45:14,025][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
[2022-04-21 22:45:19,317][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-21 22:45:20,300][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
[2022-04-21 22:45:21,758][__main__][INFO] - Start from env_idx: 0, task_idx 0
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/16nriyyx
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-21/22-45-11/wandb/run-20220421_224522-16nriyyx
wandb: Run `wandb offline` to turn off syncing.

/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
[2022-04-21 22:45:27,368][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 285, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 49, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 74, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles'])
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 35, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter))
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 379, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 91388
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-21/22-45-11/wandb/run-20220421_224522-16nriyyx/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-21/22-45-11/wandb/run-20220421_224522-16nriyyx/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/16nriyyx
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/21/2022 11:14:46 PM: error at data_collect_NeilBranch0.py:
```
            valid, list_debug_render, list_data_render, ep_stat_dict, ep_event_dict, timestamp = collect_single(
                run_name, env, data_writer, driver_dict, driver_log_dir,
                coach_dict, coach_log_dir, cfg.dagger_thresholds, cfg.log_video, noise_lon, noise_lat,
                cfg.alpha_coach, cfg.remove_final_steps)
```
