from rest_framework import serializers
from .models import Container, List


class ContainerSerializer(serializers.ModelSerializer):
    '''插件容器 序列化器'''
    create_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        models = Container
        model = models
        exclude = ()
        read_only_fields = ()


class ListSerializer(serializers.ModelSerializer):
    '''插件列表 序列化器'''
    container = ContainerSerializer()

    class Meta:
        models = List
        model = models
        exclude = ()
        read_only_fields = ()
