from django.db import models

# Create your models here.
class Geolocalizacao(models.Model):
    
    geo_lon = models.FloatField()
    geo_lat = models.FloatField()


    def __unicode__(self):
        return str(self.geo_lon)+","+str(self.geo_lat)

    def __str__(self):
        return str(self.geo_lon)+","+str(self.geo_lat)