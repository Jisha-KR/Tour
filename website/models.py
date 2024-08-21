from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Userregistration(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact_no=models.IntegerField()
    
    def __str__(self):
        return self.username


class Vendorregistration(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Increased length for hashed passwords
    email = models.EmailField(max_length=100)
    contact_no = models.IntegerField()

    def __str__(self):
        return self.username

class Vendorlogin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Increased length for hashed passwords

    def __str__(self):
        return self.username
    
class Packages(models.Model):
    destination=models.CharField(max_length=100)
    price=models.IntegerField()
    duration=models.IntegerField()
    details=models.TextField(max_length=500)
    image=models.ImageField(upload_to='images/')
    approved=models.BooleanField('Approved',default=False)
    vendor=models.CharField(max_length=100,default=False)

    def __str__(self):
        return self.destination
    


class Booking(models.Model):
    num_people=models.IntegerField()    
    tour_dates=models.DateField(null=True,blank=True)
