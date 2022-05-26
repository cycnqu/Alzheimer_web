from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
# Create your models here.
class Upload_Image(models.Model):
    Alzheimer_tag = [('MildDmented','MildDmented'),('ModerateDemented','ModerateDmented'),('NonDemented','NonDemented'),('VeryMildDemented','VeryMildDemented'),('Unknow','Unknow')]
    image = models.ImageField(upload_to='images/',blank =False , null =False)
    date = models.DateField(default=timezone.now)
    tag = models.CharField(max_length=100,default='NonDmented',null = False,choices = Alzheimer_tag)
    @property
    def img_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="200" height="200" />'.format(self.image.url))
        return ""


class NewsUnit(models.Model):
    photoid = models.CharField(max_length=10, null=False)
    nickname = models.CharField(max_length=20, null=False)
    message = models.TextField(null=False)
    pubtime = models.DateTimeField(auto_now=True)
    press = models.IntegerField(default=0)

    def __str__(self):
        return  self.photoid