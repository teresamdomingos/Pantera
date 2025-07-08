from django.db import models
from django.forms import ValidationError
from datetime import timedelta
from django.contrib.auth.models import User


class Epoca(models.Model):
    nome = models.CharField(max_length=20)  # Ex: "2024/2025"
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Competicao(models.Model):
    nome = models.CharField(max_length=100)


class Clube(models.Model):
    nome = models.CharField(max_length=5)
    nome_completo = models.CharField(max_length=200)
    local = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


class Equipa(models.Model):
    nome = models.CharField(max_length=7)
    letra = models.CharField(max_length=1)
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True, blank=True)
    divisao = models.CharField(max_length=50, blank=True, null=True)
    epoca = models.ForeignKey(Epoca, on_delete=models.CASCADE, null=True, blank=True)
    competicao = models.ForeignKey(Competicao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='fotos_perfil/pessoa.png')

    def __str__(self):
        return f"{self.nome} {self.apelido}"

class Atleta(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    numero_camisola = models.IntegerField()
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.pessoa:
            return f"{self.pessoa.nome} {self.pessoa.apelido}"
        return "Atleta sem pessoa vinculada"

    def get_nome(self):
        if self.pessoa:
            return self.pessoa.nome
        return "N/A"
    get_nome.short_description = 'Nome'

    def get_apelido(self):
        if self.pessoa:
            return self.pessoa.apelido
        return "N/A"
    get_apelido.short_description = 'Apelido'



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
        if self.atleta.pessoa:
            return f"{self.equipa.nome} {self.atleta.pessoa.nome} {self.atleta.pessoa.apelido}"
        return f"{self.equipa.nome} Atleta sem pessoa"

    

class Arbitro(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    escalão_aprendizagem = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.apelido}"

class Treinador(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.apelido}"

class Treinador_Equipa(models.Model):
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    epoca = models.ForeignKey(Epoca, on_delete=models.CASCADE)
    
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('treinador', 'equipa', 'epoca')

class Presidente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.apelido}"

class Presidente_Clube(models.Model):
    presidente = models.ForeignKey(Presidente, on_delete=models.CASCADE)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    epoca = models.ForeignKey(Epoca, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('presidente', 'clube', 'epoca')


class Jogo (models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('a_decorrer', 'A Decorrer'),
        ('terminado', 'Terminado'),
        ('cancelado', 'Cancelado'),
    ]
    
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    equipa_casa = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name="jogos_em_casa")
    equipa_fora = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name="jogos_fora")
    vencedor = models.ForeignKey(Equipa, on_delete=models.SET_NULL, null=True, blank=True, related_name="vitorias")
    
    arbitro_principal = models.CharField(max_length=100, null=True, blank=True)
    arbitro_secundario = models.CharField(max_length=100, null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    pontuacao_equipa_casa = models.IntegerField(default=0)
    pontuacao_equipa_fora = models.IntegerField(default=0)

    tempo_decorrido = models.DurationField(default=timedelta)

    def __str__(self):
        return f"{self.equipa_casa.nome} - {self.equipa_fora.nome} ({self.data} {self.hora})"
    
    @property
    def local(self):
        return self.equipa_casa.clube.local 
    
    def clean(self):
        if self.equipa_casa == self.equipa_fora:
            raise ValidationError("A equipa da casa e a equipa de fora não podem ser a mesma.")


class Pontuacao_Equipa_Jogo (models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    pontos = models.IntegerField()

    class Meta:
        unique_together = ('jogo', 'equipa')


class CestoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(acerto=True)

class Lancamento(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    atleta_responsavel = models.ForeignKey(Atleta, on_delete=models.CASCADE, related_name="lancamentos")
    atleta_assistencia = models.ForeignKey(Atleta, on_delete=models.SET_NULL, null=True, blank=True, related_name="assistencias")
    tipo = models.CharField(max_length=20)
    minuto = models.IntegerField()
    numero = models.IntegerField()
    acerto = models.BooleanField(default=True)

    objects = models.Manager()  # default
    cestos = CestoManager()     # só acertos


class Cesto(models.Model):
    TIPO_CESTO_CHOICES = [
        ('penalti', 'Penálti'),
        ('curto', 'Curto'),
        ('longo', 'Longo'),
        ('passada', 'Passada'),
    ]

    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE, related_name="cestos_marcados")
    tipo = models.CharField(max_length=10, choices=TIPO_CESTO_CHOICES)
    #timestamp = models.DateTimeField(auto_now_add=True)  # opcional: regista quando foi o cesto
    atleta_assistência = models.ForeignKey(Atleta, on_delete=models.CASCADE, null=True, blank=True, related_name="assistencias_dadas")

    def __str__(self):
        return f"{self.atleta} - {self.get_tipo_display()} em {self.jogo}"
    


class Falta(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    minuto = models.IntegerField()
    tipo = models.CharField(max_length=100)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)

class Penalizacao(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    minuto = models.IntegerField()
    numero_cartao = models.IntegerField()

class CartaoAmarelo(models.Model):
    penalizacao = models.OneToOneField(Penalizacao, on_delete=models.CASCADE)

class CartaoVermelho(models.Model):
    penalizacao = models.OneToOneField(Penalizacao, on_delete=models.CASCADE)



class Atleta_Jogo (models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    ESTADOS = [
        ("convocado", "Convocado"),
        ("dispensado", "Dispensado"),
        ("lesionado", "Lesionado"),
        ("castigado", "Castigado")
    ]
    estado_jogador = models.CharField(max_length=20, choices=ESTADOS)

   


class Atleta_Campo(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE)
    substituido = models.BooleanField(default=False)

class Substituicao(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    substituto = models.ForeignKey(Atleta_Campo, on_delete=models.CASCADE, related_name="entrou")
    substituido_por = models.ForeignKey(Atleta_Campo, on_delete=models.CASCADE, related_name="saiu")
    minuto_jogo = models.IntegerField()

    def clean(self):
        if self.substituto.jogo != self.substituido_por.jogo:
            raise ValidationError("Os dois atletas devem pertencer ao mesmo jogo.")
        if self.substituto.equipa != self.substituido_por.equipa:
            raise ValidationError("Os dois atletas devem pertencer à mesma equipa.")


class AcaoJogo(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    minuto = models.IntegerField()
    falta = models.ForeignKey(Falta, on_delete=models.SET_NULL, null=True, blank=True)
    penalizacao = models.ForeignKey(Penalizacao, on_delete=models.SET_NULL, null=True, blank=True)
    substituicao = models.ForeignKey(Substituicao, on_delete=models.SET_NULL, null=True, blank=True)
    lancamento = models.ForeignKey(Lancamento, on_delete=models.SET_NULL, null=True, blank=True)


class Cota(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    epoca = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Referência temporal
    mes = models.IntegerField(choices=[(i, f"{i:02d}") for i in range(1, 13)])
    ano = models.IntegerField()

    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_pagamento = models.DateField(null=True, blank=True)

    TIPO_CHOICES = [
        ("mensal", "Mensal"),
        ("anual", "Anual"),
        ("inscricao", "Inscrição"),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    ESTADO_CHOICES = [
        ("pago", "Pago"),
        ("pendente", "Pendente"),
        ("atrasado", "Em atraso"),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    observacoes = models.TextField(blank=True)

    class Meta:
        unique_together = ('atleta', 'mes', 'ano', 'tipo')  # Evita duplicados para o mesmo mês
