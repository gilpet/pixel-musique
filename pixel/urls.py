from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import save_image, play_song, stop_song

app_name = "pixel"

urlpatterns = [
   url(r'^image/',TemplateView.as_view(template_name = 'pixel/profile.html'),name='image'),
   url(r'^saved/',save_image, name='saved'),
   url(r'^play/',play_song, name='play'),
   url(r'^stop/',stop_song, name='stop')
]
