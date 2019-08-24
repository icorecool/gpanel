#!/bin/bash
# ubuntu19.04安装脚本
# 安装pipenv
apt update -y
apt install python3-pip -y
pip3 install pipenv
# 安装docker
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
# 设置每个容器日志最大5M
echo '{"log-driver":"json-file","log-opts":{"max-size":"5m","max-file":"1"}}' > /etc/docker/daemon.json
systemctl enable docker
systemctl start docker
# 创建目录
mkdir -p /www
chmod 777 /www
# 更新常用docker镜像
docker pull ghostry/php:5.6-fpm
docker pull phpmyadmin/phpmyadmin
docker pull mysql:5
docker pull blob/caddy:latest
