from django.urls import path
from imagenes import views

urlpatterns = [
    path('downloadi/<id>/', views.imagelinks, name="imagenlinks"),
    path('imagenes/', views.SubirImage, name="imagenes")
]