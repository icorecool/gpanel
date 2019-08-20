#!/bin/sh
export LC_ALL=C.UTF-8;
export LANG=C.UTF-8;
cd $(dirname $(readlink -f "$0"))
#检查Django是否安装
pipenvInstalled=`pipenv run pip freeze 2>>/dev/null|grep 'Django'|wc -l`
if [ "$pipenvInstalled" != "1" ];then
    pipenv install
fi
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate