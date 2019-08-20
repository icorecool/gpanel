import json
from core import mixins
from core.views import errors
from rest_framework.decorators import action
from .serializers import ExtSerializer
from .models import Ext
from .php import Php


class ExtViewSet(mixins.ModelViewSet):
    """
    插件 管理
    """
    serializer_class = ExtSerializer
    queryset = Ext.objects.all()

    @action(methods=['get'], detail=False)
    def setup(self, request, *args, **kwargs):
        # 安装插件
        # 读取插件
        try:
            pid = request.query_params.get('id')
        except Exception as e:
            return errors(400, '必须指定插件')
        try:
            info = Ext.objects.get(id=pid)
        except Exception as e:
            return errors(404, '没找到该插件')
        # 安装插件
        php = Php()
        php.ext_install('php%s' % info.version, info.cmd)
        # 返回信息
        return errors(200)
