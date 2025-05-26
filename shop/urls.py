from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path(
        'search/',
        views.search_results,
        name='search_results'
    ),
    path(
        'add/',
        views.add_product,
        name='add_product'
    ),
    path(
        'edit/<slug:slug>/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'delete/<slug:slug>/',
        views.delete_product,
        name='delete_product'
    ),
    path(
        '',
        views.product_list,
        name='product_list'
    ),
    path(
        'category/<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
    ),
    path(
        '<slug:slug>/',
        views.product_detail,
        name='product_detail'
    ),

]
