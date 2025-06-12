from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.wishlist_view,
        name='wishlist'
    ),
    path(
        'add/<slug:product_slug>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'remove/<slug:product_slug>/',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),
]
