import os
from plugins.base import Base


class PhpMyAdmin(Base):
    """docstring for Php"""

    def __init__(self, hosts, ports, port=8887, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hosts = hosts
        self.ports = ports
        self.port = port
        self.driver_name = 'phpmyadmin'
        self.image = 'phpmyadmin/phpmyadmin'

    def setup(self, container):
        """创建"""
        container.name = self.driver_name
        # 创建配置目录
        confdir = os.path.join(self.config_dir, self.driver_name)
        self.mkdir(confdir)
        configfile = '%s/config.user.inc.php' % confdir
        # 创建配置文件
        self.createConfig(configfile, """<?php
            """)
        # 创建容器
        info = {
            "image": self.image,
            "command": '',
            "name": self.driver_name,
            "ports": {
                "80/tcp": self.port
            },
            "environment": {
                "PMA_HOSTS": self.hosts,
                "PMA_PORTS": self.ports
            },
            "volumes": {
                configfile: {"bind": '/etc/phpmyadmin/config.user.inc.php', 'mode': 'ro'}
            }
        }
        container.args = info['command']
        container.binds = info['volumes']
        container.port_bindings = info['ports']
        try:
            ret = self.driver.create(**info)
        except Exception as e:
            print(e)
            return False
        container.id = ret.attrs['Id']
        container.create_time = ret.attrs['Created']
        return container
