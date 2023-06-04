from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from all_for_sale.models import AFS
from .models import LikeDislike, Comment
from .serializers import CommentSerializers, LikeDislikeSerializers


# Create your views here.

class LikeDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=LikeDislikeSerializers)
    def post(self, request, *args, **kwargs):
        serializer = LikeDislikeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        like_dislike_type = serializer.validated_data.get('type')
        afs = AFS.objects.filter(id=self.kwargs.get('pk')).first()
        if not afs:
            raise Http404
        like_dislike_blog = LikeDislike.objects.filter(afs=afs, user=user).first()
        if like_dislike_blog and like_dislike_type.type == like_dislike_type:
            like_dislike_blog.delete()
        else:
            LikeDislike.objects.update_or_create(afs=afs, user=user, defaults={"type": like_dislike_type})

        return Response({"type": like_dislike_type, "detail": "Like or Dislike."})
