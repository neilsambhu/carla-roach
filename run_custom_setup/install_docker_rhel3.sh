# https://access.redhat.com/discussions/3199282
# https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/getting_started_with_containers/index#getting_docker_in_rhel_7

# subscription-manager list --available    Find valid RHEL pool ID
# subscription-manager attach --pool=pool_id

subscription-manager repos --enable=rhel-7-server-rpms &&
subscription-manager repos --enable=rhel-7-server-extras-rpms &&
subscription-manager repos --enable=rhel-7-server-optional-rpms &&

yum install docker device-mapper-libs device-mapper-event-libs &&

systemctl start docker.service &&
systemctl enable docker.service &&
