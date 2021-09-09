from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Note, Category


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'category', 'author')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'author')
