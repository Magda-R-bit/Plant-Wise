from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop.models import Product
from wishlist.models import WishlistItem


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, slug):
    """ Add a quantity of the specified product to the shopping cart """
    product = get_object_or_404(Product, slug=slug)

    if request.method != "POST":
        messages.error(request, "Invalid request method.")
        return redirect("shop:product_list")

    quantity_str = request.POST.get("quantity")
    if not quantity_str:
        messages.error(request, "No quantity provided.")
        return redirect("shop:product_detail", slug=slug)

    try:
        quantity = int(quantity_str)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messages.error(request, "Invalid quantity.")
        return redirect("shop:product_detail", slug=slug)

    get_object_or_404(Product, slug=slug)

    redirect_url = request.POST.get("redirect_url") or "/"
    cart = request.session.get("cart", {})

    if slug in cart:
        cart[slug] += quantity
    else:
        cart[slug] = quantity

    if request.user.is_authenticated:
        WishlistItem.objects.filter(
            user=request.user,
            product__slug=slug
        ).delete()

    request.session["cart"] = cart
    messages.success(request, f'Added {product.name} to your cart')
    return redirect(redirect_url)


def update_cart(request, slug):
    quantity = int(request.POST.get('quantity', 0))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[slug] = quantity
        messages.success(request, f'Updated quantity for {slug.title()}')
    else:
        cart.pop(slug)
        messages.success(request, f'Removed {slug.title()} from your cart')

    request.session['cart'] = cart
    return redirect('view_cart')


def remove_from_cart(request, slug):
    cart = request.session.get('cart', {})
    cart.pop(slug, None)
    request.session['cart'] = cart
    messages.success(request, f'Removed {slug.title()} from your cart.')
    return redirect('view_cart')
