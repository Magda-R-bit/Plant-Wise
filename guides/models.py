from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Guide(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('companion', 'Companion Planting'),
        ('pests', 'Pest Control'),
        ('seasonal', 'Seasonal Tips'),
        ('user', 'User Tips'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='general'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
