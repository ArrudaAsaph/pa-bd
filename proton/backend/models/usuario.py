from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username