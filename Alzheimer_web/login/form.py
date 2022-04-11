from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from binascii import a2b_qp
from email.policy import default
from .models import Customer
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        }
        labels = {
            'name': '姓名',
            'email': '電子郵件',
            'tel': '聯絡電話',
            'message':'訊息'
        }

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email') #取得樣板所填寫的資料
        if email.endswith('@hotmail.com'):
            raise forms.ValidationError('不得使用Hotmail電子郵件')
        return email