from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255, verbose_name="Senha", null=False)
    username = models.CharField(max_length=150, unique=True, verbose_name="Nome de usuário", null=False)
    email = models.EmailField(unique=True, verbose_name="E-mail", null=False)

    def __str__(self):
        return f"Usuário: {self.username} (ID: {self.id})"