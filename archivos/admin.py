from django.contrib import admin
from .models import Archivo
# Register your models here.

class ArchivoAdmin(admin.ModelAdmin):
    list_display = ("file", "fecha_subida")

admin.site.register(Archivo, ArchivoAdmin)
