from django import forms
from .models import Imagenes

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        fields = ("image",)