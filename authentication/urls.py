from django.urls import path
from . import views
from .views import RegisterPage, CustomLoginView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('base/', views.BaseView.as_view, name='base'),
]
