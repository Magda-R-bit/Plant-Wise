from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import WishlistItem
from django.contrib import messages


@login_required
def wishlist_view(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'items': items})


@login_required
def add_to_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    messages.success(
        request,
        f"Added {product.name} to your wishlist."
    )
    return redirect(request.META.get('HTTP_REFERER', 'wishlist'))


@login_required
def remove_from_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f"Removed {product.name} from your wishlist.")
    return redirect('wishlist')
