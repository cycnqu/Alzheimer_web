from django.shortcuts import render,redirect
from django.http import HttpResponse
from upload.forms import *
# start django 
def helloworld(request):
    return HttpResponse('hello Alzheimer web')
# upload_image

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
  
# Create your views here.
def upload(request):
  
    if request.method == 'POST':
        form = Upload_Image_Form(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('/upload/success/')
    else:
        form = Upload_Image_Form()
    return render(request, 'upload.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def list_all(request):
    images = Upload_Image.objects.all().order_by('id')
    context = {
        'images':images
    }
    return render(request,'listall.html',context)