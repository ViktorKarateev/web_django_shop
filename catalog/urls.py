from django.urls import path
from . import views
from .apps import CatalogConfig  # добавляем имя приложения

app_name = CatalogConfig.name  # устанавливаем пространство имён

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product_view, name='add_product'),
]
