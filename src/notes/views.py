from rest_framework import generics, permissions
from notes.models import Board
from notes.serializers import BoardSerializer


class BoardListCreateView(generics.ListCreateAPIView):
    model = Board
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(author=self.request.user)


class BoardDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(author=self.request.user)
