from django import forms
from .models import Archivo

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ("file",)