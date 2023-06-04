from rest_framework import serializers
from .models import Comment, LikeDislike


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Mete:
        model = Comment
        fields = ['description', 'owner', 'afs']
        read_only_fields = ('id',)


class LikeDislikeSerializers(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=LikeDislike.LikeDislikeType.choices)

    class Meta:
        model = LikeDislike
        fields = ['afs', 'user', 'type']
