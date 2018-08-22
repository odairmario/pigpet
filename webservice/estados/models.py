from django.db import models

# Create your models here.
class Estado(models.Model):
    
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=20)
    regiao = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome