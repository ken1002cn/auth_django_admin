from django.db import models
from rest_framework import serializers

#产品模型
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField(null=False)  # 外键，关联旅游景点项
    image_url = models.TextField(null = True)
    introduction = models.CharField(max_length=128,null = False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'product'

# 产品序列化器
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'