# https://docs.docker.com/engine/install/rhel/

# Set up the repository
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/rhel/docker-ce.repo

# Install Docker Engine
sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin

## Start Docker.
sudo systemctl start docker

## Verify that Docker Engine is installed correctly by running the hello-world image.
sudo docker run hello-world
