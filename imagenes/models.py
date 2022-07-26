from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
# Create your models here.

class Imagenes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.FileField(verbose_name='Imagenes' ,upload_to='imagenes', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    fecha_subida = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Imagenes"