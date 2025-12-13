from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPOS_USUARIO = [
        ('diretoria', 'Diretoria'),
        ('associado', 'Associado'),
        ('afiliado', 'Afiliado'),
    ]

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPOS_USUARIO,
        default='afiliado'
    )

    telefone = models.CharField(max_length=20, blank=True, null=True)

