"""Alzheimer_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from distutils.command.upload import upload
from django.contrib import admin
from django.urls import path,include
from upload.views import *
from django.conf import settings
from django.conf.urls.static import static
from predict.views import *
from Alzheimer_web.views import home
from login.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # home page
    path('',home),
    # upload page
    path('upload/',upload),
    #path('upload/success/',success),
    path('listall/',list_all),
    # predict page
    path('predict/',prediction),
    # login page
    path('accounts/', include('allauth.urls')),
    path('register/',sign_up,name='Register'),
    path('login/',sign_in,name='Login'),
    #path('sign_in/',sign_in),
    path('logout/', log_out, name='Logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
