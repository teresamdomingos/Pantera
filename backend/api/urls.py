from django.urls import path
from .views import AtletaListCreate, EquipaList, JogoListCreate, ClubeListCreate, JogoDetail

urlpatterns = [
    path('atletas/', AtletaListCreate.as_view()),
    path('jogos/', JogoListCreate.as_view()),
    path('clubes/', ClubeListCreate.as_view()),
    path('equipas/', EquipaList.as_view()),
    path('jogos/<int:pk>/', JogoDetail.as_view()),    

]