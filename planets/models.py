from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField(null=True, blank=True)
    terrains = models.CharField(max_length=200)
    climates = models.CharField(max_length=200)

    def __str__(self):
        return self.name