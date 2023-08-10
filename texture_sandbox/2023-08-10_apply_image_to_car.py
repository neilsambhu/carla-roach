import carla
import os

def apply_image_to_car(car_actor, world, image_path):
    # Get the materials of the car's blueprint
    car_bp = car_actor.type_id.split('.')[0]  # Get the car's blueprint ID
    blueprint = world.get_blueprint_library().find(car_bp)
    
    # Find the first material slot
    material_slot = 0
    
    # Create an image texture asset
    image_texture = carla.AssetTexture(image_path)
    image_texture.set_filter(carla.TextureFilter.Linear, carla.TextureFilter.Linear, carla.TextureFilter.Linear)
    
    # Set the texture to the material
    blueprint.set_material_texture(material_slot, image_texture)
    blueprint.set_material_color(material_slot, carla.Color(1.0, 1.0, 1.0))  # Resetting material color

def main():
    try:
        # Connect to the CARLA simulator
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        # Get the world
        world = client.get_world()

        # Define the spawn point for the car
        spawn_point = carla.Transform(carla.Location(x=100, y=100, z=2), carla.Rotation())

        # Spawn a car (You can change the blueprint name to any other car)
        car_bp_name = "vehicle.tesla.model3"
        car_actor = world.spawn_actor(world.get_blueprint_library().find(car_bp_name), spawn_point)

        if car_actor is not None:
            print("Car spawned successfully!")

            # Define the path to the image you want to apply
            image_path = os.path.join(os.getcwd(), 'colorful_cat.jpeg')
            
            # Apply the image to the car's material
            apply_image_to_car(car_actor, world, image_path)
        else:
            print("Failed to spawn car!")

    finally:
        # Destroy actors and clean up
        if 'car_actor' in locals():
            car_actor.destroy()

if __name__ == '__main__':
    main()

