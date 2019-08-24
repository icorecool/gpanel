from apache.apache import Apache
from caddy.caddy import Caddy
from plugins.models import List


def get_httpd():
    DRIVER_NAME = 'apache'
    DRIVER_CLASS = Apache
    # 判断当前安装的是什么
    try:
        apache = List.objects.get(name='apache').container.id
        DRIVER_NAME = 'apache'
        DRIVER_CLASS = Apache
    except Exception as e:
        print(e)
    try:
        caddy = List.objects.get(name='caddy').container.id
        DRIVER_NAME = 'caddy'
        DRIVER_CLASS = Caddy
    except Exception as e:
        print(e)
    print(DRIVER_NAME, DRIVER_CLASS)
    return DRIVER_NAME, DRIVER_CLASS
