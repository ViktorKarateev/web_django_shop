from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import UserRegisterForm, ProfileForm


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию в нашем магазине!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data['email']],
            fail_silently=True,
        )
        return response


@login_required
def update_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'users/profile_edit.html', {'form': form})
