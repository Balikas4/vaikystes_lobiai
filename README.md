# vaikystes_lobiai
Kindergerten website

apt update && apt upgrade -y
apt install git -y

wget https://get.docker.com -O get-docker.sh
sh get-docker.sh

wget "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -O /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
