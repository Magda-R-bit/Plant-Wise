from django.urls import path
from . import views

urlpatterns = [
    path('', views.active_deals, name='active_deals'),
    path('', views.deal_list, name='deal_list'),
]
