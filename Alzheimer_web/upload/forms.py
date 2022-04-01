from django import forms
from upload.models import * 
from django.contrib.admin.decorators import display
from django.template.loader import get_template

class Upload_Image_Form(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = ['image','date']
        