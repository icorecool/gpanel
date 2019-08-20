from django_filters import rest_framework as filters
from .models import List


class ListFilter(filters.FilterSet):
    """
    数据库 过滤类
    """

    class Meta:
        model = List
        fields = ['name']
