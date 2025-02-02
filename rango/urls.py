from django.urls import path
from rango import views

app_name ='rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('test_media/', views.test_media, name='test_media'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
]
