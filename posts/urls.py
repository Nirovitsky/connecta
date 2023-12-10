from django.urls import path
from . import views
from .views import toggle_like

app_name = 'posts'

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('toggle_like/<int:post_id>/', toggle_like, name='toggle_like'),
]
