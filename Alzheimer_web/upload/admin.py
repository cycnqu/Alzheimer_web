from django.contrib import admin
from upload.models import *
from upload import models
# Register your models here.
class Upload_Image_Admin(admin.ModelAdmin):
    list_display = ('id','date','img_preview','tag')
    list_filter = ('id','date','tag')
    search_fields = ('date','tag')
    ordering = ('id',)
    #readonly_fields = ('img_preview',)

    def img_preview(self,obj):
        return obj.img_preview
    
    img_preview.short_description = 'img preview'
    img_preview.allow_tags = True

admin.site.register(Upload_Image,Upload_Image_Admin)
admin.site.register(models.NewsUnit)
