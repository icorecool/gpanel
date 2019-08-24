import django
import os
import sys
from os.path import abspath, dirname, join

# 使用django的数据库
sys.path.insert(0, abspath(join(dirname(__file__), './')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()
from apache.apache import Apache
if __name__ == '__main__':
    plugins = Apache()
    print(plugins.setup())
