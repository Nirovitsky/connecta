from django.urls import path, include

urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('comments/', include('comments.urls')),
    path('posts/', include('posts.urls')),
    path('userprofile/', include('userprofile.urls')),
]