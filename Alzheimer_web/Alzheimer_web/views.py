from django.shortcuts import redirect, render
#from django.http import HttpResponse
from upload.forms import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from Alzheimer_web.form import *
# start django 
def home(request):
    # check user's ip who visit our home page
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    ip = request.META['REMOTE_ADDR']
    print(user)
    print(user_agent)
    print(ip)
    form = ContactForms()
    if request.method == "POST":
        form = ContactForms(request.POST)
        username = request.POST.get('username',None)
        email1 = request.POST.get('email',None)
        phone = request.POST.get('phone',None)
        message = request.POST.get('message',None)
        if form.is_valid():
            # 電子郵件內容樣板
            email_template = render_to_string(
                '../templates/contactform_success_email.html',
                {
                    'username':username,
                    'email':email1,
                    'phone':phone,
                    'message':message
                }
            )
            email = EmailMessage(
                '表單回傳',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                [settings.EMAIL_HOST_USER]  # 收件者
            )
            email.fail_silently = False
            email.send()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'index.html',context)