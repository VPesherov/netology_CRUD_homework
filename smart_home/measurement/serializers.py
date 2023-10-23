from rest_framework import serializers
from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы

class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id_sensor', 'temperature', 'date']


