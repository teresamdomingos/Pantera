from django.contrib import admin

# Register your models here.
from .models import Clube, Equipa, Atleta, Jogo, Pontuacao_Jogo, Cesto, Atletas_Jogo

admin.site.register(Clube)
admin.site.register(Equipa)
admin.site.register(Atleta)
admin.site.register(Jogo)
admin.site.register(Pontuacao_Jogo)
admin.site.register(Cesto)
admin.site.register(Atletas_Jogo)