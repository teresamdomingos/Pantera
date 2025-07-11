# Generated by Django 5.2.2 on 2025-07-07 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_jogo_arbitro_principal_jogo_arbitro_secundario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Epoca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('numero_telemovel', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='atleta',
            name='apelido',
        ),
        migrations.RemoveField(
            model_name='atleta',
            name='nome',
        ),
        migrations.AddField(
            model_name='jogo',
            name='vencedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitorias', to='api.equipa'),
        ),
        migrations.CreateModel(
            name='Atleta_Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substituido', models.BooleanField(default=False)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atleta')),
                ('equipa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipa')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
            ],
        ),
        migrations.CreateModel(
            name='Atleta_Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_jogador', models.CharField(choices=[('convocado', 'Convocado'), ('dispensado', 'Dispensado'), ('lesionado', 'Lesionado'), ('castigado', 'Castigado')], max_length=20)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atleta')),
                ('equipa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipa')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
            ],
        ),
        migrations.AddField(
            model_name='equipa',
            name='competicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.competicao'),
        ),
        migrations.CreateModel(
            name='Cota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField(choices=[(1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12')])),
                ('ano', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('mensal', 'Mensal'), ('anual', 'Anual'), ('inscricao', 'Inscrição')], max_length=20)),
                ('estado', models.CharField(choices=[('pago', 'Pago'), ('pendente', 'Pendente'), ('atrasado', 'Em atraso')], max_length=20)),
                ('observacoes', models.TextField(blank=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atleta')),
                ('epoca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.epoca')),
            ],
            options={
                'unique_together': {('atleta', 'mes', 'ano', 'tipo')},
            },
        ),
        migrations.AddField(
            model_name='equipa',
            name='epoca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.epoca'),
        ),
        migrations.CreateModel(
            name='Falta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atleta')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
            ],
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('minuto', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('acerto', models.BooleanField(default=True)),
                ('atleta_assistencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assistencias', to='api.atleta')),
                ('atleta_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lancamentos', to='api.atleta')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
            ],
        ),
        migrations.CreateModel(
            name='Penalizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto', models.IntegerField()),
                ('numero_cartao', models.IntegerField()),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.atleta')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
            ],
        ),
        migrations.CreateModel(
            name='CartaoVermelho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalizacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.penalizacao')),
            ],
        ),
        migrations.CreateModel(
            name='CartaoAmarelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalizacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.penalizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escalão_aprendizagem', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='atleta',
            name='pessoa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pessoa'),
        ),
        migrations.CreateModel(
            name='Presidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Substituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto_jogo', models.IntegerField()),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
                ('substituido_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saiu', to='api.atleta_campo')),
                ('substituto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrou', to='api.atleta_campo')),
            ],
        ),
        migrations.CreateModel(
            name='AcaoJogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto', models.IntegerField()),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogo')),
                ('falta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.falta')),
                ('lancamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.lancamento')),
                ('penalizacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.penalizacao')),
                ('substituicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.substituicao')),
            ],
        ),
        migrations.CreateModel(
            name='Treinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='TreinadorEquipa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('epoca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.epoca')),
                ('equipa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipa')),
                ('treinador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.treinador')),
            ],
            options={
                'unique_together': {('treinador', 'equipa', 'epoca')},
            },
        ),
        migrations.DeleteModel(
            name='Atletas_Jogo',
        ),
    ]
