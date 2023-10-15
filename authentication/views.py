from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('base')

class RegisterPage(FormView):
    template_name = 'authentication/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        if User.objects.filter(username=username).exists():
            form.add_error('username', 'This username is already taken.')

        if User.objects.filter(email=email).exists():
            form.add_error('email', 'This email is already registered.')

        if len(password1) < 8:
            form.add_error('password1', 'This password is too short. It must contain at least 8 characters.')
        if password1 != password2:
            form.add_error('password1', 'Passwords do not match.')
            form.add_error('password2', 'Passwords do not match.')

        if form.errors:
            return self.form_invalid(form)

        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("base")

        return super().dispatch(request, *args, **kwargs)


class BaseView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponse("You are not logged in. Redirect to login page.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('register')