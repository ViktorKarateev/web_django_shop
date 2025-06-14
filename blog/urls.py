from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView
)

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('<int:pk>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
]

