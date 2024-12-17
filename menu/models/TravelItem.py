from django.db import models
from rest_framework import serializers

#旅游景点项模型
class TravelItem(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.TextField(null = True)
    title = models.CharField(max_length=128,null = False)
    status = models.BooleanField(null=True) #管理功能预留
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'travel_item'

# 旅游景点项序列化器
class TravelItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=TravelItem
        fields='__all__'