from django.db import models

# Create your models here.
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Clube(models.Model):
    nome = models.CharField(max_length=5)
    nome_completo = models.CharField(max_length=200)
    disciplina = models.ManyToManyField(Disciplina)
    diretor_turma = models.OneToOneField("Professor", on_delete=models.SET_NULL, null=True, blank=True, related_name="turma_diretor")
    local = models.CharField(max_length=500)


class Equipa(models.Model):
    nome = models.CharField(max_length=7)
    letra = models.CharField(max_length=1)
    clube = models.ForeignKey("Clube", on_delete=models.SET_NULL, null=True, blank=True)


class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    numero_camisola = models.IntegerField()
    clube = models.ForeignKey("Clube", on_delete=models.SET_NULL, null=True, blank=True)

class Atleta_Equipa(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)


class Jogo (models.Model):
    data = models.DateField(blank=True, null=True)
    equipa_casa = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name="jogos_em_casa")
    equipa_fora = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name="jogos_fora")
    
    @property
    def local(self):
        return self.equipa_casa.clube.local 


class Pontuacao_Jogo (models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    pontos = models.IntegerField()

    class Meta:
        unique_together = ('jogo', 'equipa')

class Cesto (models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)


class Atletas_Jogo (models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    titular = models.BooleanField(default=False)


