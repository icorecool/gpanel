from rest_framework.routers import DefaultRouter
from .views import ExtViewSet

# 版本1的路由规则
router = DefaultRouter()
# 插件
router.register(r'ext', ExtViewSet,
                base_name="ext")
