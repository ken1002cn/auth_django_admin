
from django.urls import path
from ai.views import SmartSearchView

urlpatterns = [
    #请求分发
    path('recommend_travel',SmartSearchView.as_view(),name='recommendTravel'),
]
