from django.db import models
from rest_framework import serializers

#特色美食模型
class FeaturedCuisine(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField(null=False)  # 外键，关联旅游景点项
    image_url = models.TextField(null = True)
    introduction = models.CharField(max_length=128,null = False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'featured_cuisine'

# 特色美食序列化器
class FeaturedCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeaturedCuisine
        fields='__all__'