from django.db import models
from .usuario import Usuario

from django.conf import settings

class Projeto(models.Model):
    STATUS = [
        ('P', 'Planejamento'),
        ('A', 'Em andamento'),
        ('T', 'Terminado'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'projetos',
    )

    data_criacao = models.DateField(auto_now_add = True)
    data_atualizacao = models.DateTimeField(auto_now = True)
    status = models.CharField(
        choices = STATUS, 
        default = 'P'
    )

    def __str__(self):
        return f"{self.nome} - ({self.status})"