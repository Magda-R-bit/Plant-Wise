from django.db import models
from django.utils import timezone
from shop.models import Product


class Deal(models.Model):
    DEAL_TYPES = [
        ('bogo', 'Buy One Get One Free'),
        ('discount', 'Percentage Discount'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DEAL_TYPES)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='deals'
    )
    value = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True,
        help_text="Only used for discount type (e.g., 10 for 10%)"
    )

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def is_currently_active(self):
        now = timezone.now()
        if self.start_date and self.start_date > now:
            return False
        if self.end_date and self.end_date < now:
            return False
        return self.is_active

    def __str__(self):
        return f"{self.name} - {self.get_type_display()} ({self.product.name})"
