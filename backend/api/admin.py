from django.contrib import admin
from .models import (
    Epoca, Competicao, Clube, Equipa,
    Pessoa, Atleta, Atleta_Equipa,
    Arbitro, Treinador, Treinador_Equipa, Presidente, Presidente_Clube,
    Jogo, Pontuacao_Equipa_Jogo,
    Cesto, Lancamento,
    Falta, Penalizacao, CartaoAmarelo, CartaoVermelho,
    Atleta_Jogo, Atleta_Campo, Substituicao,
    AcaoJogo, Cota
)

@admin.register(Epoca)
class EpocaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ativo']
    list_filter = ['ativo']

@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nome_completo', 'local']
    search_fields = ['nome', 'nome_completo']

@admin.register(Equipa)
class EquipaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'letra', 'clube', 'epoca', 'competicao', 'divisao']
    list_filter = ['epoca', 'competicao', 'clube']
    search_fields = ['nome']

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    search_fields = ['nome', 'apelido']

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pessoa', 'numero_camisola', 'clube']
    search_fields = ['pessoa__nome', 'pessoa__apelido']
    list_filter = ['clube']

@admin.register(Atleta_Equipa)
class AtletaEquipaAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_nome_atleta', 'equipa']
    list_filter = ['equipa', 'atleta']

    def get_nome_atleta(self, obj):
        if obj.atleta.pessoa:
            return f"{obj.atleta.pessoa.nome} {obj.atleta.pessoa.apelido}"
        return "Atleta sem pessoa"
    get_nome_atleta.short_description = "Atleta"

@admin.register(Arbitro)
class ArbitroAdmin(admin.ModelAdmin):
    list_display = ['id', 'pessoa', 'escalão_aprendizagem', 'ativo']
    list_filter = ['ativo']

@admin.register(Treinador)
class TreinadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'pessoa']

@admin.register(Treinador_Equipa)
class TreinadorEquipaAdmin(admin.ModelAdmin):
    list_display = ['id', 'treinador', 'equipa', 'epoca', 'ativo']
    list_filter = ['epoca', 'ativo']

@admin.register(Presidente)
class PresidenteAdmin(admin.ModelAdmin):
    list_display = ['id', 'pessoa']
    search_fields = ['pessoa__nome', 'pessoa__apelido']

@admin.register(Presidente_Clube)
class PresidenteClubeAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_nome_presidente', 'clube', 'epoca']
    list_filter = ['clube', 'epoca']
    search_fields = ['presidente__pessoa__nome', 'presidente__pessoa__apelido']

    def get_nome_presidente(self, obj):
        return f"{obj.presidente.pessoa.nome} {obj.presidente.pessoa.apelido}"
    get_nome_presidente.short_description = "Presidente"

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'hora', 'equipa_casa', 'equipa_fora', 'vencedor', 'status']
    list_filter = ['status', 'equipa_casa', 'equipa_fora', 'vencedor']
    search_fields = ['equipa_casa__nome', 'equipa_fora__nome']

@admin.register(Pontuacao_Equipa_Jogo)
class PontuacaoEquipaJogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'equipa', 'pontos']

@admin.register(Cesto)
class CestoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'equipa', 'atleta', 'tipo', 'atleta_assistência']
    list_filter = ['tipo', 'equipa']
    search_fields = ['atleta__pessoa__nome']

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'atleta_responsavel', 'tipo', 'acerto', 'minuto']
    list_filter = ['tipo', 'acerto']
    search_fields = ['atleta_responsavel__pessoa__nome']

@admin.register(Falta)
class FaltaAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'minuto', 'tipo', 'atleta']

@admin.register(Penalizacao)
class PenalizacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'atleta', 'minuto', 'numero_cartao']

@admin.register(CartaoAmarelo)
class CartaoAmareloAdmin(admin.ModelAdmin):
    list_display = ['id', 'penalizacao']

@admin.register(CartaoVermelho)
class CartaoVermelhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'penalizacao']

@admin.register(Atleta_Jogo)
class AtletaJogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'equipa', 'atleta', 'estado_jogador']
    list_filter = ['estado_jogador']

@admin.register(Atleta_Campo)
class AtletaCampoAdmin(admin.ModelAdmin):
    list_display = ['id', 'atleta', 'jogo', 'substituido']

@admin.register(Substituicao)
class SubstituicaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'substituto', 'substituido_por', 'minuto_jogo']

@admin.register(AcaoJogo)
class AcaoJogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'jogo', 'minuto', 'falta', 'penalizacao', 'substituicao', 'lancamento']

@admin.register(Cota)
class CotaAdmin(admin.ModelAdmin):
    list_display = ['id', 'atleta', 'epoca', 'ano', 'mes', 'valor', 'estado', 'tipo', 'data_pagamento']
    list_filter = ['epoca', 'estado', 'tipo', 'ano', 'mes']
    search_fields = ['atleta__pessoa__nome']
