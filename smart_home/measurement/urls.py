from django.urls import path
from .views import SensorView, MeasureView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', MeasureView.as_view()),

]
