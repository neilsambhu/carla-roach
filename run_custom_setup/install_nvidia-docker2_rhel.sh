# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker
sudo yum-config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo yum repolist -v
sudo yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.4.3-3.1.el7.x86_64.rpm
sudo yum install docker-ce -y
sudo systemctl --now enable docker
sudo docker run --rm hello-world
