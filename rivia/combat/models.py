from django.db import models

# Create your models here.
class Combat(models.Model):
    id = models.AutoField(primary_key=True)
    personagem = models.ForeignKey('characters.Character', on_delete=models.CASCADE, verbose_name="Personagem")
    inimigo = models.ForeignKey('characters.Character', on_delete=models.CASCADE, related_name="batalhas_como_inimigo", verbose_name="Inimigo")
    status = models.CharField(
        max_length=50,
        choices=[('em andamento', 'Em Andamento'), ('vitória', 'Vitória'), ('derrota', 'Derrota')],
        default='em andamento',
        verbose_name="Status"
    )

    def __str__(self):
        return f"Batalha de {self.personagem.name} contra {self.inimigo.name} (Status: {self.status})"