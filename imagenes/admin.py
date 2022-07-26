from django.contrib import admin
from .models import Imagenes

# Register your models here.

class ImagenesAdmin(admin.ModelAdmin):
    list_display = ("image", "fecha_subida")

admin.site.register(Imagenes, ImagenesAdmin)