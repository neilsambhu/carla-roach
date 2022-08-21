# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker

# Installing on CentOS 7/8
## Setting up Docker on CentOS 7/8
# sudo yum-config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
# sudo yum repolist -v
# sudo yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.4.3-3.1.el7.x86_64.rpm
# sudo yum install docker-ce -y
# sudo systemctl --now enable docker
# sudo docker run --rm hello-world
## Setting up NVIDIA Container Toolkit
# distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
#    && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
# sudo yum clean expire-cache
# sudo yum install -y nvidia-docker2
# sudo systemctl restart docker
# sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi

# Setting up Docker on RHEL 7
sudo subscription-manager repos --enable rhel-7-server-extras-rpms
sudo yum install docker -y
sudo systemctl --now enable docker
sudo docker -v
sudo docker run --rm hello-world
# Setting up NVIDIA Container Toolkit
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
sudo yum clean expire-cache
sudo yum install nvidia-container-toolkit -y
sudo systemctl restart docker
sudo docker run --rm -e NVIDIA_VISIBLE_DEVICES=all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
