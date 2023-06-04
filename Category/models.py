from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category_image = models.ImageField(upload_to='media', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
