import carla
import subprocess, time, os, random

def kill_carla_podman():
    kill_process = subprocess.Popen('podman kill --signal KILL -a', shell=True)
    kill_process.wait()
    time.sleep(1)
    kill_process = subprocess.Popen('podman container cleanup --all --rm', shell=True)
    kill_process.wait()
    time.sleep(1)
kill_carla_podman()

# 4/1/2023 7:57:17 PM: launch simulator: start
cmd = f'xhost local:root && podman run --privileged --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 /bin/bash ./CarlaUE4.sh'
server_process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
time.sleep(10)
# 4/1/2023 7:57:17 PM: launch simulator: end
# Connect to the CARLA simulator
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# Get the world object
world = client.get_world()
# Load layered map for Town 01 with minimum layout plus buildings and parked vehicles
# world = client.load_world('Town01_Opt', carla.MapLayer.Buildings | carla.MapLayer.ParkedVehicles)
# world = client.load_world('Town04_Opt', carla.MapLayer.Buildings | carla.MapLayer.ParkedVehicles)
# world = client.load_world('Town10HD_Opt', carla.MapLayer.Buildings | carla.MapLayer.ParkedVehicles)
# Toggle all buildings off
# world.unload_map_layer(carla.MapLayer.Buildings)
# world.unload_map_layer(carla.MapLayer.All)
# world.unload_map_layer(carla.MapLayer.Buildings)
# world.unload_map_layer(carla.MapLayer.Decals)
# world.unload_map_layer(carla.MapLayer.Foliage)
# world.unload_map_layer(carla.MapLayer.Ground)
# world.unload_map_layer(carla.MapLayer.ParkedVehicles)
# world.unload_map_layer(carla.MapLayer.Particles)
# world.unload_map_layer(carla.MapLayer.Props)
# world.unload_map_layer(carla.MapLayer.StreetLights)
# world.unload_map_layer(carla.MapLayer.Walls)

# manual control
# manual_control = subprocess.Popen('python manual_control.py')
# manual_control.wait()
spawn_points = world.get_map().get_spawn_points()

# Define the blueprint of the vehicle you want to spawn
blueprint_library = world.get_blueprint_library()
# vehicle_bp = blueprint_library.find('vehicle.tesla.model3')
vehicle_bp = blueprint_library.find('vehicle.ford.ambulance')

# Spawn the vehicle
for i, spawn_point in enumerate(spawn_points[0:1]):
    vehicle = world.spawn_actor(vehicle_bp, spawn_point)

    # Wait for a few seconds to let the vehicle spawn properly
    world.wait_for_tick()

    # Do something with the vehicle
    print(f'Spawned vehicle {vehicle.id}')
all_objects = list(world.get_names_of_all_objects())
# print(all_objects)
ambulances = [k for k in all_objects if 'BP_Ambulance' in k]
# parked_vehicles = [k for k in all_objects if 'Vh_Car_' in k]
print(ambulances)

# Load image texture
from PIL import Image
# Load the modified texture
image = Image.open('Unreal_TGA_files/ambulance/T_Details02_Ambulance_d_custom.TGA')
height = image.size[1]
width = image.size[0]

# Instantiate a carla.TextureColor object and populate
# the pixels with data from the modified image
texture = carla.TextureColor(width ,height)
for x in range(0,width):
    for y in range(0,height):
        color = image.getpixel((x,y))
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        a = 255
        texture.set(x, y, carla.Color(r,g,b,a))

from tqdm import tqdm
# Apply texture to ambulances
for ambulance in tqdm(ambulances):
    world.apply_color_texture_to_object(ambulance, carla.MaterialParameter.Diffuse, texture)
# Apply texture to all objects
# for my_object in tqdm(parked_vehicles):
#     world.apply_color_texture_to_object(my_object, carla.MaterialParameter.Diffuse, texture)

# # Retrieve the first vehicle in the world
# vehicle_list = world.get_actors().filter('vehicle.*')
# for vehicle in vehicle_list:
#     # Set the texture color
#     new_color = carla.Color(255,0,0)
#     # vehicle.set_color(new_color)
#     vehicle.set_attribute('color', new_color.rgba)

print('done')
