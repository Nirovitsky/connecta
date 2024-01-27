from django.urls import path
from .views import RegisterPage, CustomLoginView, CustomLogoutView, BaseView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('post_list/', BaseView.as_view(), name='post_list'),
]
