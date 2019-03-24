from django import forms

class ImageForm(forms.Form):
   name = forms.CharField(max_length=255,required=False)
   picture = forms.ImageField()
