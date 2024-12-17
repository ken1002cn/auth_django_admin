from django.urls import path

from menu.views import TravelItemPageView, TravelItemPageDetailView

urlpatterns = [
    path('travelItem/page',TravelItemPageView.as_view(),name='TravelItemPage'),
    path('travelItem/detail',TravelItemPageDetailView.as_view(),name='TravelItemPageDetail'),
]
