from django.urls import path
from .views import JogadorListCreate, JogoListCreate, ClubeListCreate

urlpatterns = [
    path('jogadores/', JogadorListCreate.as_view()),
    path('jogos/', JogoListCreate.as_view()),
    path('clubes/', ClubeListCreate.as_view()),  # <- aqui

]