import subprocess
import os
import time
from omegaconf import OmegaConf
# os.environ.get('CUDA_VISIBLE_DEVICES')

import logging
log = logging.getLogger(__name__)
from inspect import currentframe, getframeinfo
bVerbose = True

def kill_carla():
    kill_process = subprocess.Popen('killall -9 -r CarlaUE4-Linux', shell=True)
    kill_process.wait()
    time.sleep(1)
    log.info("Kill Carla Servers!")
def kill_carla_docker():
    kill_process = subprocess.Popen('dockerlist=$(sudo docker container ls -q); sudo docker kill $dockerlist', shell=True, stdin=subprocess.PIPE, encoding="utf8")
    kill_process.communicate('q\n')
    # kill_process.wait()
    # time.sleep(1)
    log.info("Kill Carla Servers!")


class CarlaServerManager():
    def __init__(self, carla_sh_str, port=2000, configs=None, t_sleep=5):
        self._carla_sh_str = carla_sh_str
        # self._root_save_dir = root_save_dir
        self._t_sleep = t_sleep
        self.env_configs = []

        if configs is None:
            cfg = {
                'gpu': 0,
                'port': port,
            }
            self.env_configs.append(cfg)
        else:
            for cfg in configs:
                for gpu in cfg['gpu']:
                    single_env_cfg = OmegaConf.to_container(cfg)
                    single_env_cfg['gpu'] = gpu
                    single_env_cfg['port'] = port
                    self.env_configs.append(single_env_cfg)
                    port += 5

    def start(self):
        # kill_carla()
        kill_carla_docker()
        for cfg in self.env_configs:
            cmd = f'CUDA_VISIBLE_DEVICES={cfg["gpu"]} bash {self._carla_sh_str} ' \
                f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]}'
            #     f'-fps=10 -carla-server -opengl -carla-rpc-port={cfg["port"]}'
            # 06/28/2022: Neil added: start
            # cmd = f'DISPLAY=:8 vglrun -d :7.{cfg["gpu"]} $CARLA_PATH/CarlaUE4/Binaries/Linux/CarlaUE4'
            # cmd = f'DISPLAY=:8 vglrun -d :7.{cfg["gpu"]} bash {self._carla_sh_str} ' \
            #     f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]}'
            # cmd = f'DISPLAY=:8 vglrun -d :7.{cfg["gpu"]} {self._carla_sh_str}'
            # cmd = f'DISPLAY=:1 vglrun -d :7.{cfg["gpu"]} {self._carla_sh_str}'
            # cmd = f'DISPLAY=:2 vglrun -d :7.{cfg["gpu"]} {self._carla_sh_str}'
            # 06/28/2022: Neil added: end
            # 7/10/2022: Neil added: start
            # cmd = f'CUDA_VISIBLE_DEVICES={cfg["gpu"]} bash {self._carla_sh_str} ' \
            #     f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # 7/10/2022: Neil added: end
            # 8/8/2022: Neil added: start
            # cmd = f'graphicsadapter={cfg["gpu"]} bash {self._carla_sh_str} ' \
            #     f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # cmd = f'SDL_HINT_CUDA_DEVICE={cfg["gpu"]} bash {self._carla_sh_str} ' \
            #     f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # cmd = f'CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES={cfg["gpu"]} bash {self._carla_sh_str} ' \
            #     f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # working system CARLA install
            cmd = f'DEVICE= CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES={cfg["gpu"]} bash {self._carla_sh_str} ' \
                f'-fps=10 -quality-level=Epic -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # 8/8/2022: Neil added: end
            # 8/9/2022: Neil added: start
            # cmd = f'sudo docker run --privileged --gpus "device={cfg["gpu"]}" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # working docker
            cmd = f'echo q | sudo -S docker run --privileged --gpus "device={cfg["gpu"]}" --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port={cfg["port"]} -RenderOffScreen'
            # 8/9/2022: Neil added: end
            # 8/11/2022: Neil added: start 
            # cmd = f'apptainer build --sandbox carla-0.9.13/ docker://carlasim/carla:0.9.13 && bash carla-0.9.13/home/carla/CarlaUE4.sh'
            # 8/11/2022: Neil added: end 
            log.info(cmd)
            # log_file = self._root_save_dir / f'server_{cfg["port"]}.log'
            # server_process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid, stdout=open(log_file, "w"))
            if bVerbose:
                frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
            server_process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid) # 8/9/2022 4:51:00 PM: comment out 
            # 8/9/2022: Dan added (for docker): start
            server_process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid, stdin=subprocess.PIPE, encoding="utf8")
            sudo_out = server_process.communicate('q\n', timeout=1)
            # 8/9/2022: Dan added (for docker): end
            # 8/26/2022: Neil added: start
            time.sleep(10)
            # 8/26/2022: Neil added: end
            if bVerbose:
                frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
        time.sleep(self._t_sleep)

    def stop(self):
        kill_carla()
        time.sleep(self._t_sleep)
        log.info(f"Kill Carla Servers!")
