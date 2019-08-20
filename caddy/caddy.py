import os
from plugins.base import Base
from caddy import DRIVER_NAME


class Caddy(Base):
    """docstring for Caddy"""

    def __init__(self, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.driver_name = DRIVER_NAME
        self.image = "blob/caddy:latest"

    def setup(self, container):
        """创建"""
        confdir = os.path.join(self.config_dir, self.driver_name)
        self.mkdir(confdir)
        self.mkdir('%s/vhosts' % confdir)
        self.mkdir('%s/default' % self.www_dir)
        # 创建配置文件
        self.createConfig(
            '%s/Caddyfile' % confdir, "import /caddy/conf/vhosts/*.conf")
        # 创建默认网站
        self.createConfig("%s/vhosts/default.conf" % confdir, """:80 {
    gzip
    tls off
    root /var/www/html/default/
    index index.html index.htm
}""")
        # 创建默认主页
        self.createConfig('%s/default/index.html' % self.www_dir, """<html>
<head><title>It's runing</title></head>
<body>It's runing</body>
</html>""")
        info = {
            "image": self.image,
            "command": '-conf="/caddy/conf/Caddyfile" -email %s -agree ' % self.email,
            "name": self.driver_name,
            "ports": {
                "80/tcp": 80,
                "443/tcp": 443
            },
            "volumes": {
                confdir: {"bind": '/caddy/conf/', 'mode': 'rw'},
                self.www_dir: {"bind": '/var/www/html/', 'mode': 'rw'}
            }
        }
        # 保存容器信息
        container.name = self.driver_name
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
