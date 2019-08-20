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
        self.image = 'php:%s-fpm' % version
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

    def ext_install(self, container_name, name, cmd=None):
        # docker-php-ext-install -j$(nproc) pdo_mysql
        # bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter
        # ftp gd gettext gmp hash iconv imap interbase intl json ldap mbstring
        # mcrypt mssql mysql mysqli oci8 odbc opcache pcntl pdo pdo_dblib
        # pdo_firebird pdo_mysql pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql
        # phar posix pspell readline recode reflection session shmop simplexml
        # snmp soap sockets spl standard sybase_ct sysvmsg sysvsem sysvshm tidy
        # tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zip
        # curl -o ioncube.tar.gz https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
        # tar -xvvzf ioncube.tar.gz
        # mv ioncube/ioncube_loader_lin_5.6.so `php-config --extension-dir`
        # rm -Rf ioncube.tar.gz ioncube
        # docker-php-ext-enable ioncube_loader_lin_5.6
        if not cmd:
            cmd = 'docker-php-ext-install -j$(nproc) %s' % name
        self.exec(container_name, cmd)
