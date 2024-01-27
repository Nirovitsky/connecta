from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile/profile_view.html'
    context_object_name = 'user_profile'

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        user_profile = get_object_or_404(UserProfile, user__username=username)
        return user_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user
        context['following'] = self.object.followers.all()
        return context


class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile/profile_edit.html'

    def get_object(self, queryset=None):
        obj, created = UserProfile.objects.get_or_create(user=self.request.user)
        return obj

    def form_valid(self, form):
        user = self.request.user
        new_username = form.cleaned_data.get('username')
        if new_username and new_username != user.username:
            if User.objects.filter(username=new_username).exists():
                messages.error(self.request, 'Username is already taken. Please choose a different one.')
                return self.form_invalid(form)

            user.username = new_username
            user.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Profile updated successfully.')
        return response

    def get_success_url(self):
        return reverse('profile_view', kwargs={'username': self.request.user.username})


@login_required
def follow_toggle(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)

    if request.user in user_profile.followers.all():
        user_profile.followers.remove(request.user)
        is_following = False
    else:
        user_profile.followers.add(request.user)
        is_following = True

    user_profile.save()

    return redirect('profile_view', username=username)


class FollowersListView(ListView):
    model = UserProfile
    template_name = 'followers_list.html'
    context_object_name = 'followers'

    def get_queryset(self):
        username = self.kwargs.get("username")
        user_profile = UserProfile.objects.get(user__username=username)
        return user_profile.followers.all()


class FollowingListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'following_list.html'
    context_object_name = 'following'

    def get_queryset(self):
        username = self.kwargs.get("username")
        user_profile = UserProfile.objects.get(user__username=username)
        return user_profile.followings.all()
