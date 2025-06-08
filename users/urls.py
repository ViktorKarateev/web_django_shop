from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, update_profile_view

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/edit/', update_profile_view, name='profile_edit'),
]
