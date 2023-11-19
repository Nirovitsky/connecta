from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
