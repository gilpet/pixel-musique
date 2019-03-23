from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import SaveImage

app_name = "pixel"

urlpatterns = [
   url(r'^image/',TemplateView.as_view(template_name = 'pixel/profile.html'),name='image'),
   url(r'^saved/',SaveImage, name='saved')
]
