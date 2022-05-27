from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from binascii import a2b_qp
from email.policy import default


class ContactForms(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'})
    )
    phone = forms.CharField(
        label="電話",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'})
    )
    message = forms.CharField(
        label="訊息",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'})
    )
