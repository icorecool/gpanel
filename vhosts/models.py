from django.db import models
from config import GATEWAY, WWW_DIR, mkdir, mkfile, CONFIG_DIR
from . import STATUS, PHP_VERSION, MYSQL_VERSION
from .vhosts import get_httpd


class Vhosts(models.Model):
    domain = models.CharField(
        max_length=100, unique=True, verbose_name='主要域名')
    root = models.CharField(
        max_length=100, verbose_name='网站路径')
    email = models.CharField(
        default='', blank=True, max_length=100, verbose_name='管理员邮箱')
    # tls /root/xxx.crt /root/xxx.key
    autossl = models.SmallIntegerField(
        default=0, choices=STATUS, verbose_name="是否启用let's encrypt")
    tls_crt = models.CharField(
        default='', blank=True, max_length=100, verbose_name='tls证书')
    tls_key = models.CharField(
        default='', blank=True, max_length=100, verbose_name='tls私钥')
    tls_chain = models.CharField(
        default='', blank=True, max_length=100, verbose_name='tls根证书')
    # tls
    php = models.SmallIntegerField(
        default=0, choices=PHP_VERSION, verbose_name="php版本")
    gzip = models.SmallIntegerField(
        default=0, choices=STATUS, verbose_name="是否启用gzip")
    customize = models.CharField(
        default='', blank=True, max_length=300, verbose_name='自定义内容')
    mysql = models.SmallIntegerField(
        default=0, choices=MYSQL_VERSION, verbose_name="mysql版本")
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建时间')

    def createstr(self):
        DRIVER_NAME, DRIVER_CLASS = get_httpd()
        return DRIVER_CLASS().createstr(vhost=self)

    class Meta:
        verbose_name = u'网站列表'
        verbose_name_plural = verbose_name


class Domain(models.Model):
    domain = models.CharField(
        max_length=100, unique=True, verbose_name='别名')
    vhost = models.ForeignKey(
        Vhosts, on_delete=models.CASCADE, related_name="alias", verbose_name='相关网站')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '网站别名'
        verbose_name_plural = verbose_name


class Proxy(models.Model):
    vhost = models.ForeignKey(
        Vhosts, on_delete=models.CASCADE, related_name="proxy", verbose_name='相关网站')
    from_path = models.CharField(
        default='/', max_length=100, verbose_name='请求路径')
    to_url = models.CharField(
        max_length=200, verbose_name='目标url')
    websocket = models.SmallIntegerField(
        default=0, choices=STATUS, verbose_name="websocket")
    without = models.CharField(
        max_length=100, blank=True, verbose_name='排除字符串')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '反向代理'
        verbose_name_plural = verbose_name
