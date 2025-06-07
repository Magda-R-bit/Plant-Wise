from django.db import models
from django.utils import timezone


# Shop
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Products
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    def active_deal(self):
        now = timezone.now()
        return self.deals.filter(
            start_date__lte=now,
            end_date__gte=now
        ).first()
