from django.contrib import admin
from .models import Clube, Equipa, Atleta, Jogo, Pontuacao_Equipa_Jogo, Cesto, Atletas_Jogo, Atleta_Equipa

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nome_completo', 'local']
    search_fields = ['nome', 'nome_completo']
    list_filter = ['local']

@admin.register(Equipa)
class EquipaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'letra', 'clube', 'divisao']
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
    list_display = ['id', 'data', 'hora', 'equipa_casa', 'pontuacao_equipa_casa', 'equipa_fora', 'pontuacao_equipa_fora', 'status', 'tempo_formatado', 'arbitro_principal', 'arbitro_secundario', 'local']
    list_filter = ['data', 'status']
    search_fields = ['equipa_casa__nome', 'equipa_fora__nome']

    @admin.display(description="Tempo decorrido")
    def tempo_formatado(self, obj):
        if obj.tempo_decorrido:
            minutos = int(obj.tempo_decorrido.total_seconds() // 60)
            segundos = int(obj.tempo_decorrido.total_seconds() % 60)
            return f"{minutos}m {segundos}s"
        return "-"

@admin.register(Pontuacao_Equipa_Jogo)
class PontuacaoEquipaJogoAdmin(admin.ModelAdmin):
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
