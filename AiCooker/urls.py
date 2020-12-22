from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

# app_name = "AiCooker"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('today/', include('ImageUpload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
