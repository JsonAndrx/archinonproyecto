from datetime import datetime, timedelta
from celery import shared_task
from .models import Video

@shared_task(blind=True)
def delete_video():
    limite = datetime.now() - timedelta(seconds=300)
    files = Video.objects.filter(fecha_subida__lte=limite)
    if files:
        files.delete()
        return "Videos expirados eliminados"
    return "no hay videos expirados" 