from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import BookSerializer
from .models import Book
from .permissions import PemissionsClass
# Create your views here.
class BookListView(ListAPIView,CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (PemissionsClass,IsAuthenticated)

class BookDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (PemissionsClass,IsAuthenticated)