from django.db import models

# Create your models here.
class GrupoPet(models.Model):
    
    nome = models.CharField(max_length=20, null=True, blank=True)
    area_do_conhecimento = models.CharField(max_length=20, null=True, blank=True)
    interdisciplinar = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome