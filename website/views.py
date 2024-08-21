from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from .forms import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')


def userregistration(request):
    if request.method=='POST':
        form=Userregistrationform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            if Userregistration.objects.filter(username=username).exists():
                return redirect('userexist')
            else:
                form.save()
                return redirect('success')
    else:
        form=Userregistrationform()
    return render(request,'userregistration.html',{'form':form})    


def usrlogn(request):
    form = UserloginForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            userr=Userregistration.objects.filter(username=username).exists()
            if userr:
                user=Userregistration.objects.get(username=username)
                if user:
                    if user.password == password:
                        return redirect('user_dis')   
                    else:
                        return redirect('invalidpass')
            else:    
                return redirect('invaliduser')
    else:
        form=UserloginForm()
    return render(request,'userlogin.html',{'form':form})            



def vendorregistration(request):
    if request.method == 'POST':
        form = Vendorregistrationform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if Vendorregistration.objects.filter(username=username).exists():
                return redirect('userexistv')
            else:
                form.save() 
                return redirect('vendorlogin')
    else:
        form = Vendorregistrationform()
    return render(request, 'vendorregistration.html', {'form': form})  
        

def vendorlogin(request):
    form = Vendorloginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = Vendorregistration.objects.get(username=username)
                if user.password==password:
                    request.session['username'] = username  # Store the username in session
                    return redirect('vendorhome')
                else:
                    return redirect('invalidpassv')
            except Vendorregistration.DoesNotExist:
                return redirect('invaliduserv')
    return render(request, 'vendorlogin.html', {'form': form}) 

def invalidpass(request):
    return render(request,"invalidpass.html")

def invaliduser(request):
        return render(request,"invaliduser.html")

def userexist(request):
    return render(request,"userexist.html")

def invalidpassv(request):
    return render(request,"invalidpassv.html")

def invaliduserv(request):
        return render(request,"invaliduserv.html")

def userexistv(request):
    return render(request,"userexistv.html")

def success(request):
    return render(request,"success.html")
   
def addpackages(request):
    if not request.session.get('username'):
        return redirect('vendorlogin')  # Redirect to login if not authenticated

    if request.method == 'POST':
        form = Packagesform(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.vendor = request.session['username']  # Use session to get the logged-in vendor
            package.save()
            return redirect('disply')
    else:
        form = Packagesform()
    return render(request, 'packages.html', {'form': form})


def disply(request):
    if not request.session.get('username'):
        return redirect('vendorlogin')  # Redirect to login if not authenticated

    username = request.session['username']
    items = Packages.objects.filter(vendor=username)
    return render(request, 'display.html', {'item': items, 'username': username})


def user_dis(request):    
    item=Packages.objects.all()
    return render(request,'user_dis.html',{'item':item})


def delt(request,pk):
    item=get_object_or_404(Packages,pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('disply')
    else:
        return render(request,'confirm.html',{'item':item})
    
def confirm(request):
    return render(request,'confirm.html')    

def editt(request,pk):
    item=get_object_or_404(Packages,pk=pk)
    if request.method=='POST':
        form=Packagesform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('disply')
    else:
        form=Packagesform(instance=item)
    return render(request,'edit.html',{'form':form})        


def userpackages(request):
    item=Packages.objects.all()
    return render(request,'userpackages.html',{'item':item})



def approvedpackages(request):
    if not request.session.get('username'):
        return redirect('vendorlogin')  # Redirect to login if not authenticated

    username = request.session['username']
    items = Packages.objects.filter(vendor=username)
    return render(request, 'approvedpackages.html', {'item': items, 'username': username})


def contact(request):
    return render(request,'contact.html')


def logoutt(request):
    request.session.flush() 
    return redirect('index')


def searchbar(request):
    if request.method=='GET':
        search=request.GET.get('search')
        post= Packages.objects.filter(Q(destination__icontains=search)|Q(price__icontains=search)|Q(duration__icontains=search))
        return render(request,'user_dis.html',{'post':post})
    
def home(request):
    return render(request,'home.html')    

def vendorhome(request):
    # Check if the user is authenticated
    if not request.session.get('username'):
        return redirect('vendorlogin')  # Redirect to login if not authenticated

    # Get the username from the session
    username = request.session['username']

    # Optionally, you can also fetch other information or packages here
    # packages = Packages.objects.filter(vendor=username)

    # Render the vendor home page
    return render(request, 'vendorhome.html', {'username': username})


'''
def package_details(request,pk):
    package = get_object_or_404(Packages, pk=pk)
    
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            # Handle form data (save to database, send email, etc.)
            num_people = form.cleaned_data['num_people']
            tour_dates= form.cleaned_data['tour_dates']           
            price_per_person = package.price  # Get the price from the package instance
            total_amount = num_people * price_per_person   
            form.save()
            return render(request,'package_details.html', {'total_amount':total_amount})               
    else:
        form = Bookingform()
    return render(request, 'package_details.html', {
        'package': package,
        'form': form,
        'price_per_person': package.price,
        #'total_amount':total_amount
    })
'''

def package_details(request, pk):
    package = get_object_or_404(Packages, pk=pk)
    
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            num_people = form.cleaned_data['num_people']
            tour_dates = form.cleaned_data['tour_dates']
            price_per_person = package.price
            total_amount = num_people * price_per_person
            
            # Save the booking
            booking = form.save(commit=False)
            booking.package = package
            booking.total_amount = total_amount
            booking.save()

            return render(request, 'package_details.html', {
                'package': package,
                'form': form,
                'total_amount': total_amount
            })
    else:
        form = Bookingform()
    
    return render(request, 'package_details.html', {
        'package': package,
        'form': form,
        'price_per_person': package.price,
    })

def book_package(request, pk):
    package = get_object_or_404(Packages, pk=pk)
    if request.method == 'POST':
        Booking.objects.create(package=package, user=request.user)
        return redirect('package_details', pk=pk)
    return render(request, 'book_package.html', {'package': package}) 


def user_dis_package(request):
    item=Packages.objects.all()
    return render(request,'user_dis_package.html',{'item':item})


def booking_confirm(request):
    return render(request,"booking_confirm.html")