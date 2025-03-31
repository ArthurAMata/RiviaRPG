from django.db import models

# Create your models here.
class Quest(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False)
    descricao = models.TextField(verbose_name="Descrição", null=False)
    status = models.CharField(
        max_length=50,
        choices=[('pendente', 'Pendente'), ('em progresso', 'Em Progresso'), ('concluída', 'Concluída')],
        default='pendente',
        verbose_name="Status"
    )
    recompensa_xp = models.IntegerField(default=0, verbose_name="Recompensa de XP", null=False)
    recompensa_item = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Recompensa Item")

    def __str__(self):
        return f"Quest: {self.nome} (Status: {self.status})"