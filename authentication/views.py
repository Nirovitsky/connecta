from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        if all(not form.cleaned_data[field] for field in form.fields):
            form.add_error(None, "Fields cannot be empty.")
            return self.form_invalid(form)

        # Rest of your existing code
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        if User.objects.filter(username=username).exists():
            form.add_error('username', 'This username is already taken.')

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
            return redirect("tasks")

        return super().dispatch(request, *args, **kwargs)
