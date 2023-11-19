from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'profile/profile_view.html'
    context_object_name = 'user_profile'

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_queryset().get(username=self.kwargs.get("username"))
            return render(
                request, self.template_name, self.get_context_data(object=self.object)
            )
        except User.DoesNotExist as ex:
            raise Http404("User does not exist!") from ex

class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def form_valid(self, form):
        response = super().form_valid(form)
        # Assuming you have a success message in your form_valid function
        messages.success(self.request, 'Profile updated successfully.')
        return response

    def get_success_url(self):
        # Redirect to the profile_view page with the updated user's information
        return reverse('profile_view', kwargs={'username': self.request.user.username})

