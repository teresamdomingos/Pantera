from rest_framework import serializers
from .models import Jogador, Jogo, Clube

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    local = serializers.SerializerMethodField()

    class Meta:
        model = Jogo
        fields = ['id', 'data', 'equipa_casa', 'equipa_fora', 'local']

    def get_local(self, obj):
        return obj.local  # Isto usa a property definida no model
    

class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = '__all__'