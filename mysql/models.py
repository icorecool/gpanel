from django.db import models


class List(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='名称')
    version = models.CharField(
        default='5', max_length=1, unique=False, verbose_name='版本')
    password = models.CharField(
        max_length=32, unique=False, verbose_name='密码')
    vhost = models.ForeignKey(
        "vhosts.Vhosts", on_delete=models.DO_NOTHING, null=True, related_name="mysqldb", verbose_name='相关网站')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '数据库列表'
        verbose_name_plural = verbose_name
