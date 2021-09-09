from django.urls import path
from .views import NoteList, NoteDetail
from .views import CategoryList, CategoryDetail


urlpatterns = [
    path('notes/', NoteList.as_view()),
    path('notes/<int:pk>/', NoteDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
]
