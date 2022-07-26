from django.shortcuts import redirect, render, get_object_or_404
from . import models
from .forms import UploadFileForm

# Create your views here.

def HomeFile(request):
    return render(request, "core/home.html")

def error_404(request, exception):
    return render(request, 'core/404.html')

def subirArchivo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            id = form.instance.pk
            return redirect('archilinks', id)
    else:
        form = UploadFileForm()

    archivos =  models.Archivo.objects.all()
    
    return render(request, 'core/archivo.html',{'form':form, 'archivo':archivos})


def archilinks(request, id):
    archivo = get_object_or_404(models.Archivo, id=id)
    descarga = models.Archivo.objects.filter(id=id)
    
    data = {"formu": UploadFileForm(instance=archivo), "descargas":descarga}
    return render(request, 'core/linkarchivos.html', data)
