# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework import response
from rest_framework.settings import api_settings
from rest_framework import serializers
import hashlib


def default_cache_key_func(view_instance, view_method,
                           request, args, kwargs):
    # 缓存key计算
    string = '.'.join([
        str(args),
        str(kwargs),
        str(request.get_full_path()),
        str(request.method),
        str(request.POST),
        # str(request.COOKIES),
        str(request.GET),
        str(request.scheme),
    ])
    # print(string)
    md5 = hashlib.md5()
    md5.update(string.encode(encoding='utf-8'))
    key = md5.hexdigest()
    # print(key)
    return key


class ConfigPagination(PageNumberPagination):
    """
    查询分页
    """
    # 向后台要多少条
    page_size = 20
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100
    expand_param = {}

    def get_paginated_response(self, data):
        return response.Response(dict({
            'count': self.page.paginator.count,
            #     'next': self.get_next_link(),
            #     'previous': self.get_previous_link(),
            'results': data
        }, **self.expand_param))


class CreateModelMixin(object):
    """自定义的创建model"""

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

errorsList = {
    200: "请求成功",
    201: "新建或修改数据成功",
    202: "请求已经进入后台排队（异步任务）",
    204: "删除数据成功",
    400: "请求参数错误",
    401: "没有权限（令牌、用户名、密码错误）",
    403: "访问被禁止",
    404: "资源不存在",
    406: "请求的格式不可得（比如请求JSON格式，但是只有XML格式）",
    410: "请求的资源已被删除",
    422: "当创建一个对象时，发生一个验证错误。",
    500: "服务器发生错误",
}


def errors(status=400, message=None):
    '''自定义的成功错误提示,支持传入status状态码,message回显信息'''
    data = {
        "detail": ""
    }
    if isinstance(message, str):
        data['detail'] = [message]
    elif isinstance(message, dict):
        data = message
    elif status in errorsList.keys():
        data['detail'] = errorsList[status]
    else:
        assert False, "状态码为%s时,必须传message(格式为str或dict,当前为%s)" % (
            status, type(message))
    return response.Response(data, status)
    # return Response(data, status=None, template_name=None, headers=None,
    # content_type=None)
