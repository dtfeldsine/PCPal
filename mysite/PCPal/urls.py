from django.urls import path
from . import views
from .putshitindb import initDB
# Looks for urlpatterns and stops when it finds a match.
# Calls the respective view. 
urlpatterns = [
    path('', views.cpu_index, name = 'cpu_index'),
]

initDB()

