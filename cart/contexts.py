from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product
from deals.models import Deal
from django.utils.timezone import now


def cart_contents(request):

    cart_items = []
    total = Decimal('0.00')
    product_count = 0
    deal_savings = Decimal('0.00')
    cart = request.session.get('cart', {})

    for slug, quantity in cart.items():
        product = get_object_or_404(Product, slug=slug)
        line_price = product.price * quantity
        savings = Decimal('0.00')
        free_items = 0

        deal = Deal.objects.filter(
                product=product,
                is_active=True,
                start_date__lte=now(),
                end_date__gte=now()
        ).first()

        if deal:
            if deal.type == 'bogo':
                free_items = quantity // 1
                savings = product.price * free_items
            elif deal.type == 'discount' and deal.value:
                savings = (deal.value / 100) * product.price * quantity
                line_price -= savings

        total += line_price
        product_count += quantity
        deal_savings += savings

        cart_items.append({
            'slug': slug,
            'quantity': quantity,
            'product': product,
            'subtotal': product.price * quantity,
            'line_price': line_price,
            'free_items': free_items,
            'discount': savings,
            'savings': savings,
            'deal': deal,
        })

    if total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': Decimal(settings.FREE_DELIVERY_THRESHOLD),
        'grand_total': grand_total,
        'deal_savings': deal_savings,
    }

    return context
