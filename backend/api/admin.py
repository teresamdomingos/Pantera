from django.contrib import admin
from .models import Clube, Equipa, Atleta, Jogo, Pontuacao_Jogo, Cesto, Atletas_Jogo, Atleta_Equipa

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nome_completo', 'local']
    search_fields = ['nome', 'nome_completo']
    list_filter = ['local']

@admin.register(Equipa)
class EquipaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'letra', 'clube']
    search_fields = ['nome']
    list_filter = ['clube']

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'numero_camisola', 'clube']
    search_fields = ['nome', 'apelido']
    list_filter = ['clube']

@admin.register(Atleta_Equipa)
class AtletaEquipaAdmin(admin.ModelAdmin):
    list_display = ['id', 'atleta', 'equipa']
    list_filter = ['equipa']

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'equipa_casa', 'equipa_fora', 'local']
    list_filter = ['data']
    search_fields = ['equipa_casa__nome', 'equipa_fora__nome']

@admin.register(Pontuacao_Jogo)
class PontuacaoJogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'equipa', 'pontos']
    list_filter = ['equipa']

@admin.register(Cesto)
class CestoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'equipa', 'atleta']
    list_filter = ['jogo', 'equipa']

@admin.register(Atletas_Jogo)
class AtletasJogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'equipa', 'atleta', 'titular']
    list_filter = ['titular', 'equipa']
