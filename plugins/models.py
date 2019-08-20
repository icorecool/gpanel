from django.db import models


class List(models.Model):
    name = models.CharField(max_length=20, unique=False, verbose_name='名称')
    class_name = models.CharField(
        max_length=20, unique=False, verbose_name='类名称')
    version = models.CharField(
        blank=True, max_length=20, unique=False, verbose_name='版本')
    config = models.CharField(
        default={}, max_length=20, unique=False, verbose_name='配置')

    class Meta:
        verbose_name = '插件列表'
        verbose_name_plural = verbose_name


class Container(models.Model):
    id = models.CharField(
        max_length=65, unique=True, verbose_name='ID')
    plugins = models.OneToOneField(
        List, on_delete=models.CASCADE, verbose_name='相关插件')
    name = models.CharField(
        max_length=65, primary_key=True, unique=True, verbose_name='名称')
    args = models.CharField(
        max_length=512, verbose_name='启动参数')
    binds = models.CharField(
        max_length=512, verbose_name='目录绑定')
    port_bindings = models.CharField(
        max_length=512, verbose_name='端口绑定')
    environment = models.CharField(
        max_length=512, verbose_name='环境变量')
    create_time = models.DateTimeField(
        null=True, verbose_name='创建时间')

    class Meta:
        verbose_name = u'容器列表'
        verbose_name_plural = verbose_name
