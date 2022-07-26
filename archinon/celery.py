import os
from datetime import timedelta
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archinon.settings')

app = Celery('archinon')


BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_BROKER_URL = os.environ.get('REDIS_URL')
app.conf.broker_url = BASE_REDIS_URL


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'America/Bogota'

app.conf.beat_schedule = {
    'eliminando-archivos':{
        'task':'archivos.tasks.delete_file',
        'schedule':timedelta(seconds=30),
    },
    'eliminando-image':{
        'task':'imagenes.tasks.delete_image',
        'schedule':timedelta(seconds=30),
    },
    'eliminando-video':{
        'task':'videos.tasks.delete_video',
        'schedule':timedelta(seconds=30),
    }
}

app.autodiscover_tasks()