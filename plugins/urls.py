from rest_framework.routers import DefaultRouter
from .views import ListViewSet

# 版本1的路由规则
router = DefaultRouter()
# 插件列表
router.register(r'list', ListViewSet,
                base_name="list")
