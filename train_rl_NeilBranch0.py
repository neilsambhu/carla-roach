import gym
from pathlib import Path
import wandb
import hydra
from omegaconf import DictConfig, OmegaConf
import logging
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.callbacks import CallbackList

from agents.rl_birdview.utils.wandb_callback import WandbCallback
from carla_gym.utils import config_utils
from utils import server_utils

log = logging.getLogger(__name__)
bVerbose = True

@hydra.main(config_path='config', config_name='train_rl')
def main(cfg: DictConfig):
    if bVerbose:
        print("Neil start here 1")
        # print("cfg",cfg)
    if cfg.kill_running:
        server_utils.kill_carla()
    set_random_seed(cfg.seed, using_cuda=True)
    if bVerbose:
        print("Neil left here 1")

    if bVerbose:
        print("Neil start here 2")
    # start carla servers
    server_manager = server_utils.CarlaServerManager(cfg.carla_sh_path, configs=cfg.train_envs)
    if bVerbose:
        print('cfg.train_envs',cfg.train_envs)
    server_manager.start()
    if bVerbose:
        print("Neil left here 2")

    if bVerbose:
        print("Neil start here 3")
    # prepare agent
    agent_name = cfg.actors[cfg.ev_id].agent
    if bVerbose:
        print("Neil left here 3")

    if bVerbose:
        print("Neil start here 4")
    last_checkpoint_path = Path(hydra.utils.get_original_cwd()) / 'outputs' / 'checkpoint.txt'
    if last_checkpoint_path.exists():
        if bVerbose:
            print("Neil 4.100")
            print("last_checkpoint_path",last_checkpoint_path)
            print("Neil 4.101")
        with open(last_checkpoint_path, 'r') as f:
            if bVerbose:
                print("Neil 4.200")
                print("type(f)",type(f))
                print("type(f.read())",type(f.read()))
                print("str(f.read())",str(f.read()))
                print("Neil 4.201")
            cfg.agent[agent_name].wb_run_path = f.read()
            if bVerbose:
                print("Neil 4.202")
                print("type(cfg.agent[agent_name].wb_run_path)",type(cfg.agent[agent_name].wb_run_path))
                print("str(cfg.agent[agent_name].wb_run_path)",str(cfg.agent[agent_name].wb_run_path))
                print("cfg.agent[agent_name].wb_run_path",cfg.agent[agent_name].wb_run_path)
                print("Neil 4.203")

    if bVerbose:
        print("Neil left here 4")

    if bVerbose:
        print("Neil start here 5")
    OmegaConf.save(config=cfg.agent[agent_name], f='config_agent.yaml')
    if bVerbose:
        print("Neil left here 5")

    # single agent
    if bVerbose:
        print("Neil start here 6.0")
        print("cfg.agent[agent_name]",cfg.agent[agent_name])
        print("cfg.agent[agent_name].entry_point",cfg.agent[agent_name].entry_point)
    AgentClass = config_utils.load_entry_point(cfg.agent[agent_name].entry_point)
    if bVerbose:
        print("Neil 6.1")
        print("type(AgentClass)",type(AgentClass))
        print("AgentClass",AgentClass)
    if bVerbose:
        print("Neil 6.2")
    agent = AgentClass('config_agent.yaml')
    # sPathConfigAgent = "./outputs/2022-04-25/21-22-07/config_agent.yaml"
    # agent = AgentClass(sPathConfigAgent)
    if bVerbose:
        print("Neil 6.3")
    cfg_agent = OmegaConf.load('config_agent.yaml')
    if bVerbose:
        print("Neil left here 6.0")

    if bVerbose:
        print("Neil start here 7")
    obs_configs = {cfg.ev_id: OmegaConf.to_container(cfg_agent.obs_configs)}
    reward_configs = {cfg.ev_id: OmegaConf.to_container(cfg.actors[cfg.ev_id].reward)}
    terminal_configs = {cfg.ev_id: OmegaConf.to_container(cfg.actors[cfg.ev_id].terminal)}
    if bVerbose:
        print("Neil left here 7")

    if bVerbose:
        print("Neil start here 8")
    # env wrapper
    EnvWrapper = config_utils.load_entry_point(cfg_agent.env_wrapper.entry_point)
    wrapper_kargs = cfg_agent.env_wrapper.kwargs

    config_utils.check_h5_maps(cfg.train_envs, obs_configs, cfg.carla_sh_path)
    if bVerbose:
        print("Neil left here 8")

    def env_maker(config):
        log.info(f'making port {config["port"]}')
        env = gym.make(config['env_id'], obs_configs=obs_configs, reward_configs=reward_configs,
                       terminal_configs=terminal_configs, host='localhost', port=config['port'],
                       seed=cfg.seed, no_rendering=True, **config['env_configs'])
        env = EnvWrapper(env, **wrapper_kargs)
        return env

    if cfg.dummy or len(server_manager.env_configs) == 1:
        env = DummyVecEnv([lambda config=config: env_maker(config) for config in server_manager.env_configs])
    else:
        env = SubprocVecEnv([lambda config=config: env_maker(config) for config in server_manager.env_configs])

    # wandb init
    if bVerbose:
        print("Neil start here 100")
        print("type(env)",type(env))
        print("env",env)
    # wandb.init(allow_val_change=True)
    # wandb.config.update(cfg, allow_val_change=True) # Neil added 6/13/2022 1:15 PM
    wb_callback = WandbCallback(cfg, env)
    if bVerbose:
        print("Neil left here 100")
    if bVerbose:
        print("Neil start here 200")
    callback = CallbackList([wb_callback])
    if bVerbose:
        print("Neil left here 200")

    # save wandb run path to file such that bash file can find it
    with open(last_checkpoint_path, 'w') as f:
        f.write(wandb.run.path)

    if bVerbose:
        print("int(cfg.total_timesteps)",int(cfg.total_timesteps))
        print("callback",callback)
        print("cfg.seed",cfg.seed)
    
    agent.learn(env, total_timesteps=int(cfg.total_timesteps), callback=callback, seed=cfg.seed)

    server_manager.stop()


if __name__ == '__main__':
    if bVerbose:
        print("Neil start here 1")
    main()
    if bVerbose:
        print("Neil left here 1")
    log.info("train_rl.py DONE!")
