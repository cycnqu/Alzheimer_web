from django import forms
from upload.models import * 
class Upload_Image_Form(forms.ModelForm):
    Alzheimer_tag = [('MildDmented','MildDmented'),('ModerateDemented','ModerateDmented'),('NonDemented','NonDemented'),('VeryMildDemented','VeryMildDemented'),('Unknow','Unknow')]
    tag = forms.ChoiceField(choices=Alzheimer_tag,widget=forms.RadioSelect)
    class Meta:
        model = Upload_Image
        fields = ['image','date','tag']
        #widgets = {
        #    'image':forms.FileInput(attrs={'class':'imagecontrol'})
        #}
    