from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.conf import settings

from .models import CustomUser
from .forms import UserRegisterForm

class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка приветственного письма
        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию в нашем магазине!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data['email']],
            fail_silently=True,
        )
        return response
