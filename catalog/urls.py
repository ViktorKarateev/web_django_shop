from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, ProductUpdateView,ProductDeleteView,ProductCreateView,UnpublishProductView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='product_unpublish')
]
