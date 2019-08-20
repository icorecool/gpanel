import os
from plugins.base import Base
import pymysql


class Mysql(Base):
    """docstring for Php"""

    def __init__(self, password='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = password
        self.version = {
            '5': 3306,
            '8': 3308,
        }

    def setup(self, container):
        """创建"""
        version = container.plugins.version
        self.driver_name = 'mysql%s' % version
        self.image = 'mysql:%s' % version
        container.name = self.driver_name
        # 创建配置目录
        confdir = os.path.join(self.config_dir, self.driver_name)
        self.mkdir(confdir)
        configfile = '%s/my.cnf' % confdir
        # 创建配置文件
        self.createConfig(configfile, """[mysqld]""")
        # 创建数据库目录
        database_dir = '%s/%s' % (self.database_dir, self.driver_name)
        self.mkdir(database_dir)
        # 创建容器
        info = {
            "image": self.image,
            "command": '--character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci',
            "name": self.driver_name,
            "ports": {
                "3306/tcp": (self.Gateway, self.version[version])
            },
            "environment": {
                "MYSQL_ROOT_PASSWORD": self.password
            },
            "volumes": {
                configfile: {"bind": '/etc/mysql/mysql.conf.d/my.cnf', 'mode': 'ro'},
                database_dir: {"bind": '/var/lib/mysql', 'mode': 'rw'}
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

    def createDB(self, version, password, name):
        self.driver_name = 'mysql%s' % version
        port = self.version[version]
        # 创建数据库
        connection = pymysql.connect(host=self.Gateway,
                                     port=port,
                                     user='root',
                                     password=self.password,
                                     charset='utf8')
        # 获取游标
        cursor = connection.cursor()
        # 创建数据表
        try:
            sql = """CREATE USER '%s'@'%s' IDENTIFIED BY '%s';""" % (
                name, self.Gateway, password,)
            effect_row = cursor.execute(sql)
            sql = """GRANT USAGE ON *.* TO '%s'@'%s';""" % (
                name, self.Gateway,)
            effect_row = cursor.execute(sql)
            sql = """CREATE DATABASE IF NOT EXISTS `%s`;""" % (
                name,)
            effect_row = cursor.execute(sql)
            sql = """GRANT ALL PRIVILEGES ON `%s`.* TO '%s'@'%s';""" % (
                name, name, self.Gateway,)
            effect_row = cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
        return True

    def removeDB(self, version, name):
        self.driver_name = 'mysql%s' % version
        port = self.version[version]
        # 创建数据库
        connection = pymysql.connect(host=self.Gateway,
                                     port=port,
                                     user='root',
                                     password=self.password,
                                     charset='utf8')
        # 获取游标
        cursor = connection.cursor()
        # 删除用户和数据表
        try:
            sql = """drop user '%s'@'%s';""" % (
                name, self.Gateway,)
            effect_row = cursor.execute(sql)
            sql = """drop database IF EXISTS `%s`;""" % (
                name,)
            effect_row = cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
        return True
