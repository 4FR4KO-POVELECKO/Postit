from django.contrib import admin
from .models import Board, Column, Card, Tag, Check, CheckList, Comment


admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Card)
admin.site.register(Tag)
admin.site.register(Check)
admin.site.register(CheckList)
admin.site.register(Comment)
