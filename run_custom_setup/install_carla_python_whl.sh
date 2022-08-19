cd run_custom_setup
# mkdir install_carla_python_whl
cd install_carla_python_whl

# curl -O https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.13.tar.gz
# ls *.tar.gz

# mkdir CARLA_0.9.13
# tar -xvzf CARLA_0.9.13.tar.gz -C CARLA_0.9.13

ls CARLA_0.9.13/PythonAPI/carla/dist/
pip3 install CARLA_0.9.13/PythonAPI/carla/dist/carla-0.9.13-cp37-cp37m-manylinux_2_27_x86_64.whl
