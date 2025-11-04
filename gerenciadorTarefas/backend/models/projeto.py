from django.db import models
from django.conf import settings

class Projeto(models.Model):
    STATUS_CHOICES = [
        ('P', 'Planejamento'),
        ('A', 'Em Andamento'),
        ('C', 'Concluído'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projetos'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"{self.nome} ({self.get_status_display()})"
