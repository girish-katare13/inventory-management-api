from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer