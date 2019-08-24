from django_filters import rest_framework as filters
from .models import Vhosts, Domain, Proxy


class VhostsFilter(filters.FilterSet):
    """
    站点 过滤类
    """

    class Meta:
        model = Vhosts
        fields = ['domain', ]


class DomainFilter(filters.FilterSet):
    """
    别名 过滤类
    """

    class Meta:
        model = Domain
        fields = ['domain', 'vhost']


class ProxyFilter(filters.FilterSet):
    """
    反代 过滤类
    """

    class Meta:
        model = Proxy
        fields = ['vhost']
