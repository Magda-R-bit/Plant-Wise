from django.contrib import admin
from .models import Guide


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
