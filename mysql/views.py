import json
from core import mixins
from core.views import errors
from rest_framework.decorators import action

from .serializers import ListSerializer
from .filters import ListFilter
from .models import List
from plugins.models import List as Plugins
from mysql.mysql import Mysql
from core import randomString
from caddy.models import Vhosts


def createDB(name, ver=5, vhost=None):
    try:
        info = Plugins.objects.get(name='mysql', version=ver)
    except Exception as e:
        return True, '没找到该插件'
    try:
        vhost = Vhosts.objects.get(id=vhost)
    except Exception as e:
        vhost = False
    conf = dict(json.loads(info.config))
    cls_obj = Mysql(**conf)
    password = randomString()
    container = cls_obj.createDB(info.version, password, name)
    if container:
        # 保存数据库
        mysql = List()
        mysql.name = name
        mysql.password = password
        mysql.version = info.version
        if vhost:
            mysql.vhost = vhost
        mysql.save()
    else:
        return True, '没找到该插件'
    return False, '创建成功'


class ListViewSet(mixins.ReadOnlyModelViewSet):
    """
    数据库 管理
    """
    serializer_class = ListSerializer
    queryset = List.objects.all()
    filter_class = ListFilter

    @action(methods=['get'], detail=False)
    def createdb(self, request, *args, **kwargs):
        # 创建数据库
        # 读取插件
        try:
            ver = request.query_params.get('ver')
        except Exception as e:
            pass
        if not ver:
            ver = 5
        try:
            name = request.query_params.get('name')
        except Exception as e:
            return errors(400, '必须指定名称')
        try:
            vhost = request.query_params.get('vhost')
        except Exception as e:
            vhost = None
        error, msg = createDB(name, ver=ver, vhost=vhost)
        if error:
            return errors(404, msg)
        # 返回提示
        return errors(201)

    @action(methods=['get'], detail=False)
    def removedb(self, request, *args, **kwargs):
        # 删除数据库
        # 读取插件
        try:
            mid = int(request.query_params.get('id'))
        except Exception as e:
            return errors(400, '必须指定数据库')
        try:
            mysqldb = List.objects.get(id=mid)
        except Exception as e:
            return errors(404, '没找到该数据库')
        try:
            info = Plugins.objects.get(name='mysql', version=mysqldb.version)
        except Exception as e:
            return errors(404, '没找到该插件')
        conf = dict(json.loads(info.config))
        cls_obj = Mysql(**conf)
        container = cls_obj.removeDB(mysqldb.version, mysqldb.name)
        if container:
            # 删除数据库
            mysqldb.delete()
        else:
            return errors(500)
        # 返回提示
        return errors(204)
