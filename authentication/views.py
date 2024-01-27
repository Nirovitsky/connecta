from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.forms import CustomUserCreationForm
from userprofile.models import UserProfile


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
        if form.errors:
            return self.form_invalid(form)

        user = form.save()

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.save()

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
    next_page = reverse_lazy('login')