from django.urls import path
from . import views

app_name = "ImageUpload"

urlpatterns = [
    path('', views.todayFood, name='todayFood'),
    path('uploadForm/', views.uploadForm, name='uploadForm'),
    path('upload/', views.upload, name='upload'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
]
