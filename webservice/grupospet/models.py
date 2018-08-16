from django.db import models
from projetos.models import Projeto
# Create your models here.



class GrupoPet(models.Model):
    
    nome = models.CharField(max_length=20, null=True, blank=True)
    area_do_conhecimento = models.CharField(max_length=20, null=True, blank=True)
    interdisciplinar = models.BooleanField(default=True)
    projetos = models.ManyToManyField('projetos.Projeto', null=True, blank=True, related_name='grupos_pet')

    geolocalizacao = models.ForeignKey('geolocalizacoes.Geolocalizacao', on_delete=None, default=None, related_name='grupospet')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome