from django.urls import path
from .views import BoardListCreateView, BoardDetailUpdateDestroyView


urlpatterns = [
    path('boards/', BoardListCreateView.as_view()),
    path('board/<pk>/', BoardDetailUpdateDestroyView.as_view()),
]
