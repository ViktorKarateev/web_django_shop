from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, update_product_view ,delete_product_view

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/update/', update_product_view, name='product_update'),
    path('product/<int:pk>/delete/', delete_product_view, name='product_delete'),

]
