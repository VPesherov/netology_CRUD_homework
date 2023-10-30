from django.urls import path
from .views import SensorView, MeasureView, SensorsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', MeasureView.as_view()),

]
