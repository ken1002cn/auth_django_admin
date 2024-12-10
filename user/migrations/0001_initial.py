# Generated by Django 5.1.4 on 2024-12-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('avatar', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('login_date', models.DateTimeField(null=True)),
                ('status', models.BooleanField(null=True, verbose_name='帐号状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('remark', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_user',
            },
        ),
    ]