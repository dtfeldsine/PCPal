from django.urls import path
from . import views
from .putshitindb import initDB

urlpatterns = [
    path('', views.cpu_index, name = 'cpu_index'),
]

initDB()

