from django import forms
from . models import *

class Userregistrationform(forms.ModelForm):
    class Meta:
        model=Userregistration
        fields=['username','password','email','contact_no']

                   
class UserloginForm(forms.ModelForm):
    class Meta:
        model=Userregistration
        fields=['username','password']        

class Vendorregistrationform(forms.ModelForm):
    class Meta:
        model=Vendorregistration
        fields=['username','password','email','contact_no']

class Vendorloginform(forms.ModelForm):
    class Meta:
        model=Vendorlogin
        fields=['username','password']         

class Packagesform(forms.ModelForm)    :
    class Meta:
        model=Packages 
        fields=['destination','price','duration','details','image'] 

class Bookingform(forms.ModelForm):
    tour_dates=forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'type':'date'
            }
    ))
    class Meta:
        model=Booking
        fields=['num_people','tour_dates']    
        
