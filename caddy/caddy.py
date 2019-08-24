import os
from plugins.base import Base
from config import GATEWAY, WWW_DIR, mkdir, mkfile, CONFIG_DIR
from . import STATUS, PHP_VERSION, DRIVER_NAME, MYSQL_VERSION


class Caddy(Base):
    """docstring for Caddy"""

    def __init__(self, email='a@b.c', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.driver_name = DRIVER_NAME
        self.image = "blob/caddy:latest"

    def setup(self, container):
        """创建"""
        ssldir = '%s/ssl' % self.config_dir
        self.mkdir(ssldir)
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
                ssldir: {"bind": '/caddy/ssl', 'mode': 'ro'},
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

    def createstr(self, vhost):
        schemes = ['http://']
        if vhost.autossl:
            schemes.append('https://')
        # 生成配置文件
        if vhost.domain.find(":") == -1:
            domain = []
            for scheme in schemes:
                domain.append(scheme + vhost.domain)
        else:
            domain = [vhost.domain]
        alias = vhost.alias.all()
        for x in alias:
            if x.domain.find(":") == -1:
                for scheme in schemes:
                    domain.append(scheme + x.domain)
            else:
                domain.append(x.domain)
        strlist = [' '.join(domain) + ' { ']
        path = '%s/%s' % (WWW_DIR, vhost.root)
        mkdir(path)
        strlist.append('root /var/www/html/%s' % vhost.root)
        if not vhost.autossl:
            strlist.append('tls off')
        if vhost.tls_crt != '' and vhost.tls_key != '':
            strlist.append(
                'tls /caddy/ssl/%s /caddy/ssl/%s' % (vhost.tls_crt, vhost.tls_key))
        if vhost.php:
            strlist.append('fastcgi / %s:%s php' % (GATEWAY, vhost.php))
        if vhost.gzip:
            strlist.append('gzip')
        if vhost.customize:
            strlist.append(vhost.customize)
        strlist.append('}')
        string = ' \n'.join(strlist)
        path = '%s/%s/vhosts/%s.conf' % (CONFIG_DIR, DRIVER_NAME, vhost.domain)
        mkfile(path, string, True)
        return string
