from django.contrib import admin
from upload.models import *
# Register your models here.
class Upload_Image_Admin(admin.ModelAdmin):
    list_display = ('id','date','img_preview','tag','predict_tag')
    list_filter = ('id','date','tag','predict_tag')
    search_fields = ('date','tag','predict_tag')
    ordering = ('id',)
    #readonly_fields = ('img_preview',)

    def img_preview(self,obj):
        return obj.img_preview
    
    img_preview.short_description = 'img preview'
    img_preview.allow_tags = True

admin.site.register(Upload_Image,Upload_Image_Admin)