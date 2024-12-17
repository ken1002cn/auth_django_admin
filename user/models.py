from django.core.serializers import serialize
from django.db import models
from rest_framework import serializers


#用户模型
class SysUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    avatar = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=11)
    login_date = models.DateTimeField(null=True)
    status = models.BooleanField(null=True,verbose_name='帐号状态')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'sys_user'

# 用户序列化器
class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=SysUser
        fields='__all__'
