import os
from plugins.base import Base
from config import GATEWAY, WWW_DIR, mkdir, mkfile, CONFIG_DIR
from . import STATUS, PHP_VERSION, DRIVER_NAME, MYSQL_VERSION


class Apache(Base):
    """docstring for Apache"""
    '''
    docker run --rm -it --name=apache -v $PWD/logs:/usr/local/apache2/logs -v $PWD/vhosts:/usr/local/apache2/vhosts httpd:alpine

    docker run --rm -it --name=apache -v $PWD/httpd.conf:/usr/local/apache2/conf/httpd.conf:ro -v $PWD/logs:/usr/local/apache2/logs -v $PWD/vhosts:/usr/local/apache2/vhosts httpd:alpine

    docker exec -it apache sh
    '''

    def __init__(self, email='a@b.c', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.driver_name = 'apache'
        self.image = "httpd:alpine"

    def setup(self, container):
        """创建"""
        ssldir = '%s/ssl' % self.config_dir
        self.mkdir(ssldir)
        confdir = os.path.join(self.config_dir, self.driver_name)
        self.mkdir(confdir)
        vhostsdir = '%s/vhosts' % confdir
        self.mkdir(vhostsdir)
        self.mkdir('%s/default' % self.www_dir)
        # 创建配置文件
        file = 'apache/httpd.conf'
        file_context = open(file).read()
        configfile = '%s/httpd.conf' % confdir
        self.createConfig(
            configfile, file_context + '\nServerAdmin ' + self.email)
        info = {
            "image": self.image,
            "command": '',
            "name": self.driver_name,
            "ports": {
                "80/tcp": 80,
                "443/tcp": 443
            },
            "volumes": {
                configfile: {"bind": '/usr/local/apache2/conf/httpd.conf', 'mode': 'ro'},
                vhostsdir: {"bind": '/usr/local/apache2/vhosts', 'mode': 'ro'},
                ssldir: {"bind": '/usr/local/apache2/ssl', 'mode': 'ro'},
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
        # 生成vhost字符串
        strlist = []
        # 主域名
        strlist.append('ServerName %s' % vhost.domain)
        # 别名
        alias = vhost.alias.all()
        if alias:
            aliasdomain = []
            for x in alias:
                aliasdomain.append(x.domain)
            strlist.append('ServerAlias %s' % ' '.join(aliasdomain))
        if vhost.email != '':
            strlist.append('ServerAdmin %s' % vhost.email)
        # 根目录
        path = '%s/%s' % (WWW_DIR, vhost.root)
        mkdir(path)
        strlist.append('DocumentRoot /var/www/html/%s' % vhost.root)
        # php
        if vhost.php:
            strlist.append(
                '<Proxy "fcgi://%s:%s/" enablereuse=on max=10>' % (GATEWAY, vhost.php))
            strlist.append('</Proxy>')
            strlist.append('<FilesMatch "\\.php$">')
            strlist.append(
                'SetHandler "proxy:fcgi://%s:%s"' % (GATEWAY, vhost.php))
            strlist.append('</FilesMatch>')
            strlist.append('AddType application/x-httpd-php .php')
            strlist.append('DirectoryIndex index.html index.htm index.php')
        # 反向代理
        proxys = vhost.proxy.all()
        for proxy in proxys:
            strlist.append('<Location %s>' % proxy.from_path)
            strlist.append('ProxyPass %s' % proxy.to_url)
            strlist.append('ProxyPassReverse %s' % proxy.to_url)
            strlist.append(
                'RequestHeader append X-Forwarded-For %%{REMOTE_ADDR}s')
            strlist.append('</Location>')
        # 合并
        base_string = '\n'.join(strlist)
        strlist = [
            '<VirtualHost *:80>',
            base_string,
            '</VirtualHost>',
        ]
        # ssl
        if vhost.tls_crt != '' and vhost.tls_key != '':
            strlist.append('<VirtualHost *:443>')
            strlist.append(base_string)
            strlist.append('SSLEngine on')
            strlist.append(
                'SSLCertificateFile /usr/local/apache2/ssl/%s' % vhost.tls_crt)
            strlist.append(
                'SSLCertificateKeyFile /usr/local/apache2/ssl/%s' % vhost.tls_key)
            if vhost.tls_chain != '':
                strlist.append(
                    'SSLCertificateChainFile /usr/local/apache2/ssl/%s' % vhost.tls_chain)
            strlist.append('</VirtualHost>')
        # 输出
        string = ' \n'.join(strlist)
        path = '%s/%s/vhosts/%s.conf' % (CONFIG_DIR, DRIVER_NAME, vhost.domain)
        mkfile(path, string, True)
        return string
