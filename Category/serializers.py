from rest_framework import serializers
from .models import Category


class CategoryListSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ("title", "slug", "image", "created_at", "position")


class CategoryCreateSerizlizers(serializers.Serializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Category
        fields = ('title', 'slug', 'image', 'created_at', 'position')
        read_only_fields = ('id',)


