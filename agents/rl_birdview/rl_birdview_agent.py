import logging
import numpy as np
from omegaconf import OmegaConf
import wandb
import copy

from carla_gym.utils.config_utils import load_entry_point

bVerbose = True
class RlBirdviewAgent():
    def __init__(self, path_to_conf_file='config_agent.yaml'):
        if bVerbose:
            print('Neil 6.2.1')
            print('rl_birdview_agent.py > __init__')
        self._logger = logging.getLogger(__name__)
        if bVerbose:
            print('Neil 6.2.2')
        self._render_dict = None
        if bVerbose:
            print('Neil 6.2.3')
        self.supervision_dict = None
        if bVerbose:
            print('Neil 6.2.4')
            print('path_to_conf_file',path_to_conf_file)
            from os.path import exists
            print('exists(path_to_conf_file)',exists(path_to_conf_file))
            import os
            print('os.getcwd()',os.getcwd())
        if bVerbose:
            print('Neil 6.2.5')
        self.setup(path_to_conf_file)
        if bVerbose:
            print('Neil 6.2.6')

    def setup(self, path_to_conf_file):
        if bVerbose:
            print('Neil 6.2.5.100')
            print('path_to_conf_file',path_to_conf_file)
            print('Neil 6.2.5.101')
        cfg = OmegaConf.load(path_to_conf_file)
        if bVerbose:
            print('Neil 6.2.5.2')

        # load checkpoint from wandb
        if cfg.wb_run_path is not None:
            if bVerbose:
                print('Neil 6.2.5.3')
            api = wandb.Api()
            if bVerbose:
                print('Neil 6.2.5.4')
                print('type(cfg)',type(cfg))
                print('cfg',cfg)
                print('cfg.wb_run_path',cfg.wb_run_path)
            # original line
            # run = api.run(cfg.wb_run_path) # 4/29/2022 1 PM: Neil removed. 5/2/2022 3:37:10 PM: added. 5/2/2022 3:47:33 PM: removed.
            # new line
            # run = wandb.init(config=cfg) # 4/29/2022 1 PM: Neil added. 5/2/2022 3:37:23 PM: removed. 5/2/2022 3:47:39 PM: added.
            # run = wandb.init()
            # wandb.init(config=cfg)
            # 5/10/2022 12:20:06 PM 
            # run = wandb.init(config=path_to_conf_file)
            # 5/10/2022 12:27:41 PM 
            # import os
            # full_path_to_conf_file = os.path.join(os.getcwd(),path_to_conf_file)
            # if bVerbose:
            #     print("type(full_path_to_conf_file)",type(full_path_to_conf_file))
            #     print("full_path_to_conf_file",full_path_to_conf_file)
            #     print("os.path.exists(full_path_to_conf_file)",os.path.exists(full_path_to_conf_file))
            # run = wandb.init(config=full_path_to_conf_file)
            # 5/10/2022 3:40:09 PM 
            # run = wandb.init(config="config_driver.yaml")
            # 5/10/2022 3:52:54 PM 
            # run = wandb.init()
            # wandb.config.update(cfg)
            # 5/10/2022 3:58:48 PM 
            # run = wandb.init()
            # wandb.config.update("config_driver.yaml")
            # 5/10/2022 4:37:00 PM: troubleshooting
            # run = wandb.init(config={"epochs": 4, "batch_size": 32})
            # 5/10/2022 4:48:06 PM: start
            # cfg2 = None
            # import yaml
            # with open(path_to_conf_file, "r") as stream:
            #     cfg2 = yaml.safe_load(stream)
            # print("type(cfg2)",type(cfg2))
            # print("cfg2",cfg2)
            # run = wandb.init(config=cfg2)
            # 5/10/2022 4:48:06 PM: end
            # 5/10/2022 5:48:29 PM: start
            cfg2 = None
            import yaml
            with open(path_to_conf_file, "r") as stream:
                cfg2 = yaml.safe_load(stream)
            if bVerbose:
                print("type(cfg2)",type(cfg2))
                print("cfg2",cfg2)
            # add "<entity>/<project>/<run_id>" to init
            entity = "neilsambhu"
            # project = "carla-roach"
            project = "train_rl_experts"
            import random, string
            letters = string.ascii_lowercase
            # run_id = ''.join(random.choice(letters) for i in range(10))
            # run_id = "roach"
            # run_id = "fg8y4a2n"
            # run_id = "Neil009RL"
            run_id = ""
            with open('outputs/checkpoint.txt') as f:
                checkpoint = f.read()
                run_id = checkpoint.split("/")[2]
            if bVerbose:
                print("entity",entity,"\nproject",project,"\nrun_id",run_id)
            # run = wandb.init(config=cfg2, entity=entity, project=project, id=run_id)
            run = wandb.init(config=cfg2, entity=entity, project=project, resume=run_id)
            # 5/10/2022 5:48:29 PM: end
            if bVerbose:
                print('Neil 6.2.5.500')
                print('type(run)',type(run))
                print('run',run)
                print('type(wandb.config)',type(wandb.config))
                print('wandb.config',wandb.config)
                assert wandb.run is not None
                print('Neil 6.2.5.501')
                # print('type(run.files())',type(run.files()))
                print('Neil 6.2.5.502')
                # print('run.files()',run.files())
                print('Neil 6.2.5.503')
                # import os
                # print('os.getcwd()',os.getcwd())
                print('Neil 6.2.5.504')
                # print("type(f.name)",type(f.name))
                # print("f.name",f.name)
                print('Neil 6.2.5.505')
                print("wandb.apis.public.Files",wandb.apis.public.Files)
                # print("wandb.apis.public.Files.Files()",wandb.apis.public.Files.Files())
                print('Neil 6.2.5.506')
            # 5/10/2022 5:21:24 PM: start
            if bVerbose:
                print('Neil 6.2.5.600')
            api = wandb.Api()
            if bVerbose:
                print('Neil 6.2.5.601')
            # template
            # run = api.run("<entity>/<project>/<run_id>")
            # sParametersApiRun = f"<{entity}>/<{project}>/<{run_id}>"
            # remove angle brackets from sParametersApiRun
            sParametersApiRun = f"{entity}/{project}/{run_id}"
            if bVerbose:
                print("sParametersApiRun",sParametersApiRun)
            run = api.run(sParametersApiRun)
            if bVerbose:
                print('Neil 6.2.5.602')
            # for file in run.files():
            #     # file.download()
            #     print("file.download()",file.download())
            if bVerbose:
                print('Neil 6.2.5.603')
            # 5/10/2022 5:21:24 PM: end
            if bVerbose:
                print('Neil 6.2.5.604')
                print('type(run.files())',type(run.files()))
                print('Neil 6.2.5.605')
                print('run.files()',run.files())
                print('Neil 6.2.5.606')
            
            all_ckpts = [f for f in run.files() if 'ckpt' in f.name]
            if bVerbose:
                print('Neil 6.2.5.607')
                print("type(all_ckpts)",type(all_ckpts))
                print("all_ckpts",all_ckpts)
                print('Neil 6.2.5.608')

            if bVerbose:
                print('Neil 6.2.5.700')
            if cfg.wb_ckpt_step is None:
                if bVerbose:
                    print('Neil 6.2.5.701')
                # 6/19/2022 3:39 PM: start
                # if len(all_ckpts) == 0:
                #     all_ckpts = [0]
                # 6/19/2022 3:39 PM: end
                f = max(all_ckpts, key=lambda x: int(x.name.split('_')[1].split('.')[0]))
                # if len(all_ckpts) > 0:
                #     f = max(all_ckpts, key=lambda x: int(x.name.split('_')[1].split('.')[0]))
                if bVerbose:
                    print('Neil 6.2.5.702')
                self._logger.info(f'Resume checkpoint latest {f.name}')
                # if len(all_ckpts) > 0:
                #     self._logger.info(f'Resume checkpoint latest {f.name}')
                if bVerbose:
                    print('Neil 6.2.5.703')
            else:
                wb_ckpt_step = int(cfg.wb_ckpt_step)
                f = min(all_ckpts, key=lambda x: abs(int(x.name.split('_')[1].split('.')[0]) - wb_ckpt_step))
                self._logger.info(f'Resume checkpoint closest to step {wb_ckpt_step}: {f.name}')
            

            f.download(replace=True)
            run.file('config_agent.yaml').download(replace=True)
            cfg = OmegaConf.load('config_agent.yaml')
            self._ckpt = f.name
        else:
            self._ckpt = None
        if bVerbose:
            print('Neil 6.2.5.1000')
        cfg = OmegaConf.to_container(cfg)

        self._obs_configs = cfg['obs_configs']
        self._train_cfg = cfg['training']

        # prepare policy
        self._policy_class = load_entry_point(cfg['policy']['entry_point'])
        self._policy_kwargs = cfg['policy']['kwargs']
        if self._ckpt is None:
            self._policy = None
        else:
            self._logger.info(f'Loading wandb checkpoint: {self._ckpt}')
            self._policy, self._train_cfg['kwargs'] = self._policy_class.load(self._ckpt)
            self._policy = self._policy.eval()

        self._wrapper_class = load_entry_point(cfg['env_wrapper']['entry_point'])
        self._wrapper_kwargs = cfg['env_wrapper']['kwargs']

    def run_step(self, input_data, timestamp):
        input_data = copy.deepcopy(input_data)

        policy_input = self._wrapper_class.process_obs(input_data, self._wrapper_kwargs['input_states'], train=False)

        actions, values, log_probs, mu, sigma, features = self._policy.forward(
            policy_input, deterministic=True, clip_action=True)
        control = self._wrapper_class.process_act(actions, self._wrapper_kwargs['acc_as_action'], train=False)
        self.supervision_dict = {
            'action': np.array([control.throttle, control.steer, control.brake], dtype=np.float32),
            'value': values[0],
            'action_mu': mu[0],
            'action_sigma': sigma[0],
            'features': features[0],
            'speed': input_data['speed']['forward_speed']
        }
        self.supervision_dict = copy.deepcopy(self.supervision_dict)

        self._render_dict = {
            'timestamp': timestamp,
            'obs': policy_input,
            'im_render': input_data['birdview']['rendered'],
            'action': actions,
            'action_value': values[0],
            'action_log_probs': log_probs[0],
            'action_mu': mu[0],
            'action_sigma': sigma[0]
        }
        self._render_dict = copy.deepcopy(self._render_dict)

        return control

    def reset(self, log_file_path):
        # logger
        self._logger.handlers = []
        self._logger.propagate = False
        self._logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(log_file_path, mode='w')
        fh.setLevel(logging.DEBUG)
        self._logger.addHandler(fh)
    
    def learn(self, env, total_timesteps, callback, seed):
        from inspect import currentframe, getframeinfo
        bVerbose = True
        if bVerbose:
            frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
        if self._policy is None:
            self._policy = self._policy_class(env.observation_space, env.action_space, **self._policy_kwargs)

        # init ppo model
        model_class = load_entry_point(self._train_cfg['entry_point'])
        model = model_class(self._policy, env, **self._train_cfg['kwargs'])
        model.learn(total_timesteps, callback=callback, seed=seed)

    def render(self, reward_debug, terminal_debug):
        '''
        test render, used in benchmark.py
        '''
        self._render_dict['reward_debug'] = reward_debug
        self._render_dict['terminal_debug'] = terminal_debug

        return self._wrapper_class.im_render(self._render_dict)

    @property
    def obs_configs(self):
        return self._obs_configs
