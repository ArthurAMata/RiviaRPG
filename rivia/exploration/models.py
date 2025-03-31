from django.db import models

# Create your models here.
class Regiao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False)
    descricao = models.TextField(verbose_name="Descrição", null=False)

    def __str__(self):
        return self.nome
    

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False)
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('cidade', 'Cidade'),
            ('masmorra', 'Masmorra'),
            ('floresta', 'Floresta'),
            ('montanha', 'Montanha'),
            ('deserto', 'Deserto'),
            ('vilarejo', 'Vilarejo'),
        ],
        default='cidade',
        verbose_name="Tipo"
    )
    regiao = models.ForeignKey('Regiao', on_delete=models.CASCADE, verbose_name="Região")
    descricao = models.TextField(verbose_name="Descrição", null=False)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"
    

class Loja(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False)
    localizacao = models.CharField(max_length=255, verbose_name="Localização", null=False)
    itens_disponiveis = models.ManyToManyField('inventory.Item', verbose_name="Itens Disponíveis", blank=True)

    def __str__(self):
        return f"Loja: {self.nome} - Localização: {self.localizacao}"