from django.urls import path
from . import views

urlpatterns = [
    path('', views.todayFood, name='todayFood'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]
