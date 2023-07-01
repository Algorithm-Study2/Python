from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
]