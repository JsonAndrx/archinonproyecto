from datetime import datetime, timedelta
from celery import shared_task
from .models import Imagenes

@shared_task(blind=True)
def delete_image():
    limite = datetime.now() - timedelta(seconds=300)
    files = Imagenes.objects.filter(fecha_subida__lte=limite)
    if files:
        files.delete()
        return "imagenes eliminados"
    return "no hay imagenes expiradas" 