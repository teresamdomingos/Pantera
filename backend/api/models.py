from django.db import models
from django.forms import ValidationError

class Clube(models.Model):
    nome = models.CharField(max_length=5)
    nome_completo = models.CharField(max_length=200)
    local = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


class Equipa(models.Model):
    nome = models.CharField(max_length=7)
    letra = models.CharField(max_length=1)
    clube = models.ForeignKey("Clube", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    numero_camisola = models.IntegerField()
    clube = models.ForeignKey("Clube", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.apelido}"
    
class Atleta_Equipa(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)

    def clean(self):
        # Se a equipa não tem clube ou atleta não tem clube, erro
        if not self.equipa.clube:
            raise ValidationError("A equipa deve estar associada a um clube.")
        if not self.atleta.clube:
            raise ValidationError("O atleta deve estar associado a um clube antes de entrar numa equipa.")
        # Também podes validar se clube do atleta e clube da equipa são iguais, se quiseres:
        if self.atleta.clube != self.equipa.clube:
            raise ValidationError("O clube do atleta e da equipa devem ser o mesmo.")

    def save(self, *args, **kwargs):
        self.clean()  # Garante que valida ao guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.equipa.nome} {self.atleta.nome}"
    

class Jogo (models.Model):
    data = models.DateField(blank=True, null=True)
    equipa_casa = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name="jogos_em_casa")
    equipa_fora = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name="jogos_fora")
    
    def __str__(self):
        return f"{self.equipa_casa.nome} - {self.equipa_fora.nome}"
    
    @property
    def local(self):
        return self.equipa_casa.clube.local 
    
    def clean(self):
        if self.equipa_casa == self.equipa_fora:
            raise ValidationError("A equipa da casa e a equipa de fora não podem ser a mesma.")


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


