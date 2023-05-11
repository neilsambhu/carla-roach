import logging
import gym
import numpy as np
import carla

from .core.zombie_walker.zombie_walker_handler import ZombieWalkerHandler
from .core.zombie_vehicle.zombie_vehicle_handler import ZombieVehicleHandler
from .core.obs_manager.obs_manager_handler import ObsManagerHandler
from .core.task_actor.ego_vehicle.ego_vehicle_handler import EgoVehicleHandler
from .core.task_actor.scenario_actor.scenario_actor_handler import ScenarioActorHandler
from .utils.traffic_light import TrafficLightHandler
from .utils.dynamic_weather import WeatherHandler
from stable_baselines3.common.utils import set_random_seed

logger = logging.getLogger(__name__)

from inspect import currentframe, getframeinfo
bVerbose = True

class CarlaMultiAgentEnv(gym.Env):
    def __init__(self, carla_map, host, port, seed, no_rendering,
                 obs_configs, reward_configs, terminal_configs, all_tasks):
        if bVerbose:
            print("CarlaMultiAgentEnv > __init__")
            # print('all_tasks',all_tasks)
        self._all_tasks = all_tasks
        self._obs_configs = obs_configs
        self._carla_map = carla_map
        self._seed = seed

        self.name = self.__class__.__name__

        self._init_client(carla_map, host, port, seed=seed, no_rendering=no_rendering)

        # define observation spaces exposed to agent
        self._om_handler = ObsManagerHandler(obs_configs)
        self._ev_handler = EgoVehicleHandler(self._client, reward_configs, terminal_configs)
        self._zw_handler = ZombieWalkerHandler(self._client)
        self._zv_handler = ZombieVehicleHandler(self._client, tm_port=self._tm.get_port())
        self._sa_handler = ScenarioActorHandler(self._client)
        self._wt_handler = WeatherHandler(self._world)

        # observation spaces
        self.observation_space = self._om_handler.observation_space
        # define action spaces exposed to agent
        # throttle, steer, brake
        self.action_space = gym.spaces.Dict({ego_vehicle_id: gym.spaces.Box(
            low=np.array([0.0, -1.0, 0.0]),
            high=np.array([1.0, 1.0, 1.0]),
            dtype=np.float32)
            for ego_vehicle_id in obs_configs.keys()})

        self._task_idx = 0
        self._shuffle_task = True
        self._task = self._all_tasks[self._task_idx].copy()

    def set_task_idx(self, task_idx):
        if bVerbose:
            print("calling set_task_idx")
            # print('self._all_tasks',self._all_tasks)
        self._task_idx = task_idx
        self._shuffle_task = False
        self._task = self._all_tasks[self._task_idx].copy()
        if bVerbose:
            # print('self._all_tasks',self._all_tasks)
            pass

    @property
    def num_tasks(self):
        return len(self._all_tasks)

    @property
    def task(self):
        return self._task

    def reset(self):
        if bVerbose:
            frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
            print('inside CarlaMultiAgentEnv.reset() function')
            frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
        if self._shuffle_task:
            self._task_idx = np.random.choice(self.num_tasks)
            self._task = self._all_tasks[self._task_idx].copy()
        self.clean()

        self._wt_handler.reset(self._task['weather'])
        logger.debug("_wt_handler reset done!!")

        if bVerbose:
            # print("self._task['ego_vehicles']",self._task['ego_vehicles'])
            # print("self._task['ego_vehicles']['actors']",self._task['ego_vehicles']['actors']);quit();
            # print(f'self._world.get_names_of_all_objects(): {self._world.get_names_of_all_objects()}')
            pass
        ev_spawn_locations = self._ev_handler.reset(self._task['ego_vehicles']) # 4/22/2022 11:09:04 AM: error line
        logger.debug("_ev_handler reset done!!")
        if bVerbose:
            # print(f'self._world.get_names_of_all_objects(): {self._world.get_names_of_all_objects()}');quit()
            pass
        

        self._sa_handler.reset(self._task['scenario_actors'], self._ev_handler.ego_vehicles)
        logger.debug("_sa_handler reset done!!")

        self._zw_handler.reset(self._task['num_zombie_walkers'], ev_spawn_locations)
        logger.debug("_zw_handler reset done!!")

        self._zv_handler.reset(self._task['num_zombie_vehicles'], ev_spawn_locations)
        logger.debug("_zv_handler reset done!!")

        self._om_handler.reset(self._ev_handler.ego_vehicles)
        logger.debug("_om_handler reset done!!")
        
        # 12/5/2022 4:59:47 PM: Neil added adversarial textures: start
        # self.adversarial_textures(bVerbose)
        # 12/5/2022 4:59:47 PM: Neil added adversarial textures: end

        self._world.tick()

        snap_shot = self._world.get_snapshot()
        self._timestamp = {
            'step': 0,
            'frame': snap_shot.timestamp.frame,
            'relative_wall_time': 0.0,
            'wall_time': snap_shot.timestamp.platform_timestamp,
            'relative_simulation_time': 0.0,
            'simulation_time': snap_shot.timestamp.elapsed_seconds,
            'start_frame': snap_shot.timestamp.frame,
            'start_wall_time': snap_shot.timestamp.platform_timestamp,
            'start_simulation_time': snap_shot.timestamp.elapsed_seconds
        }

        _, _, _ = self._ev_handler.tick(self.timestamp)
        # get obeservations
        obs_dict = self._om_handler.get_observation(self.timestamp)
        return obs_dict

    def step(self, control_dict):
        self._ev_handler.apply_control(control_dict)
        self._sa_handler.tick()
        # tick world
        self._world.tick()

        # update timestamp
        snap_shot = self._world.get_snapshot()
        self._timestamp['step'] = snap_shot.timestamp.frame-self._timestamp['start_frame']
        self._timestamp['frame'] = snap_shot.timestamp.frame
        self._timestamp['wall_time'] = snap_shot.timestamp.platform_timestamp
        self._timestamp['relative_wall_time'] = self._timestamp['wall_time'] - self._timestamp['start_wall_time']
        self._timestamp['simulation_time'] = snap_shot.timestamp.elapsed_seconds
        self._timestamp['relative_simulation_time'] = self._timestamp['simulation_time'] \
            - self._timestamp['start_simulation_time']

        reward_dict, done_dict, info_dict = self._ev_handler.tick(self.timestamp)

        # get observations
        obs_dict = self._om_handler.get_observation(self.timestamp)

        # update weather
        self._wt_handler.tick(snap_shot.timestamp.delta_seconds)

        # num_walkers = len(self._world.get_actors().filter("*walker.pedestrian*"))
        # num_vehicles = len(self._world.get_actors().filter("vehicle*"))
        # logger.debug(f"num_walkers: {num_walkers}, num_vehicles: {num_vehicles}, ")

        return obs_dict, reward_dict, done_dict, info_dict
    # 12/5/2022 5:28:05 PM: helper functions for adversarial textures: start
    def adversarial_textures_on_object(self, target_object):
        print('Altering texture for object: ' + target_object)
        # Modify its texture 
        # import cv2
        # image = cv2.imread('../../../textures/colorful_cat.jpeg')
        # image = cv2.imread('../../../textures/M_Tesla_Bodywork_orm2.TGA')
        # print(f'image.shape: {image.shape}')
        # height,width,_ = image.shape
        from PIL import Image
        image = Image.open('../../../textures/M_Tesla_Bodywork_orm4.TGA')
        height = image.size[1]
        width = image.size[0]
        print(f'image.size: {image.size}')
        texture = carla.TextureColor(width,height)
        # for x in range(0,len(image[0])):
        #     for y in range(0,len(image)):
        for x in range(0,width):
            for y in range(0,height):
                # color = image[y][x]
                color = image.getpixel((x,y))
                r = int(color[0])
                g = int(color[1])
                b = int(color[2])
                # a = int(color[3])
                a = int(0)
                a = 255
                # texture.set(x, height - y - 1, carla.Color(r,g,b,a))
                texture.set(x, y, carla.Color(r,g,b,a)) # 12/14/2022 9:52:20 PM: I think this will be upside down
        self._world.apply_color_texture_to_object(target_object, carla.MaterialParameter.Diffuse, texture)
    def filter_carla_object_names(self,object_names):
        list_output_object_names = []
        import re
        reVehicle = re.compile('Vehicle_Car_.*')
        reVh = re.compile('Vh_.*')
        reBP_C = re.compile('BP_.*_C_.*')
        reBP_Tesla = re.compile('BP_TeslaM3_C_.*')
        for object_name in object_names:
            # if (reVehicle.match(object_name) or reVh.match(object_name) or reBP_C.match(object_name)):
            if reBP_Tesla.match(object_name):
                list_output_object_names.append(object_name)
        return list_output_object_names
    def adversarial_textures(self, bVerbose):
        # Get names of all available objects
        object_names = self._world.get_names_of_all_objects()
        object_names = self.filter_carla_object_names(object_names)
        if bVerbose:
            import os;print(f'os.getcwd(): {os.getcwd()}')
            print(f'len(object_names): {len(object_names)}')
            print(f'type(object_names): {type(object_names)}')
            print(f'object_names: {object_names}');#import time;time.sleep(1);quit()
        # for name in object_names:
        #     print(name)
        # Choose an object to modify # For example target_object could be 'SM_Cartel_Add_5' 
        import random
        # target_object = random.choice(object_names)
        random.shuffle(object_names)
        
        # serial for loop
        from tqdm import tqdm
        lObjectNamesToModify = len(object_names)
        for i in tqdm(range(lObjectNamesToModify)):
            self.adversarial_textures_on_object(object_names[i])
    # 12/5/2022 5:28:05 PM: helper functions for adversarial textures: end
    def _init_client(self, carla_map, host, port, seed=2021, no_rendering=False):
        client = None
        while client is None:
            try:
                if bVerbose:
                    print(f'host: {host}\tport: {port}')
                client = carla.Client(host, port)
                client.set_timeout(60.0)
            except RuntimeError as re:
                if "timeout" not in str(re) and "time-out" not in str(re):
                    print("Could not connect to Carla server because:", re)
                client = None

        self._client = client
        self._world = client.load_world(carla_map)
        self._tm = client.get_trafficmanager(port+6000)

        self.set_sync_mode(True)
        self.set_no_rendering_mode(self._world, no_rendering)

        # self._tm.set_hybrid_physics_mode(True)

        # self._tm.set_global_distance_to_leading_vehicle(5.0)
        # logger.debug("trafficmanager set_global_distance_to_leading_vehicle")

        set_random_seed(self._seed, using_cuda=True)
        self._tm.set_random_device_seed(self._seed)

        self._world.tick()

        # register traffic lights
        TrafficLightHandler.reset(self._world)

    def set_sync_mode(self, sync):
        settings = self._world.get_settings()
        settings.synchronous_mode = sync
        settings.fixed_delta_seconds = 0.1
        settings.deterministic_ragdolls = True
        self._world.apply_settings(settings)
        self._tm.set_synchronous_mode(sync)

    @staticmethod
    def set_no_rendering_mode(world, no_rendering):
        settings = world.get_settings()
        settings.no_rendering_mode = no_rendering
        world.apply_settings(settings)

    @property
    def timestamp(self):
        return self._timestamp.copy()

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()
        logger.debug("env __exit__!")

    def close(self):
        self.clean()
        self.set_sync_mode(False)
        self._client = None
        self._world = None
        self._tm = None

    def clean(self):
        self._sa_handler.clean()
        self._zw_handler.clean()
        self._zv_handler.clean()
        self._om_handler.clean()
        self._ev_handler.clean()
        self._wt_handler.clean()
        self._world.tick()
