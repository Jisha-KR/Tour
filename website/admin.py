from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Userregistration)
class UserregistrationAdmin(admin.ModelAdmin):
    list_display=('username','password','email','contact_no')
    list_filter=('username','password','email','contact_no')
    search_fields=('username','password','email','contact_no')

@admin.register(Vendorregistration)    
class VendorregistrationAdmin(admin.ModelAdmin):
    list_display=('id','username','password','email','contact_no')
    list_filter=('id','username','password','email','contact_no')
    search_fields=('id','username','password','email','contact_no')

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display=('id','destination','price','duration','details','image','approved')
    list_filter=('id','destination','price','duration','details','image','approved') 
    search_fields=('id','destination','price','duration','details','image','approved')


    