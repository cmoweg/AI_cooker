from django.contrib import admin
from django.urls import include, path

import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
]
