from django.urls import path
from .views import LikeDislikeView

urlpatterns = [
    path('<int:pk>/like_dislike', LikeDislikeView.as_view(), name='like-dislike')
]
