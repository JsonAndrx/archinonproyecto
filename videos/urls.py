from django.urls import path
from videos import views

urlpatterns = [
    path('downloadv/<id>/', views.videoslink, name="subirvideo"),
    path('videos/', views.SubirVide, name="videos"),
]