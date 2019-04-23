from django import forms
from pixel.image_to_music import file_size

class ImageForm(forms.Form):
   name = forms.CharField(max_length=255, required=False)
   picture = forms.ImageField(validators=[file_size])
