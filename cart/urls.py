from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('update/<slug:slug>/', views.update_cart, name='update_cart'),
    path('remove/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
]
