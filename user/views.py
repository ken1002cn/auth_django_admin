import json
from datetime import datetime, timedelta, timezone
from django.views import View
from rest_framework_jwt.settings import api_settings
from django.http import JsonResponse
from .models import SysUser, SysUserSerializer
from auth_django_admin.utill.JsonResultUtill import JsonResponseUtil


class RegisterView(View):
    def post(self, request):
        try:
            # 解析 JSON 数据
            user_data = json.loads(request.body)
            username = user_data.get("username")
            email = user_data.get("email")
            password = user_data.get("password")
            # 创建用户
            SysUser.objects.create(username=username, email=email, password=password)
            # 返回成功的响应
            return JsonResponse({'code': 200, 'message': '注册成功'})
        except Exception as e:
            # 错误处理
            return JsonResponse({'code': 400, 'message': '注册失败，请稍后再试'})


class LoginView(View):
    def post(self,request):
        username = request.GET.get("username")
        password = request.GET.get("password")
        try:
            user = SysUser.objects.get(username=username,password=password)
            # 使用 JWT 设置获取负载处理器和编码处理器
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # 创建有效负载
            payload = jwt_payload_handler(user)
            # 设置 token 过期时间
            exp = datetime.now(timezone.utc) + timedelta(days=1)  # 1 天过期
            payload['exp'] = exp
            # 生成JWT token
            token = jwt_encode_handler(payload)
        except Exception as e:
            print(e)
            return JsonResponseUtil.failure()
        return JsonResponse({'code': 200,'info': '登陆成功','token':token,'data':SysUserSerializer(user).data})

class UserView(View):
    def get(self,request):
        uid = request.GET.get("uid")
        try:
            user = SysUser.objects.get(id=uid)
            return JsonResponseUtil.success(SysUserSerializer(user).data)
        except Exception as e:
            print(e)
            return JsonResponseUtil.failure()

    def post(self,request):
        user_data = json.loads(request.body)
            #更新用户
        user_id = user_data.get("id")
        try:
            db_user = SysUser.objects.get(id=user_id)
            if user_data.get("phone_number"):
                db_user.phone_number = user_data.get("phone_number")
            if user_data.get("email"):
                db_user.email = user_data.get("email")
            db_user.save()
            return JsonResponseUtil.success()
        except Exception as e:
            return  JsonResponseUtil.failure()
