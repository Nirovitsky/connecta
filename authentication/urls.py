from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import RegisterPage, CustomLoginView, CustomLogoutView, BaseView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('base/', login_required(BaseView.as_view()), name='base'),
]
