from django.urls import path
from .views import UserProfileView, UserProfileEditView, follow_toggle, FollowersListView, FollowingListView

urlpatterns = [
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile_view'),
    path('profile_edit/<str:username>/', UserProfileEditView.as_view(), name='profile_edit'),
    path('follow_toggle/<str:username>/', follow_toggle, name='follow_toggle'),
    path('<str:username>/followers/', FollowersListView.as_view(), name='follower_list'),
    path('<str:username>/following/', FollowingListView.as_view(), name='following_list'),
]
