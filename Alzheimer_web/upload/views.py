from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import number
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from upload import models
from .filters import *
from django.contrib.auth.models import User #User模組
import math

# Create your views here.
number = None
@login_required(login_url='/login')
def upload(request,username=None):
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
    images = Upload_Image.objects.all()
    imageFilter = Upload_ImageFilter(queryset=images)
    if request.method == "POST":
        imageFilter = Upload_ImageFilter(request.POST, queryset=images)
    context = {
        'imageFilter':imageFilter
    }
    return render(request,'listall.html',context)

@login_required(login_url='/login')
def image_delete(request, number=None):
    imagee = Upload_Image.objects.get(id=number)
    posts = models.NewsUnit.objects.filter(photoid=number).delete()
    #print(image.id)
    # 驗證登入使用者、待刪除使用者是否相同
    #退出登入，刪除資料並返回部落格列表
    imagee.delete()
    return redirect('/listall')


    
@login_required(login_url='/login')
def comment(request, photo=None):
    global number 
    number = photo
    img = models.Upload_Image.objects.get(id=number)
    posts = NewsUnit.objects.filter(photoid=photo)
    context = {
        'img':img,
        'posts':posts
    }

    message = ''
    photoid = number
    editor = request.POST.get('news_editor', '')
    content = request.POST.get('news_content', '')
    if content == '':
        message = '每個欄位都要填寫!'
    else:    
        unit = models.NewsUnit.objects.create(photoid=photoid, nickname=editor, message=content, press=0)
        unit.save()
        return  redirect('/photocomment/'+str(number))

    return render(request, "photocomment.html",context)

@login_required(login_url='/login')
def detail(request, detailid=None):
    unit = models.NewsUnit.objects.get(id=detailid)
    photoid = unit.photoid
    pubtime = unit.pubtime
    nickname = unit.nickname
    message = unit.message
    unit.press += 1
    unit.save()
    return render(request, "detail.html", locals())

#def newsadd(request,detailid=22):
    #global number
    #message = ''
    #photoid = number
    #subject = request.POST.get('news_subject', '')
    #editor = request.POST.get('news_editor', '')
    #content = request.POST.get('news_content', '')
    #ok = request.POST.get('news_ok', '')
    #if subject == '' or editor == '' or content == '':
     #   message = '每個欄位都要填寫!'
    #else:
     #   if ok == 'yes':
      #      enabled = True
       # else:
        #    enabled = False
        #unit = models.NewsUnit.objects.create(photoid=photoid, nickname=editor, title=subject, message=content,enabled=enabled, press=0)
        #unit.save()
        #return  redirect('/photocomment/'+str(number))
    #return render(request, "addpost.html", locals())