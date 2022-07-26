from email.mime import image
from operator import ge
from django.shortcuts import redirect, render, get_object_or_404
from . import models
from .forms import UploadVideoForm

# Create your views here.

def SubirVide(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            id = form.instance.pk
            return redirect("subirvideo", id)
    else:
        form = UploadVideoForm()

    video = models.Video.objects.all()

    return render(request, "videos/videos.html", {'form':form, 'videos':video})


def videoslink(request, id):
    video = get_object_or_404(models.Video, id=id)
    descarga = models.Video.objects.filter(id=id)

    data = {"formu":UploadVideoForm(instance=video), 'descargas':descarga}
    return render(request, 'videos/linkvideos.html', data)
