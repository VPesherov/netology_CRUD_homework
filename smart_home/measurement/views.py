from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializers, MeasureSerializers


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# @api_view(['GET'])
# def get_sensors_list(request):
#     sensors = Sensor.objects.all()  # Достанем все оружия из нашей модели
#     ser = SensorSerializers(sensors, many=True)
#     return Response(ser.data)  # специальный класс который возвращает словарь

class SensorView(APIView):
    def get(self, request, pk):
        sensors = Sensor.objects.get(pk=pk)
        measurement = Measurement.objects.filter(id_sensor=pk)
        ser_measure = MeasureSerializers(measurement, many=True)
        # print(sensors.id)
        result_data = {
            "id": sensors.id,
            "name": sensors.name,
            "description": sensors.description,
            "measurements": ser_measure.data
        }
        return Response(result_data)  # специальный класс который возвращает словарь

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorSerializers(sensor, data=request.data,
                                       partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class MeasureView(APIView):
    def post(self, request):

        measure = MeasureSerializers(data=request.data)
        # print(measure)
        if measure.is_valid():
            measure.save()
            return Response(measure.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SensorsView(APIView):

    def post(self, request):

        sensor = SensorSerializers(data=request.data)

        if sensor.is_valid():
            sensor.save()
            return Response(sensor.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializers(sensors, many=True)
        return Response(ser.data)  # специальный класс который возвращает словарь
