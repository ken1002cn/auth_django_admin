from django.urls import path
from user.views import LoginView, UserView, RegisterView

urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('info',UserView.as_view(),name="user"),
    path('register',RegisterView.as_view(),name="register"),
]
