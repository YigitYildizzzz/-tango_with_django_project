from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('test_media/', views.test_media, name='test_media'),
]
