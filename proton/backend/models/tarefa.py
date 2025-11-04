from django.db import models
from .projeto import Projeto

class Tarefa(models.Model):
    PRIORIDADE = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta')
    ]

    titulo = models.CharField(max_length = 200)
    descricao = models.TextField()
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='tarefas'
    )
    concluida = models.BooleanField(default = False)
    prioridade = models.CharField(
        max_length = 10, 
        choices = PRIORIDADE, 
        default = 'B'
    )
    data_criacao = models.DateTimeField(auto_now_add = True)
    data_conclusao = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return f"{self.titulo} ({'Concluída' if self.concluida else 'Pendente'})"
