from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AtletaListCreate, EquipaList, JogoListCreate, ClubeListCreate, JogoDetail, is_presidente


urlpatterns = [
    path('atletas/', AtletaListCreate.as_view()),
    path('jogos/', JogoListCreate.as_view()),
    path('clubes/', ClubeListCreate.as_view()),
    path('equipas/', EquipaList.as_view()),
    path('jogos/<int:pk>/', JogoDetail.as_view()),  
    path('is_presidente/', is_presidente),

    # Rotas para autenticação JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login (obter token)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # renovar token
]


