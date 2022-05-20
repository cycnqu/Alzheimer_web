from django.shortcuts import render
from django.http import HttpResponse
from upload.forms import *
# start django 
def home(request):
    # check user's ip who visit our home page
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    ip = request.META['REMOTE_ADDR']
    print(user)
    print(user_agent)
    print(ip)
    return render(request, 'index.html')
