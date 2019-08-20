import json
from core import mixins
from core.views import errors
from rest_framework.decorators import action
from .serializers import ListSerializer, ContainerSerializer
from .filters import ListFilter, ContainerFilter
from .models import List, Container


class ListViewSet(mixins.ReadOnlyModelViewSet):
    """
    插件 管理
    """
    serializer_class = ListSerializer
    queryset = List.objects.all()
    filter_class = ListFilter

    @action(methods=['get'], detail=False)
    def setup(self, request, *args, **kwargs):
        # 安装插件
        # 读取插件
        try:
            pid = request.query_params.get('id')
        except Exception as e:
            print(e)
            return errors(400, '必须指定插件')
        try:
            resetup = int(request.query_params.get('re', 0))
        except Exception as e:
            print(e)
            resetup = 0
        try:
            info = List.objects.get(id=pid)
        except Exception as e:
            print(e)
            return errors(404, '没找到该插件')
        try:
            conf = dict(json.loads(request.query_params.get('config')))
        except Exception as e:
            print(e)
            conf = dict(json.loads(info.config))
        try:
            container = Container.objects.get(plugins=info)
            if not resetup:
                return errors(422, '您已经安装该插件')
        except Exception as e:
            print(e)
            container = Container()
            container.plugins = info
        # 调用插件安装
        ip_module = __import__('%s.%s' % (
            info.name, info.name), fromlist=[info.class_name])
        # 使用getattr()获取imp_module的类
        plugins_class = getattr(ip_module, info.class_name)
        cls_obj = plugins_class(**conf)
        container = cls_obj.setup(container)
        # 安装信息入库
        try:
            container.save()
        except Exception as e:
            print(e)
            return errors(500, '保存容器信息失败')
        try:
            info.config = json.dumps(conf)
            info.save()
        except Exception as e:
            print(e)
            return errors(500, '保存配置信息失败')
        # 返回提示
        return errors(200)

    @action(methods=['get'], detail=False)
    def remove(self, request, *args, **kwargs):
        # 卸载插件
        # 读取插件
        try:
            pid = request.query_params.get('id')
        except Exception as e:
            print(e)
            return errors(400, '必须指定插件')
        try:
            info = List.objects.get(id=pid)
        except Exception as e:
            print(e)
            return errors(404, '没找到该插件')
        try:
            container = Container.objects.get(plugins=info)
        except Exception as e:
            print(e)
            return errors(410, '您已经卸载')
        conf = dict(json.loads(info.config))
        # 调用插件安装
        ip_module = __import__('%s.%s' % (
            info.name, info.name), fromlist=[info.class_name])
        # 使用getattr()获取imp_module的类
        plugins_class = getattr(ip_module, info.class_name)
        cls_obj = plugins_class(**conf)
        container = cls_obj.remove(container)
        # 移除容器
        container.delete()
        # 返回提示
        return errors(200)

    @action(methods=['get'], detail=False)
    def restart(self, request, *args, **kwargs):
        # 读取插件
        try:
            pid = request.query_params.get('id')
        except Exception as e:
            print(e)
            return errors(400, '必须指定插件')
        try:
            info = List.objects.get(id=pid)
        except Exception as e:
            print(e)
            return errors(404, '没找到该插件')
        try:
            container = Container.objects.get(plugins=info)
        except Exception as e:
            print(e)
            return errors(410, '您还没有安装插件')
        conf = dict(json.loads(info.config))
        # 调用插件重启
        ip_module = __import__('%s.%s' % (
            info.name, info.name), fromlist=[info.class_name])
        # 使用getattr()获取imp_module的类
        plugins_class = getattr(ip_module, info.class_name)
        cls_obj = plugins_class(**conf)
        container = cls_obj.restart(container)
        # 返回提示
        return errors(200)
