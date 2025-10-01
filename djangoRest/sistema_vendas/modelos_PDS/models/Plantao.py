from django.db import models
from .Escala import Escala

class Plantao(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('AVISTA', 'À Vista'),
        ('PIX', 'Pix'),
        ('CARTAO', 'Cartão'),
        ('BOLETO', 'Boleto'),
    ]

    escala = models.ForeignKey(Escala, on_delete=models.CASCADE, related_name="plantoes")
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()
    estimativa_valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO_CHOICES, default='PIX')
    estimativa_pagamento = models.DateField()
    comentario = models.TextField(blank=True, null=True)
    quantidade_profissionais = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plantão {self.hora_entrada.strftime('%H:%M')} - {self.hora_saida.strftime('%H:%M')} ({self.escala.nome})"