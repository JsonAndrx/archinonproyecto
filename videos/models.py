from datetime import datetime
from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid

# Create your models here.

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='videos', validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Video')
    fecha_subida = models.DateTimeField(default=timezone.now)