from rest_framework import serializers
from .models import Clube, Equipa, Atleta, Jogo, Pontuacao_Jogo, Cesto, Atletas_Jogo, Atleta_Equipa

class AtletaSerializer(serializers.ModelSerializer):
    clube_nome = serializers.CharField(source='clube.nome', read_only=True)
    equipa_letras = serializers.SerializerMethodField()

    class Meta:
        model = Atleta
        fields = ['id', 'nome', 'apelido', 'numero_camisola', 'clube', 'clube_nome', 'equipa_letras']

    def get_equipa_letras(self, obj):
        # Vai buscar todas as letras das equipas a que este atleta pertence
        equipas = Atleta_Equipa.objects.filter(atleta=obj).select_related('equipa')
        return [ae.equipa.letra for ae in equipas if ae.equipa]
    

class JogoSerializer(serializers.ModelSerializer):
    equipa_casa_nome = serializers.CharField(source='equipa_casa.nome', read_only=True)
    equipa_fora_nome = serializers.CharField(source='equipa_fora.nome', read_only=True)
    local = serializers.SerializerMethodField()

    class Meta:
        model = Jogo
        fields = ['id', 'data', 'equipa_casa', 'equipa_fora', 'equipa_casa_nome', 'equipa_fora_nome', 'local']

    def get_local(self, obj):
        return obj.local
    

class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = '__all__'

class EquipaSerializer(serializers.ModelSerializer):
    clube_nome = serializers.CharField(source='clube.nome', read_only=True)

    class Meta:
        model = Equipa
        fields = ['id', 'nome', 'letra', 'clube', 'clube_nome', 'divisao']
