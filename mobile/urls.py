from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materia/<str:cod>', views.materia, name='materia'),
    path('actualizar', views.actualizar, name='actualizar')
]