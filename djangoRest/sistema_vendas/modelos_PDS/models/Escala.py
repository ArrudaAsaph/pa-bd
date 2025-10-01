from django.db import models

class Escala(models.Model):
    STATUS_CHOICES = [
        ('ATIVA', 'Ativa'),
        ('FECHADA', 'Fechada'),
        ('RASCU', 'Rascunho'),
    ]

    nome = models.CharField(max_length=100)
    mes_da_escala = models.DateField(help_text="Data de referência para o mês da escala")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='RASCU')
    data_criacao = models.DateTimeField(auto_now_add=True) 
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.mes_da_escala.strftime('%B %Y')}"
