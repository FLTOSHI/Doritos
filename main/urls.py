from django.urls import path
from . import views
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contacts, name='contacts'),
]