from django.urls import path

from .views import  FacebookSocialAuthView

urlpatterns = [
    path('faceobok/', FacebookSocialAuthView.as_view(), name='facebook_login'),
]