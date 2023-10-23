import datetime

from django.db import models
from django.utils import timezone


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} {self.description}'


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.id_sensor} {self.temperature} {self.date}'
