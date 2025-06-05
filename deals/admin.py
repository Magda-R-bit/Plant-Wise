from django.contrib import admin
from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'product',
        'is_active',
        'start_date',
        'end_date',
    )
    list_filter = ('is_active', 'type')
    search_fields = ('name', 'product__name')
