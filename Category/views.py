from .serializers import CategoryListSerializers, CategoryCreateSerizlizers
from .models import Category
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from paginations import CustomPageNumberPagination


# class CategoryApiView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get_permissions(self):
#         if self.request.method in SAFE_METHODS:
#             self.permission_classes = [AllowAny]
#         return [permission() for permission in self.permission_classes]
#
#     def get(self, request, *args, **kwargs):
#         category_object = Category.objects.all()
#         serializer = CategorySerializers(category_object, many=True)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(request_body=CategorySerializers)
#     def post(self, request, *args, **kwargs):
#         serializer = CategorySerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(serializer.data)

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = CategoryListSerializers
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CategoryCreateSerizlizers
        return CategoryListSerializers


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerizlizers


class CategorDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
