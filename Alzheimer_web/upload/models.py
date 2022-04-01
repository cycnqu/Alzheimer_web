from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
# Create your models here.
class Upload_Image(models.Model):
    image = models.ImageField(upload_to='images/',blank =False , null =False)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name

    @property
    def img_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="200" height="200" />'.format(self.image.url))
        return ""