from core import mixins
from core.views import errors
from .serializers import VhostsSerializer, DomainSerializer, ProxySerializer
from .filters import VhostsFilter, DomainFilter, ProxyFilter
from .models import Vhosts, Domain, Proxy
from rest_framework import status
from rest_framework.response import Response
from mysql.views import createDB
from . import DRIVER_NAME
from config import CONFIG_DIR, rmfile


class VhostsViewSet(mixins.ModelViewSet):
    """
    站点管理
    """
    serializer_class = VhostsSerializer
    queryset = Vhosts.objects.all()
    filter_class = VhostsFilter

    def create(self, request, *args, **kwargs):
        # 创建同名数据库
        try:
            mysql = int(request.data.get('mysql'))
        except Exception as e:
            mysql = 0
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # print(mysql)
        # print(serializer.data)
        if mysql:
            error, msg = createDB(
                serializer.data['domain'], ver=mysql, vhost=serializer.data['id'])
            if error:
                return errors(404, 'Vhost创建成功,但是Mysql创建失败' + msg)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # 删除配置文件
        configFile = "%s/%s/vhosts/%s.conf" % (
            CONFIG_DIR, DRIVER_NAME, instance.domain)
        rmfile(configFile)
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 删除配置文件
        configFile = "%s/%s/vhosts/%s.conf" % (
            CONFIG_DIR, DRIVER_NAME, instance.domain)
        rmfile(configFile)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DomainViewSet(mixins.ModelViewSet):
    """
    站点别名管理
    """
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()
    filter_class = DomainFilter

    def create(self, request, *args, **kwargs):
        try:
            Vhosts.objects.get(domain=request.data.get('domain'))
            return errors(422, {'domain': ['域名已经存在']})
        except Exception as e:
            pass
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        # 保存前先校验域名是否存在于主域名
        try:
            Vhosts.objects.get(domain=request.data.get('domain'))
            return errors(422, {'domain': ['域名已经存在']})
        except Exception as e:
            pass
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ProxyViewSet(mixins.ModelViewSet):
    """
    反代 管理
    """
    serializer_class = ProxySerializer
    queryset = Proxy.objects.all()
    filter_class = ProxyFilter
