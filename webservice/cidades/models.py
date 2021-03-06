from django.db import models

# Create your models here.
class Cidade(models.Model):
    
    nome = models.CharField(max_length=20)

    estado = models.ForeignKey('estados.Estado', on_delete=models.CASCADE, default=None, related_name='cidades')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome