from django.shortcuts import render,redirect
from django.http import HttpResponse
from upload.forms import *
from login.form import *

# start django 
def home(request):
    form = CustomerModelForm()
    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customers')
    context = {
        'form': form
    }
    return render(request, 'index.html')
