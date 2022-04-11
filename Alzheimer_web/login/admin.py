from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'tel','message')  # 顯示欄位

admin.site.register(Customer, CustomerAdmin)