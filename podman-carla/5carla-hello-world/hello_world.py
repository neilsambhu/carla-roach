import carla
import subprocess
import os
import time

def kill_carla_podman():
    kill_process = subprocess.Popen('podman kill --signal KILL -a', shell=True)
    kill_process.wait()
    time.sleep(1)
    kill_process = subprocess.Popen('podman container cleanup --all --rm', shell=True)
    kill_process.wait()
    time.sleep(1)
def open_carla_simulator():
    kill_carla_podman()
    cmd = f'podman run -it --privileged -e NVIDIA_VISIBLE_DEVICES=0 --net=host -v /tmp/.X11-unix:/tmp/.X11-unix:rw carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh -carla-rpc-port=2000 -RenderOffScreen'
    cmd = f'xhost local:root && podman run --privileged --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh'
    server_process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid) 
    time.sleep(10)
def fundamentals():
    import math, random
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    bp_lib = world.get_blueprint_library()
    spawn_points = world.get_map().get_spawn_points()
    vehicle_bp = bp_lib.find('vehicle.lincoln.mkz_2020')
    vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))
    spectator = world.get_spectator()
    transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4,z=2.5)), vehicle.get_transform().rotation)
    spectator.set_transform(transform) 
    for i in range(30): 
        vehicle_bp = random.choice(bp_lib.filter('vehicle')) 
        npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points)) 
    for v in world.get_actors().filter('*vehicle*'): 
        v.set_autopilot(True) 
    camera_bp = bp_lib.find('sensor.camera.rgb') 
    camera_init_trans = carla.Transform(carla.Location(z=2))
    camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=vehicle)
    camera.listen(lambda image: image.save_to_disk('out/%06d.png' % image.frame))
    time.sleep(10)
    camera.stop()

def main():
    open_carla_simulator()
    fundamentals()
    time.sleep(5)
    
if __name__ == "__main__":
    main()