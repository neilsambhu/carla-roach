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
4/22/2022 10:42:05 AM: search for line in function collect_single that causes error

4/22/2022 10:54:57 AM: error at data_collect_NeilBranch0.py > collect_single:
    obs = env.reset()

4/22/2022 11:30:44 AM: ego_vehicle_handler.py > bp_filter needs to change from "vehicle.lincoln.mkz2017" to "vehicle.lincoln.mkz_2017"

4/22/2022 11:38:32 AM: change bp_filter hardcoded:
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 12720 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 11:38:29,629][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 11:38:30,644][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 11:38:30,644][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 11:38:35,947][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 11:38:36,787][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 11:38:38,247][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/3txghvu7
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/11-38-28/wandb/run-20220422_113838-3txghvu7
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
[2022-04-22 11:38:44,263][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._world World(id=11299570584422527121)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
change bp_filter hardcoded
bp_filter vehicle.lincoln.mkz_2017 , type: <class 'str'>
self._world.get_blueprint_library() [ActorBlueprint(id=static.prop.mesh,tags=[mesh, static, prop]), ActorBlueprint(id=static.prop.trashcan01,tags=[trashcan01, static, prop]), ActorBlueprint(id=static.prop.trashbag,tags=[trashbag, static, prop]), ActorBlueprint(id=static.prop.trafficwarning,tags=[static, trafficwarning, prop]), ActorBlueprint(id=static.prop.trafficcone02,tags=[trafficcone02, static, prop]), ActorBlueprint(id=static.prop.trafficcone01,tags=[trafficcone01, static, prop]), ActorBlueprint(id=static.prop.table,tags=[table, static, prop]), ActorBlueprint(id=static.prop.streetbarrier,tags=[streetbarrier, static, prop]), ActorBlueprint(id=static.prop.shoppingtrolley,tags=[shoppingtrolley, static, prop]), ActorBlueprint(id=static.prop.shoppingbag,tags=[static, shoppingbag, prop]), ActorBlueprint(id=static.prop.shoppingcart,tags=[static, shoppingcart, prop]), ActorBlueprint(id=static.prop.plasticchair,tags=[plasticchair, static, prop]), ActorBlueprint(id=static.prop.plantpot08,tags=[static, plantpot08, prop]), ActorBlueprint(id=static.prop.platformgarbage01,tags=[platformgarbage01, static, prop]), ActorBlueprint(id=static.prop.plasticbag,tags=[plasticbag, static, prop]), ActorBlueprint(id=static.prop.plantpot07,tags=[plantpot07, static, prop]), ActorBlueprint(id=static.prop.plantpot05,tags=[plantpot05, static, prop]), ActorBlueprint(id=static.prop.plantpot03,tags=[plantpot03, static, prop]), ActorBlueprint(id=static.prop.plantpot02,tags=[plantpot02, static, prop]), ActorBlueprint(id=static.prop.plantpot01,tags=[plantpot01, static, prop]), ActorBlueprint(id=static.prop.fountain,tags=[fountain, static, prop]), ActorBlueprint(id=static.prop.motorhelmet,tags=[static, motorhelmet, prop]), ActorBlueprint(id=static.prop.maptable,tags=[static, maptable, prop]), ActorBlueprint(id=static.prop.kiosk_01,tags=[kiosk_01, static, prop]), ActorBlueprint(id=static.prop.ironplank,tags=[ironplank, static, prop]), ActorBlueprint(id=static.prop.gnome,tags=[gnome, static, prop]), ActorBlueprint(id=static.prop.gardenlamp,tags=[gardenlamp, static, prop]), ActorBlueprint(id=static.prop.travelcase,tags=[travelcase, static, prop]), ActorBlueprint(id=static.prop.garbage06,tags=[garbage06, static, prop]), ActorBlueprint(id=static.prop.swing,tags=[static, swing, prop]), ActorBlueprint(id=static.prop.garbage04,tags=[garbage04, static, prop]), ActorBlueprint(id=static.prop.garbage01,tags=[garbage01, static, prop]), ActorBlueprint(id=static.prop.dirtdebris03,tags=[dirtdebris03, static, prop]), ActorBlueprint(id=static.prop.dirtdebris01,tags=[dirtdebris01, static, prop]), ActorBlueprint(id=static.prop.creasedbox02,tags=[creasedbox02, static, prop]), ActorBlueprint(id=static.prop.purse,tags=[purse, static, prop]), ActorBlueprint(id=static.prop.guitarcase,tags=[guitarcase, static, prop]), ActorBlueprint(id=static.prop.constructioncone,tags=[constructioncone, static, prop]), ActorBlueprint(id=static.prop.streetfountain,tags=[static, streetfountain, prop]), ActorBlueprint(id=static.prop.streetsign,tags=[streetsign, static, prop]), ActorBlueprint(id=static.prop.container,tags=[container, static, prop]), ActorBlueprint(id=static.prop.clothcontainer,tags=[clothcontainer, static, prop]), ActorBlueprint(id=static.prop.chainbarrierend,tags=[chainbarrierend, static, prop]), ActorBlueprint(id=static.prop.busstop,tags=[busstop, static, prop]), ActorBlueprint(id=static.prop.brokentile02,tags=[brokentile02, static, prop]), ActorBlueprint(id=static.prop.box03,tags=[box03, static, prop]), ActorBlueprint(id=static.prop.box02,tags=[box02, static, prop]), ActorBlueprint(id=static.prop.bike helmet,tags=[bike helmet, static, prop]), ActorBlueprint(id=static.prop.bench03,tags=[bench03, static, prop]), ActorBlueprint(id=static.prop.bench02,tags=[static, bench02, prop]), ActorBlueprint(id=controller.ai.walker,tags=[controller, walker, ai]), ActorBlueprint(id=static.prop.garbage02,tags=[garbage02, static, prop]), ActorBlueprint(id=static.prop.barrel,tags=[barrel, static, prop]), ActorBlueprint(id=walker.pedestrian.0049,tags=[0049, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0046,tags=[0046, walker, pedestrian]), ActorBlueprint(id=static.prop.advertisement,tags=[static, advertisement, prop]), ActorBlueprint(id=walker.pedestrian.0045,tags=[0045, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0044,tags=[0044, walker, pedestrian]), ActorBlueprint(id=static.prop.creasedbox03,tags=[creasedbox03, static, prop]), ActorBlueprint(id=walker.pedestrian.0043,tags=[walker, 0043, pedestrian]), ActorBlueprint(id=walker.pedestrian.0042,tags=[0042, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0041,tags=[0041, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0039,tags=[walker, 0039, pedestrian]), ActorBlueprint(id=static.prop.trashcan03,tags=[trashcan03, static, prop]), ActorBlueprint(id=static.prop.brokentile01,tags=[static, brokentile01, prop]), ActorBlueprint(id=walker.pedestrian.0038,tags=[0038, walker, pedestrian]), ActorBlueprint(id=static.prop.garbage05,tags=[garbage05, static, prop]), ActorBlueprint(id=walker.pedestrian.0037,tags=[walker, 0037, pedestrian]), ActorBlueprint(id=walker.pedestrian.0036,tags=[0036, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0035,tags=[0035, walker, pedestrian]), ActorBlueprint(id=static.prop.colacan,tags=[colacan, static, prop]), ActorBlueprint(id=walker.pedestrian.0034,tags=[walker, 0034, pedestrian]), ActorBlueprint(id=walker.pedestrian.0033,tags=[0033, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0028,tags=[0028, walker, pedestrian]), ActorBlueprint(id=static.prop.clothesline,tags=[clothesline, static, prop]), ActorBlueprint(id=walker.pedestrian.0024,tags=[0024, walker, pedestrian]), ActorBlueprint(id=static.prop.box01,tags=[box01, static, prop]), ActorBlueprint(id=walker.pedestrian.0022,tags=[walker, 0022, pedestrian]), ActorBlueprint(id=static.prop.vendingmachine,tags=[vendingmachine, static, prop]), ActorBlueprint(id=walker.pedestrian.0030,tags=[0030, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0021,tags=[0021, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0020,tags=[walker, 0020, pedestrian]), ActorBlueprint(id=walker.pedestrian.0019,tags=[0019, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0016,tags=[0016, walker, pedestrian]), ActorBlueprint(id=static.prop.doghouse,tags=[doghouse, static, prop]), ActorBlueprint(id=walker.pedestrian.0040,tags=[walker, 0040, pedestrian]), ActorBlueprint(id=walker.pedestrian.0014,tags=[0014, walker, pedestrian]), ActorBlueprint(id=static.prop.streetsign01,tags=[streetsign01, static, prop]), ActorBlueprint(id=walker.pedestrian.0011,tags=[0011, walker, pedestrian]), ActorBlueprint(id=static.prop.streetsign04,tags=[streetsign04, static, prop]), ActorBlueprint(id=static.prop.plastictable,tags=[plastictable, static, prop]), ActorBlueprint(id=walker.pedestrian.0031,tags=[0031, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0023,tags=[0023, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0009,tags=[0009, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0047,tags=[0047, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0007,tags=[0007, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0006,tags=[0006, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0048,tags=[0048, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0005,tags=[0005, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0004,tags=[0004, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0003,tags=[0003, walker, pedestrian]), ActorBlueprint(id=static.prop.creasedbox01,tags=[static, creasedbox01, prop]), ActorBlueprint(id=walker.pedestrian.0001,tags=[0001, walker, pedestrian]), ActorBlueprint(id=sensor.camera.instance_segmentation,tags=[instance_segmentation, sensor, camera]), ActorBlueprint(id=static.prop.plantpot04,tags=[plantpot04, static, prop]), ActorBlueprint(id=sensor.camera.semantic_segmentation,tags=[semantic_segmentation, sensor, camera]), ActorBlueprint(id=static.prop.bench01,tags=[static, bench01, prop]), ActorBlueprint(id=walker.pedestrian.0032,tags=[walker, 0032, pedestrian]), ActorBlueprint(id=walker.pedestrian.0010,tags=[0010, walker, pedestrian]), ActorBlueprint(id=sensor.camera.rgb,tags=[rgb, sensor, camera]), ActorBlueprint(id=static.prop.wateringcan,tags=[wateringcan, static, prop]), ActorBlueprint(id=sensor.other.rss,tags=[sensor, rss, other]), ActorBlueprint(id=static.prop.pergola,tags=[pergola, static, prop]), ActorBlueprint(id=sensor.lidar.ray_cast_semantic,tags=[ray_cast_semantic, sensor, lidar]), ActorBlueprint(id=sensor.camera.optical_flow,tags=[sensor, optical_flow, camera]), ActorBlueprint(id=static.prop.briefcase,tags=[briefcase, static, prop]), ActorBlueprint(id=walker.pedestrian.0018,tags=[0018, walker, pedestrian]), ActorBlueprint(id=sensor.other.radar,tags=[radar, sensor, other]), ActorBlueprint(id=sensor.other.obstacle,tags=[obstacle, sensor, other]), ActorBlueprint(id=static.prop.slide,tags=[slide, static, prop]), ActorBlueprint(id=static.prop.brokentile04,tags=[brokentile04, static, prop]), ActorBlueprint(id=sensor.other.lane_invasion,tags=[lane_invasion, sensor, other]), ActorBlueprint(id=static.prop.trashcan04,tags=[trashcan04, static, prop]), ActorBlueprint(id=static.prop.trashcan02,tags=[trashcan02, static, prop]), ActorBlueprint(id=sensor.other.imu,tags=[imu, sensor, other]), ActorBlueprint(id=static.prop.plantpot06,tags=[plantpot06, static, prop]), ActorBlueprint(id=static.prop.glasscontainer,tags=[glasscontainer, static, prop]), ActorBlueprint(id=static.prop.chainbarrier,tags=[chainbarrier, static, prop]), ActorBlueprint(id=sensor.camera.dvs,tags=[dvs, sensor, camera]), ActorBlueprint(id=static.prop.trampoline,tags=[trampoline, static, prop]), ActorBlueprint(id=sensor.camera.depth,tags=[depth, sensor, camera]), ActorBlueprint(id=static.prop.trashcan05,tags=[trashcan05, static, prop]), ActorBlueprint(id=sensor.other.collision,tags=[collision, sensor, other]), ActorBlueprint(id=vehicle.volkswagen.t2_2021,tags=[t2_2021, vehicle, volkswagen]), ActorBlueprint(id=walker.pedestrian.0008,tags=[walker, 0008, pedestrian]), ActorBlueprint(id=vehicle.ford.crown,tags=[crown, vehicle, ford]), ActorBlueprint(id=static.prop.calibrator,tags=[calibrator, static, prop]), ActorBlueprint(id=static.prop.mobile,tags=[mobile, static, prop]), ActorBlueprint(id=vehicle.mercedes.sprinter,tags=[sprinter, vehicle, mercedes]), ActorBlueprint(id=vehicle.nissan.patrol_2021,tags=[vehicle, patrol_2021, nissan]), ActorBlueprint(id=vehicle.mini.cooper_s_2021,tags=[cooper_s_2021, vehicle, mini]), ActorBlueprint(id=vehicle.vespa.zx125,tags=[zx125, vehicle, vespa]), ActorBlueprint(id=vehicle.carlamotors.firetruck,tags=[firetruck, vehicle, carlamotors]), ActorBlueprint(id=walker.pedestrian.0013,tags=[0013, walker, pedestrian]), ActorBlueprint(id=vehicle.ford.ambulance,tags=[ambulance, vehicle, ford]), ActorBlueprint(id=walker.pedestrian.0015,tags=[walker, 0015, pedestrian]), ActorBlueprint(id=vehicle.dodge.charger_police_2020,tags=[charger_police_2020, vehicle, dodge]), ActorBlueprint(id=walker.pedestrian.0029,tags=[0029, walker, pedestrian]), ActorBlueprint(id=vehicle.dodge.charger_2020,tags=[charger_2020, vehicle, dodge]), ActorBlueprint(id=vehicle.mercedes.coupe_2020,tags=[coupe_2020, vehicle, mercedes]), ActorBlueprint(id=vehicle.lincoln.mkz_2020,tags=[mkz_2020, vehicle, lincoln]), ActorBlueprint(id=static.prop.garbage03,tags=[garbage03, static, prop]), ActorBlueprint(id=static.prop.barbeque,tags=[barbeque, static, prop]), ActorBlueprint(id=static.prop.atm,tags=[atm, static, prop]), ActorBlueprint(id=walker.pedestrian.0026,tags=[0026, walker, pedestrian]), ActorBlueprint(id=vehicle.ford.mustang,tags=[mustang, vehicle, ford]), ActorBlueprint(id=vehicle.lincoln.mkz_2017,tags=[mkz_2017, vehicle, lincoln]), ActorBlueprint(id=vehicle.volkswagen.t2,tags=[t2, vehicle, volkswagen]), ActorBlueprint(id=vehicle.tesla.model3,tags=[model3, vehicle, tesla]), ActorBlueprint(id=static.trigger.friction,tags=[friction, static, trigger]), ActorBlueprint(id=sensor.lidar.ray_cast,tags=[ray_cast, sensor, lidar]), ActorBlueprint(id=vehicle.tesla.cybertruck,tags=[cybertruck, vehicle, tesla]), ActorBlueprint(id=vehicle.audi.etron,tags=[vehicle, etron, audi]), ActorBlueprint(id=static.prop.swingcouch,tags=[swingcouch, static, prop]), ActorBlueprint(id=walker.pedestrian.0002,tags=[0002, walker, pedestrian]), ActorBlueprint(id=vehicle.diamondback.century,tags=[century, vehicle, diamondback]), ActorBlueprint(id=sensor.other.gnss,tags=[gnss, sensor, other]), ActorBlueprint(id=vehicle.gazelle.omafiets,tags=[omafiets, vehicle, gazelle]), ActorBlueprint(id=vehicle.bh.crossbike,tags=[crossbike, vehicle, bh]), ActorBlueprint(id=static.prop.brokentile03,tags=[brokentile03, static, prop]), ActorBlueprint(id=vehicle.kawasaki.ninja,tags=[ninja, vehicle, kawasaki]), ActorBlueprint(id=vehicle.yamaha.yzf,tags=[yzf, vehicle, yamaha]), ActorBlueprint(id=vehicle.harley-davidson.low_rider,tags=[low_rider, vehicle, harley-davidson]), ActorBlueprint(id=vehicle.toyota.prius,tags=[prius, vehicle, toyota]), ActorBlueprint(id=vehicle.seat.leon,tags=[leon, vehicle, seat]), ActorBlueprint(id=vehicle.nissan.patrol,tags=[patrol, vehicle, nissan]), ActorBlueprint(id=vehicle.nissan.micra,tags=[vehicle, micra, nissan]), ActorBlueprint(id=vehicle.mini.cooper_s,tags=[cooper_s, vehicle, mini]), ActorBlueprint(id=static.prop.dirtdebris02,tags=[dirtdebris02, static, prop]), ActorBlueprint(id=vehicle.mercedes.coupe,tags=[coupe, vehicle, mercedes]), ActorBlueprint(id=walker.pedestrian.0027,tags=[0027, walker, pedestrian]), ActorBlueprint(id=vehicle.jeep.wrangler_rubicon,tags=[wrangler_rubicon, vehicle, jeep]), ActorBlueprint(id=static.prop.bin,tags=[bin, static, prop]), ActorBlueprint(id=vehicle.dodge.charger_police,tags=[charger_police, vehicle, dodge]), ActorBlueprint(id=vehicle.citroen.c3,tags=[vehicle, c3, citroen]), ActorBlueprint(id=vehicle.chevrolet.impala,tags=[impala, vehicle, chevrolet]), ActorBlueprint(id=walker.pedestrian.0025,tags=[0025, walker, pedestrian]), ActorBlueprint(id=vehicle.carlamotors.carlacola,tags=[carlacola, vehicle, carlamotors]), ActorBlueprint(id=static.prop.mailbox,tags=[mailbox, static, prop]), ActorBlueprint(id=vehicle.micro.microlino,tags=[microlino, vehicle, micro]), ActorBlueprint(id=walker.pedestrian.0017,tags=[0017, walker, pedestrian]), ActorBlueprint(id=walker.pedestrian.0012,tags=[0012, walker, pedestrian]), ActorBlueprint(id=vehicle.bmw.grandtourer,tags=[grandtourer, vehicle, bmw]), ActorBlueprint(id=vehicle.audi.tt,tags=[tt, vehicle, audi]), ActorBlueprint(id=vehicle.audi.a2,tags=[vehicle, a2, audi])]
self._world.get_blueprint_library().filter(bp_filter) [ActorBlueprint(id=vehicle.lincoln.mkz_2017,tags=[mkz_2017, vehicle, lincoln])]
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 356, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 86, in reset
    self._om_handler.reset(self._ev_handler.ego_vehicles)
  File "/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/obs_manager_handler.py", line 34, in reset
    om.attach_ego_vehicle(ev_actor)
  File "/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/birdview/chauffeurnet.py", line 73, in attach_ego_vehicle
    with h5py.File(maps_h5_path, 'r', libver='latest', swmr=True) as hf:
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/h5py/_hl/files.py", line 408, in __init__
    swmr=swmr)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/h5py/_hl/files.py", line 173, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 88, in h5py.h5f.open
OSError: Unable to open file (unable to open file: name = '/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/birdview/maps/Carla/Maps/Town01.h5', errno = 2, error message = 'No such file or directory', flags = 40, o_flags = 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 454, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 13538
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/11-38-28/wandb/run-20220422_113838-3txghvu7/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/11-38-28/wandb/run-20220422_113838-3txghvu7/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/3txghvu7
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 11:42:16 AM: TODO: fix source of "bp_filter"

4/22/2022 11:58:18 AM: TODO: find how "\_task['ego_vehicles']" is set in "CarlaMultiAgentEnv"; potential solution: find calls to "CarlaMultiAgentEnv" constructor
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ grep -r "CarlaMultiAgentEnv"
Binary file outputs/2022-04-22/11-46-58/wandb/run-20220422_114710-1cwmhon8/run-1cwmhon8.wandb matches
outputs/2022-04-22/11-46-58/wandb/run-20220422_114710-1cwmhon8/files/output.log:    from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
Binary file carla_gym/__pycache__/carla_multi_agent_env.cpython-37.pyc matches
carla_gym/carla_multi_agent_env.py:class CarlaMultiAgentEnv(gym.Env):
Binary file carla_gym/envs/suites/__pycache__/endless_env.cpython-37.pyc matches
Binary file carla_gym/envs/suites/__pycache__/nocrash_env.cpython-37.pyc matches
Binary file carla_gym/envs/suites/__pycache__/leaderboard_env.cpython-37.pyc matches
Binary file carla_gym/envs/suites/__pycache__/corl2017_env.cpython-37.pyc matches
carla_gym/envs/suites/leaderboard_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/leaderboard_env.py:class LeaderboardEnv(CarlaMultiAgentEnv):
carla_gym/envs/suites/corl2017_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/corl2017_env.py:class CoRL2017Env(CarlaMultiAgentEnv):
carla_gym/envs/suites/endless_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/endless_env.py:class EndlessEnv(CarlaMultiAgentEnv):
carla_gym/envs/suites/nocrash_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/nocrash_env.py:class NoCrashEnv(CarlaMultiAgentEnv):
```
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ grep -r --include=*.py "CarlaMultiAgentEnv"
carla_gym/carla_multi_agent_env.py:class CarlaMultiAgentEnv(gym.Env):
carla_gym/envs/suites/leaderboard_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/leaderboard_env.py:class LeaderboardEnv(CarlaMultiAgentEnv):
carla_gym/envs/suites/corl2017_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/corl2017_env.py:class CoRL2017Env(CarlaMultiAgentEnv):
carla_gym/envs/suites/endless_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/endless_env.py:class EndlessEnv(CarlaMultiAgentEnv):
carla_gym/envs/suites/nocrash_env.py:from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv
carla_gym/envs/suites/nocrash_env.py:class NoCrashEnv(CarlaMultiAgentEnv):
```
4/22/2022 12:11:58 PM: print('env_setup',env_setup):
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 15132 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 12:08:38,427][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 12:08:39,442][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 12:08:39,442][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 12:08:44,786][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 12:08:45,553][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 12:08:46,916][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/yrmsrlk1
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-08-37/wandb/run-20220422_120847-yrmsrlk1
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
env_setup {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
[2022-04-22 12:08:52,747][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=14400922288193170268)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 358, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 77, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 456, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 16797
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-08-37/wandb/run-20220422_120847-yrmsrlk1/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-08-37/wandb/run-20220422_120847-yrmsrlk1/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/yrmsrlk1
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 12:22:51 PM: "Neil start here 13" > "gym.make parameters":
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 18157 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 12:21:03,211][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 12:21:04,226][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 12:21:04,226][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 12:21:09,665][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 12:21:10,463][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 12:21:11,777][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/1xinpzi0
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-21-02/wandb/run-20220422_122112-1xinpzi0
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
gym.make parameters:
	env_setup['env_id'] Endless-v0 obs_configs=obs_configs {'hero': {'birdview': {'module': 'birdview.chauffeurnet', 'width_in_pixels': 192, 'pixels_ev_to_bottom': 40, 'pixels_per_meter': 5.0, 'history_idx': [-16, -11, -6, -1], 'scale_bbox': True, 'scale_mask_col': 1.0}, 'speed': {'module': 'actor_state.speed'}, 'control': {'module': 'actor_state.control'}, 'velocity': {'module': 'actor_state.velocity'}, 'gnss': {'module': 'navigation.gnss'}, 'central_rgb': {'module': 'camera.rgb', 'fov': 100, 'width': 900, 'height': 256, 'location': [-1.5, 0.0, 2.0], 'rotation': [0.0, 0.0, 0.0]}, 'route_plan': {'module': 'navigation.waypoint_plan', 'steps': 20}}} reward_configs=reward_configs {'hero': {'entry_point': 'reward.valeo_action:ValeoAction'}} terminal_configs=terminal_configs {'hero': {'entry_point': 'terminal.leaderboard_dagger:LeaderboardDagger', 'kwargs': {'max_time': 300, 'no_collision': True, 'no_run_rl': False, 'no_run_stop': False}}} host=cfg.host localhost port=cfg.port 2000 seed=cfg.seed 2021 no_rendering=cfg.no_rendering False **env_setup['env_configs'] {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
[2022-04-22 12:21:17,583][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=1472883097159059815)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 371, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 77, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 469, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 18942
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-21-02/wandb/run-20220422_122112-1xinpzi0/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-21-02/wandb/run-20220422_122112-1xinpzi0/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/1xinpzi0
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 12:30:07 PM: "Neil start here 13" > "env_setup" and "gym.make parameters":
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 18693 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 12:28:53,859][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 12:28:54,873][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 12:28:54,874][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 12:29:00,271][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 12:29:01,132][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 12:29:02,553][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/3kng465f
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-28-52/wandb/run-20220422_122902-3kng465f
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
env_setup {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
gym.make parameters:
	env_setup['env_id'] Endless-v0 obs_configs=obs_configs {'hero': {'birdview': {'module': 'birdview.chauffeurnet', 'width_in_pixels': 192, 'pixels_ev_to_bottom': 40, 'pixels_per_meter': 5.0, 'history_idx': [-16, -11, -6, -1], 'scale_bbox': True, 'scale_mask_col': 1.0}, 'speed': {'module': 'actor_state.speed'}, 'control': {'module': 'actor_state.control'}, 'velocity': {'module': 'actor_state.velocity'}, 'gnss': {'module': 'navigation.gnss'}, 'central_rgb': {'module': 'camera.rgb', 'fov': 100, 'width': 900, 'height': 256, 'location': [-1.5, 0.0, 2.0], 'rotation': [0.0, 0.0, 0.0]}, 'route_plan': {'module': 'navigation.waypoint_plan', 'steps': 20}}} reward_configs=reward_configs {'hero': {'entry_point': 'reward.valeo_action:ValeoAction'}} terminal_configs=terminal_configs {'hero': {'entry_point': 'terminal.leaderboard_dagger:LeaderboardDagger', 'kwargs': {'max_time': 300, 'no_collision': True, 'no_run_rl': False, 'no_run_stop': False}}} host=cfg.host localhost port=cfg.port 2000 seed=cfg.seed 2021 no_rendering=cfg.no_rendering False **env_setup['env_configs'] {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
[2022-04-22 12:29:08,200][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=11684082283257058607)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 371, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 77, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 469, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 19818
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-28-52/wandb/run-20220422_122902-3kng465f/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-28-52/wandb/run-20220422_122902-3kng465f/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/3kng465f
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 12:43:38 PM: between "Neil left here 14" and "Neil start here 15" > env.set_task_idx
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 20914 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 12:41:20,534][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 12:41:21,548][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 12:41:21,548][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 12:41:26,863][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 12:41:27,777][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 12:41:29,019][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/33okyo49
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-41-19/wandb/run-20220422_124129-33okyo49
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
calling set_task_idx
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
[2022-04-22 12:41:35,331][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=5266563482667726008)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 373, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 82, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 471, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 21760
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-41-19/wandb/run-20220422_124129-33okyo49/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/12-41-19/wandb/run-20220422_124129-33okyo49/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/33okyo49
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 12:52:18 PM: grep for \_all_tasks:
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ grep -r --include=*.py "_all_tasks"
carla_gym/carla_multi_agent_env.py:        self._all_tasks = all_tasks
carla_gym/carla_multi_agent_env.py:        self._task = self._all_tasks[self._task_idx].copy()
carla_gym/carla_multi_agent_env.py:            print('self._all_tasks',self._all_tasks)
carla_gym/carla_multi_agent_env.py:        self._task = self._all_tasks[self._task_idx].copy()
carla_gym/carla_multi_agent_env.py:            print('self._all_tasks',self._all_tasks)
carla_gym/carla_multi_agent_env.py:        return len(self._all_tasks)
carla_gym/carla_multi_agent_env.py:            self._task = self._all_tasks[self._task_idx].copy()
carla_gym/envs/suites/leaderboard_env.py:        all_tasks = self.build_all_tasks(carla_map, weather_group, routes_group)
carla_gym/envs/suites/leaderboard_env.py:    def build_all_tasks(carla_map, weather_group, routes_group):
carla_gym/envs/suites/corl2017_env.py:        all_tasks = self.build_all_tasks(carla_map, weather_group, route_description, task_type)
carla_gym/envs/suites/corl2017_env.py:    def build_all_tasks(carla_map, weather_group, route_description, task_type):
carla_gym/envs/suites/endless_env.py:        all_tasks = self.build_all_tasks(num_zombie_vehicles, num_zombie_walkers, weather_group)
carla_gym/envs/suites/endless_env.py:    def build_all_tasks(num_zombie_vehicles, num_zombie_walkers, weather_group):
carla_gym/envs/suites/nocrash_env.py:        all_tasks = self.build_all_tasks(carla_map, weather_group, route_description, background_traffic)
carla_gym/envs/suites/nocrash_env.py:    def build_all_tasks(carla_map, weather_group, route_description, background_traffic):
agents/rl_birdview/utils/wandb_callback.py:        #     env_all_tasks = self.vec_env.get_attr('all_tasks',indices=i)[0]
agents/rl_birdview/utils/wandb_callback.py:        #     num_zombies[f'train/n_veh/{i}'] = env_all_tasks[0]['num_zombie_vehicles']
agents/rl_birdview/utils/wandb_callback.py:        #     num_zombies[f'train/n_ped/{i}'] = env_all_tasks[0]['num_zombie_walkers']
agents/rl_birdview/utils/wandb_callback.py:        #             for env_task in env_all_tasks:
agents/rl_birdview/utils/wandb_callback.py:        #             self.vec_env.set_attr('all_tasks', env_all_tasks, indices=i)
```
4/22/2022 1:15:30 PM: found "'model': 'vehicle.lincoln.mkz2017'" with missing underscore
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 23275 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 13:13:02,677][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 13:13:03,693][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 13:13:03,693][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 13:13:09,052][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 13:13:09,874][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 13:13:11,226][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/oja6qsnm
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-13-01/wandb/run-20220422_131311-oja6qsnm
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
CarlaMultiAgentEnv > __init__
all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
calling set_task_idx
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
[2022-04-22 13:13:17,022][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=2168647527154206492)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 373, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 85, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 471, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 24265
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-13-01/wandb/run-20220422_131311-oja6qsnm/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-13-01/wandb/run-20220422_131311-oja6qsnm/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/oja6qsnm
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 1:23:54 PM: found line in data_collect_NeilBranch0.py that calls CarlaMultiAgentEnv.__init__: 13.2
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 24017 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 13:22:12,884][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 13:22:13,899][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 13:22:13,899][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 13:22:19,306][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 13:22:20,217][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 13:22:21,540][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/s1vjhxch
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-22-11/wandb/run-20220422_132221-s1vjhxch
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
13.1:start: may be call to CarlaMultiAgentEnv__init__
13.1:end: may be call to CarlaMultiAgentEnv__init__
13.2:start: may be call to CarlaMultiAgentEnv__init__
CarlaMultiAgentEnv > __init__
all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
13.2:end: may be call to CarlaMultiAgentEnv__init__
13.3:start: may be call to CarlaMultiAgentEnv__init__
13.3:end: may be call to CarlaMultiAgentEnv__init__
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
calling set_task_idx
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
[2022-04-22 13:22:27,125][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=10735668673024523280)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 385, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 85, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 483, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 25337
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-22-11/wandb/run-20220422_132221-s1vjhxch/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-22-11/wandb/run-20220422_132221-s1vjhxch/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/s1vjhxch
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 1:30:26 PM: "data_collect_NeilBranch0.py":13.2: data types of "gym" and "env":
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
CarlaUE4-Linux: no process found
[2022-04-22 13:32:34,322][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 13:32:35,337][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 13:32:35,337][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 13:32:40,673][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 13:32:41,448][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 13:32:42,818][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/24jvwweb
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-32-33/wandb/run-20220422_133243-24jvwweb
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
13.1:start: may be call to CarlaMultiAgentEnv__init__
13.1:end: may be call to CarlaMultiAgentEnv__init__
13.2:start: may be call to CarlaMultiAgentEnv__init__
type(gym) <class 'module'>
CarlaMultiAgentEnv > __init__
all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
type(env) <class 'carla_gym.envs.suites.endless_env.EndlessEnv'>
13.2:end: may be call to CarlaMultiAgentEnv__init__
13.3:start: may be call to CarlaMultiAgentEnv__init__
13.3:end: may be call to CarlaMultiAgentEnv__init__
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
calling set_task_idx
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
[2022-04-22 13:32:48,422][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=1925341583290222597)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 389, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 85, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 487, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 26427
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-32-33/wandb/run-20220422_133243-24jvwweb/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/13-32-33/wandb/run-20220422_133243-24jvwweb/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/24jvwweb
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 1:37:28 PM: "endless_env.py" > find "CarlaMultiAgentEnv" and "\_all_tasks"
```
from carla_gym.carla_multi_agent_env import CarlaMultiAgentEnv


class EndlessEnv(CarlaMultiAgentEnv):
    def __init__(self, carla_map, host, port, seed, no_rendering, obs_configs, reward_configs, terminal_configs,
                 num_zombie_vehicles, num_zombie_walkers, weather_group):
        all_tasks = self.build_all_tasks(num_zombie_vehicles, num_zombie_walkers, weather_group)
        super().__init__(carla_map, host, port, seed, no_rendering,
                         obs_configs, reward_configs, terminal_configs, all_tasks)
```
4/22/2022 1:40:23 PM: (probably) the call to EndlessEnv will have the parameter "'model': 'vehicle.lincoln.mkz2017'"
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ grep -r --include=*.py "EndlessEnv"
carla_gym/__init__.py:        'entry_point': 'carla_gym.envs:EndlessEnv',
carla_gym/envs/__init__.py:from carla_gym.envs.suites.endless_env import EndlessEnv
carla_gym/envs/__init__.py:    'EndlessEnv',
carla_gym/envs/suites/endless_env.py:class EndlessEnv(CarlaMultiAgentEnv):
```
4/22/2022 1:46:39 PM: no meaningful results from finding "EndlessEnv"

4/22/2022 1:47:26 PM: look inside "data_collect_NeilBranch0.py":13.2:"gym.make"

4/22/2022 2:00:35 PM: see if I found the write function definition of "make"
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
[2022-04-22 14:00:18,424][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
/opt/carla-simulator/CarlaUE4.sh: line 2: 26178 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 14:00:19,437][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 14:00:19,437][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 14:00:24,810][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 14:00:25,591][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 14:00:26,937][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/2ynuxfeh
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-00-17/wandb/run-20220422_140027-2ynuxfeh
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
13.1:start: may be call to CarlaMultiAgentEnv__init__
13.1:end: may be call to CarlaMultiAgentEnv__init__
env_setup {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
gym.make parameters:
	env_setup['env_id'] Endless-v0 obs_configs=obs_configs {'hero': {'birdview': {'module': 'birdview.chauffeurnet', 'width_in_pixels': 192, 'pixels_ev_to_bottom': 40, 'pixels_per_meter': 5.0, 'history_idx': [-16, -11, -6, -1], 'scale_bbox': True, 'scale_mask_col': 1.0}, 'speed': {'module': 'actor_state.speed'}, 'control': {'module': 'actor_state.control'}, 'velocity': {'module': 'actor_state.velocity'}, 'gnss': {'module': 'navigation.gnss'}, 'central_rgb': {'module': 'camera.rgb', 'fov': 100, 'width': 900, 'height': 256, 'location': [-1.5, 0.0, 2.0], 'rotation': [0.0, 0.0, 0.0]}, 'route_plan': {'module': 'navigation.waypoint_plan', 'steps': 20}}} reward_configs=reward_configs {'hero': {'entry_point': 'reward.valeo_action:ValeoAction'}} terminal_configs=terminal_configs {'hero': {'entry_point': 'terminal.leaderboard_dagger:LeaderboardDagger', 'kwargs': {'max_time': 300, 'no_collision': True, 'no_run_rl': False, 'no_run_stop': False}}} host=cfg.host localhost port=cfg.port 2000 seed=cfg.seed 2021 no_rendering=cfg.no_rendering False **env_setup['env_configs'] {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}
13.2:start: may be call to CarlaMultiAgentEnv__init__
type(gym) <class 'module'>
calling registration.py > make(id, **kwargs)
CarlaMultiAgentEnv > __init__
all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
type(env) <class 'carla_gym.envs.suites.endless_env.EndlessEnv'>
13.2:end: may be call to CarlaMultiAgentEnv__init__
13.3:start: may be call to CarlaMultiAgentEnv__init__
13.3:end: may be call to CarlaMultiAgentEnv__init__
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
calling set_task_idx
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
[2022-04-22 14:00:32,751][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz2017'}}, 'endless': {'hero': True}}
self._world World(id=5781624559481619419)
bp_filter vehicle.lincoln.mkz2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) []
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 389, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 85, in reset
    ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
  File "/home/nsambhu/github/carla-roach/carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py", line 45, in reset
    blueprint = np.random.choice(self._world.get_blueprint_library().filter(bp_filter)) # 4/22/2022 11:12:05 AM: error line
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 487, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 28300
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-00-17/wandb/run-20220422_140027-2ynuxfeh/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-00-17/wandb/run-20220422_140027-2ynuxfeh/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/2ynuxfeh
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 2:08:21 PM: (potential solution) endless_env.py > change "'model': 'vehicle.lincoln.mkz2017'"

4/22/2022 2:10:34 PM: find all instances of "lincoln"
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ grep -r --include=*.py "lincoln"
carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py:                print('bp_filter',bp_filter,", type:",type(bp_filter)) # 4/22/2022 11:30:44 AM: bp_filter needs to change from "vehicle.lincoln.mkz2017" to "vehicle.lincoln.mkz_2017"
carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py:                # bp_filter = "vehicle.lincoln.mkz_2017"
carla_gym/envs/suites/endless_env.py:                'hero': {'model': 'vehicle.lincoln.mkz2017'}
```
4/22/2022 2:12:00 PM: implement 4/22/2022 2:08:21 PM:"potential solution"

4/22/2022 2:13:48 PM: find all instances of "bVerbose = True"
```
(carla) nsambhu@SAMBHU19:~/github/carla-roach$ grep -r --include=*.py "bVerbose *= *True"
carla_gym/core/task_actor/ego_vehicle/ego_vehicle_handler.py:            bVerbose = True
carla_gym/carla_multi_agent_env.py:bVerbose = True
carla_gym/envs/suites/endless_env.py:bVerbose = True
data_collect_NeilBranch0.py:bVerbose = True
```
4/22/2022 2:17:03 PM: with "'model': 'vehicle.lincoln.mkz2017'" fixed at the source, I'm back to the error message at 4/22/2022 11:38:32 AM (i.e. hardcoded fix for model parameter)
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 28051 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 14:15:58,925][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 14:15:59,939][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 14:15:59,939][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 14:16:05,259][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 14:16:06,171][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 14:16:07,644][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/371p5ay9
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-15-57/wandb/run-20220422_141607-371p5ay9
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
13.1:start: may be call to CarlaMultiAgentEnv__init__
13.1:end: may be call to CarlaMultiAgentEnv__init__
env_setup {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
gym.make parameters:
	env_setup['env_id'] Endless-v0 obs_configs=obs_configs {'hero': {'birdview': {'module': 'birdview.chauffeurnet', 'width_in_pixels': 192, 'pixels_ev_to_bottom': 40, 'pixels_per_meter': 5.0, 'history_idx': [-16, -11, -6, -1], 'scale_bbox': True, 'scale_mask_col': 1.0}, 'speed': {'module': 'actor_state.speed'}, 'control': {'module': 'actor_state.control'}, 'velocity': {'module': 'actor_state.velocity'}, 'gnss': {'module': 'navigation.gnss'}, 'central_rgb': {'module': 'camera.rgb', 'fov': 100, 'width': 900, 'height': 256, 'location': [-1.5, 0.0, 2.0], 'rotation': [0.0, 0.0, 0.0]}, 'route_plan': {'module': 'navigation.waypoint_plan', 'steps': 20}}} reward_configs=reward_configs {'hero': {'entry_point': 'reward.valeo_action:ValeoAction'}} terminal_configs=terminal_configs {'hero': {'entry_point': 'terminal.leaderboard_dagger:LeaderboardDagger', 'kwargs': {'max_time': 300, 'no_collision': True, 'no_run_rl': False, 'no_run_stop': False}}} host=cfg.host localhost port=cfg.port 2000 seed=cfg.seed 2021 no_rendering=cfg.no_rendering False **env_setup['env_configs'] {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}
13.2:start: may be call to CarlaMultiAgentEnv__init__
type(gym) <class 'module'>
calling registration.py > make(id, **kwargs)
CarlaMultiAgentEnv > __init__
all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
type(env) <class 'carla_gym.envs.suites.endless_env.EndlessEnv'>
13.2:end: may be call to CarlaMultiAgentEnv__init__
13.3:start: may be call to CarlaMultiAgentEnv__init__
13.3:end: may be call to CarlaMultiAgentEnv__init__
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
calling set_task_idx
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
self._all_tasks [{'weather': 'ClearNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'WetNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'HardRainNoon', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}, {'weather': 'ClearSunset', 'description_folder': 'None', 'route_id': 0, 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'ego_vehicles': {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}, 'scenario_actors': {}}]
[2022-04-22 14:16:12,917][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
self._task['ego_vehicles'] {'routes': {'hero': []}, 'actors': {'hero': {'model': 'vehicle.lincoln.mkz_2017'}}, 'endless': {'hero': True}}
self._world World(id=7190748693545958152)
bp_filter vehicle.lincoln.mkz_2017 , type: <class 'str'>
self._world.get_blueprint_library().filter(bp_filter) [ActorBlueprint(id=vehicle.lincoln.mkz_2017,tags=[mkz_2017, vehicle, lincoln])]
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 389, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 97, in reset
    self._om_handler.reset(self._ev_handler.ego_vehicles)
  File "/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/obs_manager_handler.py", line 34, in reset
    om.attach_ego_vehicle(ev_actor)
  File "/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/birdview/chauffeurnet.py", line 73, in attach_ego_vehicle
    with h5py.File(maps_h5_path, 'r', libver='latest', swmr=True) as hf:
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/h5py/_hl/files.py", line 408, in __init__
    swmr=swmr)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/h5py/_hl/files.py", line 173, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 88, in h5py.h5f.open
OSError: Unable to open file (unable to open file: name = '/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/birdview/maps/Carla/Maps/Town01.h5', errno = 2, error message = 'No such file or directory', flags = 40, o_flags = 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 487, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 29553
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-15-57/wandb/run-20220422_141607-371p5ay9/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-15-57/wandb/run-20220422_141607-371p5ay9/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/371p5ay9
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 2:27:41 PM: "data_collect_bc_NeilBranch0.sh": removed some verbosity
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
/opt/carla-simulator/CarlaUE4.sh: line 2: 29303 Killed                  "/opt/carla-simulator/CarlaUE4/Binaries/Linux/CarlaUE4-Linux-Shipping" CarlaUE4 $@
[2022-04-22 14:26:27,144][utils.server_utils][INFO] - Kill Carla Servers!
Neil left here 2
Neil start here 3
CarlaUE4-Linux: no process found
[2022-04-22 14:26:28,159][utils.server_utils][INFO] - Kill Carla Servers!
[2022-04-22 14:26:28,159][utils.server_utils][INFO] - CUDA_VISIBLE_DEVICES=0 bash /opt/carla-simulator/CarlaUE4.sh -fps=10 -quality-level=Epic -carla-rpc-port=2000
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
Neil left here 3
Neil start here 4
[2022-04-22 14:26:33,477][agents.rl_birdview.rl_birdview_agent][INFO] - Resume checkpoint latest ckpt/ckpt_11833344.pth
[2022-04-22 14:26:34,273][agents.rl_birdview.rl_birdview_agent][INFO] - Loading wandb checkpoint: ckpt/ckpt_11833344.pth
Neil left here 4
Neil start here 5
Neil left here 5
Neil start here 6
Neil left here 6
Neil start here 7
Neil left here 7
Neil start here 8
Neil left here 8
Neil start here 9
[2022-04-22 14:26:35,591][__main__][INFO] - Start from env_idx: 0, task_idx 0
Neil left here 9
Neil start here 10
Neil left here 10
Neil start here 11
wandb: Currently logged in as: neilsambhu (use `wandb login --relogin` to force relogin)
wandb: wandb version 0.12.15 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.10.12
wandb: Syncing run bc/expert
wandb: ⭐ View project at https://wandb.ai/neilsambhu/il_leaderboard_roach
wandb: 🚀 View run at https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/s0u0ps1i
wandb: Run data is saved locally in /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-26-26/wandb/run-20220422_142635-s0u0ps1i
wandb: Run `wandb offline` to turn off syncing.

Neil left here 11
Neil start here 12
Neil left here 12
Neil start here 13
calling registration.py > make(id, **kwargs)
/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
Neil left here 13
Neil start here 14
Neil left here 14
env.num_tasks 4
[2022-04-22 14:26:41,432][__main__][INFO] - Start episode 0000, noise_lon=False, noise_lat=False, {'env_id': 'Endless-v0', 'env_configs': {'carla_map': 'Town01', 'num_zombie_vehicles': [80, 160], 'num_zombie_walkers': [80, 160], 'weather_group': 'train'}}
Neil start here 15
Neil start here 16
Neil left here 16
Neil start here 17
Neil left here 17
Neil start here 18
Neil left here 18
Neil start here 19
Neil left here 19
Neil start here 20
Traceback (most recent call last):
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 198, in run_and_report
    return func()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 350, in <lambda>
    overrides=args.overrides,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/hydra.py", line 112, in run
    configure_logging=with_log_configuration,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/core/utils.py", line 125, in run_job
    ret.return_value = task_function(task_cfg)
  File "data_collect_NeilBranch0.py", line 389, in main
    cfg.alpha_coach, cfg.remove_final_steps)
  File "data_collect_NeilBranch0.py", line 68, in collect_single
    obs = env.reset()
  File "/home/nsambhu/github/carla-roach/carla_gym/carla_multi_agent_env.py", line 97, in reset
    self._om_handler.reset(self._ev_handler.ego_vehicles)
  File "/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/obs_manager_handler.py", line 34, in reset
    om.attach_ego_vehicle(ev_actor)
  File "/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/birdview/chauffeurnet.py", line 73, in attach_ego_vehicle
    with h5py.File(maps_h5_path, 'r', libver='latest', swmr=True) as hf:
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/h5py/_hl/files.py", line 408, in __init__
    swmr=swmr)
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/h5py/_hl/files.py", line 173, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 88, in h5py.h5f.open
OSError: Unable to open file (unable to open file: name = '/home/nsambhu/github/carla-roach/carla_gym/core/obs_manager/birdview/maps/Carla/Maps/Town01.h5', errno = 2, error message = 'No such file or directory', flags = 40, o_flags = 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "data_collect_NeilBranch0.py", line 487, in <module>
    main()
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/main.py", line 37, in decorated_main
    strict=strict,
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 347, in _run_hydra
    lambda: hydra.run(
  File "/home/nsambhu/anaconda3/envs/carla/lib/python3.7/site-packages/hydra/_internal/utils.py", line 237, in run_and_report
    assert mdl is not None
AssertionError

wandb: Waiting for W&B process to finish, PID 30725
wandb: Program failed with code 1.  Press ctrl-c to abort syncing.
wandb:                                                                                
wandb: Find user logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-26-26/wandb/run-20220422_142635-s0u0ps1i/logs/debug.log
wandb: Find internal logs for this run at: /home/nsambhu/github/carla-roach/outputs/2022-04-22/14-26-26/wandb/run-20220422_142635-s0u0ps1i/logs/debug-internal.log
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: 
wandb: Synced bc/expert: https://wandb.ai/neilsambhu/il_leaderboard_roach/runs/s0u0ps1i
$ PYTHON_RETURN=1!!! Start Over!!!$
```
4/22/2022 2:31:56 PM: TODO: find "Town01.h5" in \*.py
```
grep -r --include=*.py "Town01.h5"
```