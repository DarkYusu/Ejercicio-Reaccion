from django.db import models
from django.contrib.auth.models import User

class Prueba(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    letra_1 = models.CharField(max_length=1)
    tiempo_1 = models.FloatField()
    letra_2 = models.CharField(max_length=1)
    tiempo_2 = models.FloatField()
    letra_3 = models.CharField(max_length=1)
    tiempo_3 = models.FloatField()
    letra_4 = models.CharField(max_length=1)
    tiempo_4 = models.FloatField()
    letra_5 = models.CharField(max_length=1)
    tiempo_5 = models.FloatField()

    def tiempo_total(self):
        return self.tiempo_1 + self.tiempo_2 + self.tiempo_3 + self.tiempo_4 + self.tiempo_5
