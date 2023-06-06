from django.contrib import admin
from .models import AFS, Author, Brand


# Register your models here.


@admin.register(AFS)
class AFSAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Brand)
