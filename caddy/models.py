from django.db import models
from caddy import STATUS, PHP_VERSION, DRIVER_NAME, MYSQL_VERSION
from config import GATEWAY, WWW_DIR, mkdir, mkfile, CONFIG_DIR


class Vhosts(models.Model):
    domain = models.CharField(
        max_length=100, unique=True, verbose_name='主要域名')
    root = models.CharField(
        max_length=100, verbose_name='网站路径')
    # tls /root/xxx.crt /root/xxx.key
    autossl = models.SmallIntegerField(
        default=0, choices=STATUS, verbose_name="是否启用let's encrypt")
    tls_crt = models.CharField(
        default='', blank=True, max_length=100, verbose_name='tls证书')
    tls_key = models.CharField(
        default='', blank=True, max_length=100, verbose_name='tls私钥')
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
        # 生成配置文件
        if self.domain.find(":") == -1:
            domain = [self.domain + ':80']
        else:
            domain = [self.domain]
        alias = self.alias.all()
        for x in alias:
            if x.domain.find(":") == -1:
                domain.append(x.domain + ':80')
            else:
                domain.append(x.domain)
        strlist = [' '.join(domain) + ' { ']
        path = '%s/%s' % (WWW_DIR, self.root)
        mkdir(path)
        strlist.append('root /var/www/html/%s' % self.root)
        if not self.autossl:
            strlist.append('tls off')
        if self.tls_crt != '' and self.tls_key != '':
            strlist.append('tls %s %s' % (self.tls_crt, self.tls_key))
        if self.php:
            strlist.append('fastcgi / %s:%s php' % (GATEWAY, self.php))
        if self.gzip:
            strlist.append('gzip')
        if self.customize:
            strlist.append(self.customize)
        strlist.append('}')
        string = ' \n'.join(strlist)
        path = '%s/%s/vhosts/%s.conf' % (CONFIG_DIR, DRIVER_NAME, self.domain)
        mkfile(path, string, True)
        return string

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
