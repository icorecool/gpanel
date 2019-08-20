from driver.base import Base
import docker


class Docker(Base):
    """docstring for Docker"""

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.client = docker.DockerClient(
            base_url='unix://var/run/docker.sock')
        self.info = {
            "mem_swappiness": 0,
        }

    def create(self, name, image, command=None, ports={}, volumes={}, environment={}, detach=True, restart='always'):
        """创建"""
        # 检查是否存在
        try:
            self.remove(name)
        except Exception as e:
            pass
        if detach:
            self.info['detach'] = detach
        if restart:
            self.info['restart_policy'] = {"Name": restart}
        self.info['name'] = name
        self.info['ports'] = ports
        self.info['volumes'] = volumes
        self.info['environment'] = environment
        info = self.client.containers.run(image, command, **self.info)
        return info

    def pull(self, image):
        """更新镜像"""
        return self.client.images.pull(image)

    def remove(self, name):
        """删除"""
        container = self.client.containers.get(name)
        container.stop()
        return container.remove()

    def edit(self):
        """编辑"""
        pass

    def restart(self, name):
        """重启"""
        container = self.client.containers.get(name)
        container.stop()
        return container.start()

    def exec(self, name, cmd, stdout=True, stderr=True, stdin=False, tty=False, privileged=False, user='', detach=False, stream=False, socket=False, environment=None, workdir=None, demux=False):
        container = self.client.containers.get(name)
        return container.exec_run(
            cmd, stdout, stderr, stdin, tty, privileged,
            user, detach, stream, socket, environment, workdir, demux)
