from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from upload import models
from .filters import *
import math
#from lazypage.decorators import lazypage_decorator
# Create your views here.
#@lazypage_decorator 
number = None

@login_required(login_url='/login')
def upload(request):
  
    if request.method == 'POST':
        form = Upload_Image_Form(request.POST, request.FILES)
  
        if form.is_valid() and 'gopred' in request.POST:
            form.save()
            return redirect('/predict/')
        if form.is_valid() and 'gocheck' in request.POST:
            form.save()
            return redirect('/')
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
    image = Upload_Image.objects.get(id=number)
    posts = models.NewsUnit.objects.filter(photoid=number).delete()
    #print(image.id)
    # 驗證登入使用者、待刪除使用者是否相同
    #退出登入，刪除資料並返回部落格列表
    image.delete()
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


