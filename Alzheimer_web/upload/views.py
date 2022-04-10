from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def upload(request):
  
    if request.method == 'POST':
        form = Upload_Image_Form(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('/predict/')
    else:
        form = Upload_Image_Form()
    return render(request, 'upload.html', {'form' : form})
  
  
#def success(request):
#    return HttpResponse('successfully uploaded')
@login_required(login_url='/login')
def list_all(request):
    images = Upload_Image.objects.all().order_by('id')
    context = {
        'images':images
    }
    return render(request,'listall.html',context)