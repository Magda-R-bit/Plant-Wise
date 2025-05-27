from django.urls import path
from . import views

urlpatterns = [
    path('', views.guide_list, name='guide_list'),
    path('tips/', views.tip_list, name='tip_list'),
    path('tips/submit/', views.submit_tip, name='submit_tip'),
    path('<slug:slug>/', views.guide_detail, name='guide_detail'),
]
