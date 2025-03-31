from django.db import models

# Create your models here.
class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Nome", null=False)
    user = models.ForeignKey('authent.User', on_delete=models.CASCADE, verbose_name="Usuário")
    character_class = models.ForeignKey('Classe', on_delete=models.CASCADE, verbose_name="Classe")
    race = models.CharField(max_length=100, verbose_name="Raça", null=False)
    birth_region = models.CharField(max_length=100, verbose_name="Região de Nascimento", null=False)
    level = models.IntegerField(default=1, verbose_name="Nível", null=False)
    experience = models.IntegerField(default=0, verbose_name="Experiência", null=False)
    health = models.IntegerField(default=100, verbose_name="Vida", null=False)
    mana = models.IntegerField(default=100, verbose_name="Mana", null=False)
    blessing = models.CharField(max_length=100, verbose_name="Benção", null=True, blank=True)
    sprite = models.ImageField(upload_to="sprites/", verbose_name="Sprite", null=True, blank=True) #resolver isso mais pra frente

    def __str__(self):
        return f"{self.name} (Nível {self.level}) - {self.character_class}"
    

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Nome", null=False)
    description = models.TextField(verbose_name="Descrição", null=False)
    type = models.CharField(max_length=100, verbose_name="Tipo", null=False)

    def __str__(self):
        return self.name
    
class Ocupation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Nome", null=False)
    description = models.TextField(verbose_name="Descrição", null=False)
    benefits = models.TextField(verbose_name="Benefícios", null=False)

    def __str__(self):
        return self.name
    

class Classe(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False)
    descricao = models.TextField(verbose_name="Descrição", null=False)

    def __str__(self):
        return self.nome
    
    