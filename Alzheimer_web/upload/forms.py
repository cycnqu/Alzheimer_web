from django import forms
from upload.models import * 
class Upload_Image_Form(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = ['image','date']
        #widgets = {
        #    'image':forms.FileInput(attrs={'class':'imagecontrol'})
        #}