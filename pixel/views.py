import time
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from .image_to_music import get_image_data, pixels_to_midi
from .midi_player import load_file, play, stop
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import Image, Metrics
from .forms import ImageForm


@csrf_exempt
def stats(request):
    metrics = Metrics.objects.all()
    average_pixels = sum([x.pixels for x in metrics])/len(metrics)
    average_time = sum([x.processing_time for x in metrics])/len(metrics)
    return render_to_response('pixel/profile.html', {'saved': True,
                              'average_pixels': average_pixels,
                              'average_time': average_time})

@csrf_exempt
def play_song(request):
    play()
    return render_to_response('pixel/profile.html', {'saved':True})


@csrf_exempt
def stop_song(request):
    stop()
    return render_to_response('pixel/profile.html', {'saved':True})


@csrf_exempt
def save_image(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
       start = time.time()
       image = Image()
       image.name = form.cleaned_data["name"]
       image.picture = form.cleaned_data["picture"]
       image.save()
       saved = True
       midi_file_name = image.name[:10]+".mid"
       pixels = get_image_data(image.picture)
       num_pixels = pixels_to_midi(pixels, midi_file_name)
       load_file(midi_file_name)
       metrics = Metrics(processing_time=time.time() - start,
                         pixels=num_pixels)
       metrics.save()
       return render_to_response('pixel/profile.html', {'saved':True,
                                 'song':True,'image':{'name':image.name}})
    else:
       return render_to_response('pixel/profile.html',{'form': form})
