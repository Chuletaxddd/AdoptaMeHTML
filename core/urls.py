from django.urls import path
from .views import ong

urlpatterns = [
    path('', ong,name="ong"),
]