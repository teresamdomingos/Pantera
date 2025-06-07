from django.shortcuts import render
from rest_framework import generics
from .models import Atleta,  Jogo, Clube
from .serializers import AtletaSerializer, JogoSerializer, ClubeSerializer

class AtletaListCreate(generics.ListCreateAPIView):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class JogoListCreate(generics.ListCreateAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class ClubeListCreate(generics.ListCreateAPIView):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer