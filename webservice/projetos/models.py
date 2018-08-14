from django.db import models

# Create your models here.
class Projeto(models.Model):
    
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50, default="")
    texto = models.CharField(max_length=5000, default="")
    ativo = models.BooleanField(default=True)
    membros = models.ManyToManyField('userprofile.UserProfile')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome