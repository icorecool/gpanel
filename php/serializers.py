from rest_framework import serializers
from .models import Ext


class ExtSerializer(serializers.ModelSerializer):
    '''插件列表 序列化器'''

    class Meta:
        models = Ext
        model = models
        exclude = ()
        read_only_fields = ()
