# accounts/views.py
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
