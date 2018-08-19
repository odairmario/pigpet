from django.db import models

# Create your models here.
class Campi(models.Model):
    
    nome = models.CharField(max_length=20)
    geolocalizacao = models.ForeignKey('geolocalizacoes.Geolocalizacao', on_delete=None, default=None, related_name='campis')

    universidade = models.ForeignKey('universidades.Universidade', on_delete=models.CASCADE, default=None, related_name='campis')

    class Meta:
        unique_together = (("nome", "universidade"),)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome