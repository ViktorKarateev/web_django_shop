from django.urls import path
from . import views
from .apps import CatalogConfig  # добавляем имя приложения

app_name = CatalogConfig.name  # устанавливаем пространство имён

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
