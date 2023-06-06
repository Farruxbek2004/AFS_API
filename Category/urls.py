from django.urls import path

from .views import (
    CategoryListCreate,
    CategoryUpdateView,
    CategoryDetailView,
    CategorDeleteView,
    CategoryRetrieveView

)

urlpatterns = [
    path("", CategoryListCreate.as_view(), name="category_list_create"),
    path("<int:pk>/", CategoryRetrieveView.as_view(), name="category_read"),
    path("<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path("<int:pk>/delete/", CategorDeleteView.as_view(), name="category_delete"),
    # path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
