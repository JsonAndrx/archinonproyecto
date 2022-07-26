import uuid
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.

class Archivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='archivos', validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx", "xls", "xls", "txt", "rar", "pptx"])], verbose_name="Archivo")
    fecha_subida = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Archivos'