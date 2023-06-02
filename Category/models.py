from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year = models.IntegerField()
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_query_name='author')
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='category')

    def __str__(self):
        return self.title

    @property
    def image_count(self):
        return self.image_count


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

