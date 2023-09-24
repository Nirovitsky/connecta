from os import path

from authentication import admin
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]