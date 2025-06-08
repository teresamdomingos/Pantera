from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Atleta,  Jogo, Clube, Equipa
from .serializers import AtletaSerializer, EquipaSerializer, JogoSerializer, ClubeSerializer

class AtletaListCreate(generics.ListCreateAPIView):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class JogoListCreate(generics.ListCreateAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class ClubeListCreate(generics.ListCreateAPIView):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer

class EquipaList(generics.ListAPIView):
    queryset = Equipa.objects.all()
    serializer_class = EquipaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['divisao']  # Permite filtrar pela coluna divisao

class JogoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer