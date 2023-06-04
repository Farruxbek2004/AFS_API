from django.contrib import admin

from .models import Category


# Register your models here.

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "created_at"]



