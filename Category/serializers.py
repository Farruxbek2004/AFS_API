from rest_framework import serializers
from .models import Category


class CategorySerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ("title", "slug", "image", "created_at", "position")
