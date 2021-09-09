from rest_framework import generics
from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
from .permissions import AuthorPermissions


class NoteList(AuthorPermissions, generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(AuthorPermissions, generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CategoryList(AuthorPermissions, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(AuthorPermissions, generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
