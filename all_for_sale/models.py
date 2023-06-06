import random
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from commit_vs_like.models import LikeDislike


# Create your models here.


class AFS(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year = models.IntegerField()
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    category = models.ForeignKey('Category.Category', on_delete=models.CASCADE, related_name='category')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_query_name='author')
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='category')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='brand', null=True, blank=True)

    @property
    def image_count(self):
        return self.image_count

    @property
    def likes(self):
        return self.like_dislike.filter(type=LikeDislike.LikeDislikeType.Like).count()

    @property
    def dislikes(self):
        return self.like_dislike(type=LikeDislike.LikeDislikeType.DISLIKE).count()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
