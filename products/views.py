from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(summary='создание продуктов')
)
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@extend_schema_view(
    get=extend_schema(summary='получить по id продукт')
)
class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

@extend_schema_view(
    delete=extend_schema(summary='удалить продукт')
)
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

@extend_schema_view(
    get=extend_schema(summary='получить продукты')
)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer