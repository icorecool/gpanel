#ubuntu19.04安装脚本
#安装pipenv
apt update -y
apt install python3-pip -y
pip3 install pipenv
#安装docker
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
systemctl enable docker
systemctl start docker
# 创建目录
mkdir -p /www
chmod 777 /www
# 更新常用docker镜像
docker pull php:5.6-fpm
docker pull phpmyadmin/phpmyadmin
docker pull mysql:5
docker pull blob/caddy:latest
