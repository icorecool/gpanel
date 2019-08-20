from rest_framework.routers import DefaultRouter
from .views import VhostsViewSet, DomainViewSet, ProxyViewSet

# 版本1的路由规则
router = DefaultRouter()
# 虚拟主机
router.register(r'vhost', VhostsViewSet,
                base_name="vhost")
# 虚拟主机别名
router.register(r'domain', DomainViewSet,
                base_name="domain")
# 虚拟主机反代
router.register(r'proxy', ProxyViewSet,
                base_name="proxy")
