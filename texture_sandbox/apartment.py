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

from PIL import Image

# Connect to client
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(2.0)

# Get the world object
world = client.get_world()

# Filter world objects for those with 'Apartment' in the name
#print(list(filter(lambda k: 'Apartment' in k, world.get_names_of_all_objects())))

# Load the modified texture
#image = Image.open('BP_Apartment04_v05_modified.tga')
image = Image.open('Unreal_TGA_files/ambulance/T_Bodywork_Ambulance_d.TGA')
print(image)
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

# Now apply the texture to the building asset
world.apply_color_texture_to_object('BP_Apartment04_v05_Opt_2', carla.MaterialParameter.Diffuse, texture)

