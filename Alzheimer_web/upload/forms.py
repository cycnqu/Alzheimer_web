from binascii import a2b_qp
from datetime import datetime
from email.policy import default
import django


from django import forms
from upload.models import * 
from django.utils import timezone
class Upload_Image_Form(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = ['image','date']
