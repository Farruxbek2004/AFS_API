from django.urls import path
from .views import (
    CategoryApiView,
    CategoryDetailView,
)

#
urlpatterns = [
    path('', CategoryApiView.as_view(), name='category'),
    path('<int:pk>', CategoryDetailView.as_view(), name='category-detail')
]
