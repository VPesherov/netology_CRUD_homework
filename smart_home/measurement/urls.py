from django.urls import path
from .views import demo1

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('', demo1)
]
