from django.contrib import admin
from .models import Note, Category

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)
admin.site.register(Category, NoteAdmin)
