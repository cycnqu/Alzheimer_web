from .models import Upload_Image
import django_filters
 
 
class Upload_ImageFilter(django_filters.FilterSet):
 
    class Meta:
        model = Upload_Image
        fields = ['id','date','tag']