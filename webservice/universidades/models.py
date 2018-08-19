from django.db import models

# Create your models here.
class Universidade(models.Model):
    
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=10)

    def __unicode__(self):
        return self.sigla

    def __str__(self):
        return self.sigla