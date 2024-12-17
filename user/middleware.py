from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import ExpiredSignatureError, InvalidTokenError, PyJWTError
from rest_framework_jwt.settings import api_settings

#jwt拦截器
class JwtAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self,request):
        white_list = ["/user/login","/user/register"] #请求白名单
        path = request.path
        if path not in white_list and not path.startswith("/media"):
            #进行验权
            token = request.META.get("HTTP_AUTHORIZATION")
            try:
                # 不报错直接放行
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                jwt_decode_handler(token)
            except ExpiredSignatureError:
                return HttpResponse('token过期，请重新登录')
            except InvalidTokenError:
                return HttpResponse('token验证不通过')
            except PyJWTError:
                return HttpResponse("token验证失败")
        else:
            #直接放行
            return None