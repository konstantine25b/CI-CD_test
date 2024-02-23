from django.shortcuts import render
from rest_framework.viewsets import viewsets
from .models import Book 
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.add()
    serializer_class =BookSerializer