from django.shortcuts import render
from .models import Deal
from django.utils.timezone import now


def active_deals(request):
    deals = [
        deal
        for deal in Deal.objects.select_related('product').all()
        if deal.is_currently_active()
    ]
    return render(request, 'deals/active_deals.html', {'deals': deals})


def deal_list(request):
    active_deals = Deal.objects.filter(
        start_date__lte=now(),
        end_date__gte=now()
    )
    return render(request, 'deals/deal_list.html', {
        'deals': active_deals
    })
