curl -O https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-20.10.9-3.el7.x86_64.rpm
curl -O https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-cli-20.10.9-3.el7.x86_64.rpm
curl -O https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.6.7-3.1.el7.x86_64.rpm
curl -O https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-compose-plugin-2.6.0-3.el7.x86_64.rpm
# Install Docker Engine
# sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo yum localinstall *.rpm
rm *.rpm
## Start Docker.
sudo systemctl start docker
## Verify that Docker Engine is installed correctly by running the hello-world image.
sudo docker run hello-world
