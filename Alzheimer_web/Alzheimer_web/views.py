from django.shortcuts import render,redirect
from django.http import HttpResponse
from upload.forms import *
from login.form import *

# start django 
def home(request):
    return render(request, 'index.html')
