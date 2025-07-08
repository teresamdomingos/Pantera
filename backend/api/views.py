from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Atleta,  Jogo, Clube, Equipa
from .serializers import AtletaSerializer, EquipaSerializer, JogoSerializer, ClubeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_presidente(request):
    user = request.user

    pessoa = getattr(user, 'pessoa', None)

    is_pres = hasattr(user, 'pessoa')  # apenas verifica se tem pessoa
    nome = ""
    foto_perfil = None

    if pessoa:
        nome = pessoa.nome
        if pessoa.foto_perfil and hasattr(pessoa.foto_perfil, 'url'):
            foto_perfil = pessoa.foto_perfil.url

    return Response({
        "is_presidente": is_pres,
        "nome": nome,
        "foto_perfil": foto_perfil
    })
