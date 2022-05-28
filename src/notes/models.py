from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    in_archive = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Column(models.Model):
    title = models.CharField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    sort = models.IntegerField()
    in_archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=50)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Check(models.Model):
    title = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CheckList(models.Model):
    title = models.CharField(max_length=50)
    checks = models.ManyToManyField(Check)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
