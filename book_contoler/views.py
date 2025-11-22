from rest_framework import generics
from .models import Book
from .serialziers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class BookCrud(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
