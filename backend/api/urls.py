from django.urls import path
from .views import JogadorListCreate

urlpatterns = [
    path('jogadores/', JogadorListCreate.as_view()),
]