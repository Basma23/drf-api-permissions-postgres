from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializer import MovieSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthorOrReadOnly,)