from django.urls import path
from .import views as v

urlpatterns=[
    path('',v.index,name='index'),
    path('addpackages/',v.addpackages,name='addpackages'),
    path('userpackages/',v.userpackages,name='userpackages'),
    path('contact/',v.contact,name='contact'),
    path('userlogin/',v.usrlogn,name='usrlogn'),
    path('userregistration/',v.userregistration,name='userregistration'),
    path('vendorregistration/',v.vendorregistration,name='vendorregistration'),
    path('vendorlogin/',v.vendorlogin,name='vendorlogin'),
    path('disply/',v.disply,name='disply'),
    path('confirm/',v.confirm,name='confirm'),
    path('item/<int:pk>/delete',v.delt,name='delt'),
    path('item/<int:pk>/edit',v.editt,name='editt'),
    path('user_dis/',v.user_dis,name='user_dis'),
    path('logout/',v.logoutt,name='logoutt'),
    path('searchbar/',v.searchbar,name='searchbar'),
    path('home/',v.home,name='home'),
    path('vendorhome/',v.vendorhome,name='vendorhome'),
    path('approvedpackages/',v.approvedpackages,name='approvedpackages'),
    path('success/',v.success,name='success'),
    path('package_details/<int:pk>/', v.package_details, name='package_details'),
    path('book_package/<int:pk>/', v.book_package, name='book_package'),
    path('user_dis_package/',v.user_dis_package,name='user_dis_package'),
    path('booking_confirm/',v.booking_confirm,name='booking_confirm'),
    path('invalidpass/',v.invalidpass,name='invalidpass'),
    path('invaliduser/',v.invaliduser,name='invaliduser'),
    path('userexist/',v.userexist,name='userexist'),
    path('invalidpassv/',v.invalidpassv,name='invalidpassv'),
    path('invaliduserv/',v.invaliduserv,name='invaliduserv'),
    path('userexistv/',v.userexistv,name='userexistv'),
    ]


