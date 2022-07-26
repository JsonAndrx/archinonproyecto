from datetime import datetime, timedelta
from celery import shared_task
from .models import Archivo

@shared_task(blind=True)
def delete_file():
    limite = datetime.now() - timedelta(seconds=300)
    files = Archivo.objects.filter(fecha_subida__lte=limite)
    if files:
        files.delete()
        return "archivos eliminados"
    return "no hay archivos expirados" 