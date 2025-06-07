from django.urls import path
from .views import AtletaListCreate, JogoListCreate, ClubeListCreate

urlpatterns = [
    path('atletas/', AtletaListCreate.as_view()),
    path('jogos/', JogoListCreate.as_view()),
    path('clubes/', ClubeListCreate.as_view()),  
    

]