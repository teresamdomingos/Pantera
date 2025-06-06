from django.shortcuts import render
from rest_framework import generics
from .models import Jogador
from .serializers import JogadorSerializer

class JogadorListCreate(generics.ListCreateAPIView):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
# Create your views here.
