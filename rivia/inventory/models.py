from django.db import models

# Create your models here.
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    personagem = models.ForeignKey('characters.Character', on_delete=models.CASCADE, verbose_name="Personagem")

    def __str__(self):
        return f"Inventário de {self.personagem.name}"
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False)
    tipo = models.CharField(max_length=100, verbose_name="Tipo", null=False)
    descricao = models.TextField(verbose_name="Descrição", null=False)
    qtd = models.IntegerField(default=1, verbose_name="Quantidade", null=False)

    def __str__(self):
        return f"{self.nome} ({self.qtd} unidades)"