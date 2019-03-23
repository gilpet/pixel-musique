from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from .image_to_music import get_image_data, pixels_to_midi
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import Image
from .forms import ImageForm

@csrf_exempt
def SaveImage(request):
    form = ImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
       image = Image()
       image.name = form.cleaned_data["name"]
       image.picture = form.cleaned_data["picture"]
       image.save()
       saved = True
       pix = get_image_data(image.picture)
       pixels_to_midi(pix,image.name)
       return render(request, 'pixel/saved.html', locals())
    else:
       return render_to_response('pixel/profile.html',{'form': form})
