from django.db import models
from rest_framework import serializers
#旅游景点详情图片模型
class TravelItemDetailRelImage(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField(null=False)  # 外键，关联旅游景点项
    image_url = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = 'travel_item_detail_rel_image'

# 旅游景点详情图片序列化器
class TravelItemDetailRelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=TravelItemDetailRelImage
        fields='__all__'