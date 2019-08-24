import os
from plugins.base import Base


class Php(Base):
    """docstring for Php"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = {
            '5.6': 9056,
            '7.3': 9073
        }

    def setup(self, container):
        """创建"""
        version = container.plugins.version
        self.driver_name = 'php%s' % version
        self.image = 'ghostry/php:%s-fpm' % version
        container.name = self.driver_name
        # print(container.id)
        confdir = os.path.join(self.config_dir, self.driver_name)
        self.mkdir(confdir)
        configfile = '%s/php-fpm.conf' % confdir
        # 创建配置文件
        self.createConfig(configfile, """[global]
include=etc/php-fpm.d/*.conf""")
        info = {
            "image": self.image,
            "command": '',
            "name": self.driver_name,
            "ports": {
                "9000/tcp": (self.Gateway, self.version[version])
            },
            "volumes": {
                configfile: {"bind": '/usr/local/etc/php-fpm.conf', 'mode': 'ro'},
                self.www_dir: {"bind": '/var/www/html/', 'mode': 'rw'}
            }
        }
        container.args = info['command']
        container.binds = info['volumes']
        container.port_bindings = info['ports']
        try:
            ret = self.driver.create(**info)
        except Exception as e:
            return False
        container.id = ret.attrs['Id']
        container.create_time = ret.attrs['Created']
        return container
