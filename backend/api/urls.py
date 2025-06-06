from django.urls import path
from .views import JogadorListCreate, JogoListCreate

urlpatterns = [
    path('jogadores/', JogadorListCreate.as_view()),
    path('jogos/', JogoListCreate.as_view()),
]