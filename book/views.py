from django.shortcuts import render

from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from .models import Author, Book

# Create your views here.
class AuthorListAPI(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPI(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPI(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPI(generics.RetrieveAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer