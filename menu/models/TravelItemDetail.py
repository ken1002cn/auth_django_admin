from django.db import models
from rest_framework import serializers

#旅游景点详情模型
class TravelItemDetail(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField(null = False) #外键，关联旅游景点项
    name = models.CharField(max_length=10, null=True)
    addr = models.TextField(null = True)
    rate = models.IntegerField(null = True)
    ticket_price = models.CharField(max_length=10,null=True)
    ticket_price_unit = models.CharField(max_length=12,null=True)
    introduction = models.CharField(max_length=128,null = False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'travel_item_detail'

# 旅游景点详情序列化器
class TravelItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TravelItemDetail
        fields='__all__'