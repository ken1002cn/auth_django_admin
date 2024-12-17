from django.shortcuts import render
from django.views import View

from ai.AicallHandler import AiCallHandler
from auth_django_admin.utill.JsonResultUtill import JsonResponseUtil


# Create your views here.
class SmartSearchView(View):
    def get(self,request):
        message = request.GET.get('message')
        result = AiCallHandler.call(message,"请尽您所能的根据用户的想法推荐一个旅游景点")
        return JsonResponseUtil.success(result)