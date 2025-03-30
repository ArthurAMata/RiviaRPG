from django.db import models

class personagems(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)
    experiencia = models.IntegerField(default=0)
    vida = models.IntegerField(default=100)
    mana = models.IntegerField(default=50)

class Inventario(models.Model):
    personagem = models.ForeignKey(personagems, on_delete=models.CASCADE)
    item_nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)

