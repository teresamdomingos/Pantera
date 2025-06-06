from django.shortcuts import render
from rest_framework import generics
from .models import Jogador,  Jogo
from .serializers import JogadorSerializer, JogoSerializer

class JogadorListCreate(generics.ListCreateAPIView):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class JogoListCreate(generics.ListCreateAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer