"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.static import serve
from django.contrib import admin
from . import settings
from vhosts.urls import router as vhosts
from plugins.urls import router as plugins
from mysql.urls import router as mysql
from django.views.generic import TemplateView
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$',
        TemplateView.as_view(
            template_name='dist/index.html'),
        name='index'),
    url(r'^admin/', admin.site.urls),
    # 版本1
    path('v1/vhosts/', include(vhosts.urls)),
    path('v1/plugins/', include(plugins.urls)),
    path('v1/mysql/', include(mysql.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$',
                            serve, {'document_root': settings.MEDIA_ROOT}), ]
