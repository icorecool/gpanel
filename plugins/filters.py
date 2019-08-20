from django_filters import rest_framework as filters
from .models import Container, List


class ContainerFilter(filters.FilterSet):
    """
    容器 过滤类
    """

    class Meta:
        model = Container
        fields = ['plugins', ]


class ListFilter(filters.FilterSet):
    """
    插件 过滤类
    """

    class Meta:
        model = List
        fields = ['name']
