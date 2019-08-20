from django.db import models


class Ext(models.Model):
    name = models.CharField(max_length=20, unique=False, verbose_name='名称')
    cmd = models.CharField(
        null=True, max_length=500, unique=False, verbose_name='安装命令')
    version = models.CharField(
        default='5.6', max_length=3, unique=False, verbose_name='PHP版本')

    class Meta:
        verbose_name = '插件列表'
        verbose_name_plural = verbose_name
