from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

@api_view(['GET'])
def demo1(request):
    sensors = Sensor.objects.all()  # Достанем все оружия из нашей модели
    data = {'message': 'Hello'}
    return Response(data)  # специальный класс который возвращает словарь
