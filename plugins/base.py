from config import DRIVER, CONFIG_DIR, WWW_DIR, mkdir, GATEWAY, mkfile, DATABASE_DIR


class Base(object):
    """基础"""
    driver = DRIVER()
    config_dir = CONFIG_DIR
    www_dir = WWW_DIR
    Gateway = GATEWAY
    database_dir = DATABASE_DIR

    def __init__(self, *args, **kwargs):
        self.image = ''
        self.driver_name = ''

    def setup(self, container):
        """创建"""
        pass

    def pull(self, container):
        """更新"""
        self.driver.pull(self.image)
        return self.setup()

    def exec(self, name, cmd, workdir=None):
        """执行"""
        return self.driver.exec(name, cmd, workdir=workdir)

    def remove(self, container):
        """删除"""
        self.driver.remove(container.name)
        return container

    def restart(self, container=None):
        """重启"""
        if container:
            return self.driver.restart(container.name)
        else:
            return self.driver.restart(self.driver_name)

    def mkdir(self, path):
        mkdir(path)

    def createConfig(self, path, value):
        return mkfile(path, value)
