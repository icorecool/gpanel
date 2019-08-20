from rest_framework import serializers
from .models import List


class ListSerializer(serializers.ModelSerializer):
    '''数据库列表 序列化器'''

    class Meta:
        models = List
        model = models
        exclude = ()
        read_only_fields = ()
