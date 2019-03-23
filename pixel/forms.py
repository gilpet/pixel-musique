from django import forms

class ImageForm(forms.Form):
   name = forms.CharField(max_length=255,required=False)
   picture = forms.ImageField()

   def __init__(self, *args, **kwargs):
       super(ImageForm, self).__init__(*args, **kwargs)
       self.fields['picture'].error_messages = {'required': 'Gotta upload an image!'}
