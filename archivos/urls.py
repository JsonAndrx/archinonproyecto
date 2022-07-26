from django.urls import path, re_path
from archivos import views

urlpatterns = [
    path('', views.HomeFile, name="home"),
    path('download/<id>/', views.archilinks, name="archilinks"),
    path('archivos/', views.subirArchivo, name="archivos")
]