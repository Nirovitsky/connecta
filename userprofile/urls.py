from django.urls import path
from .views import UserProfileView, UserProfileEditView

urlpatterns = [
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile_view'),
    path('profile_edit/<str:username>/', UserProfileEditView.as_view(), name='profile_edit'),
]
