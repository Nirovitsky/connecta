from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
