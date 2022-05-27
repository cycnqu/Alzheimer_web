from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from login.form import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
# Create your views here.
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        username = request.POST.get('email',None)
        if form.is_valid():
            form.save()
            print(username)
            # 電子郵件內容樣板
            email_template = render_to_string(
                '../templates/signup_success_email.html',
                {'username': request.user.username}
            )
            email = EmailMessage(
                '註冊成功通知信',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                [''+username]  # 收件者
            )
            email.fail_silently = False
            email.send()

            return redirect('/login')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

#登入
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
        else:
            messages.error(request,'username or password not correct')
            return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

# 登出
def log_out(request):
    logout(request)
    return redirect('/login') #重新導向到登入畫面

def user_delete(request, id):
    user = User.objects.get(id=id)
    print(user)
    # 驗證登入使用者、待刪除使用者是否相同
    if request.user == user:
        #退出登入，刪除資料並返回部落格列表
        logout(request)
        user.delete()
        return redirect('/login')