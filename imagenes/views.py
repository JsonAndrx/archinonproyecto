from django.shortcuts import redirect, render, get_object_or_404
from . import models
from .forms import UploadImageForm
# Create your views here.

def SubirImage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            id = form.instance.pk
            return redirect("imagenlinks", id)
    else:
        form = UploadImageForm()

    imagenes = models.Imagenes.objects.all()

    return render (request, "imagenes/imagenes.html", {'form':form, 'imagenes':imagenes})


def imagelinks(request, id):
    imagen = get_object_or_404(models.Imagenes, id=id)
    descarga = models.Imagenes.objects.filter(id=id)

    data = {"formu":UploadImageForm(instance=imagen), 'descargas':descarga}
    return render(request, 'imagenes/linkimagenes.html', data)
