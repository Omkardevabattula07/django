from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import Userprofile
from django.contrib.auth.models import User
# Create your views here.
common=['password','1234567890','qwerty']
def index(request):
    return render(request,"index.html")
def register_view(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        bio=request.POST['bio']
        profile_pic=request.FILES.get('profile_pic')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
            return redirect('register')
        elif password1 != password2:
            messages.error(request,'Passwords doesn\'t match ')
            return redirect('register')
        elif len(password1)<10:
            messages.error(request,'Password is too short')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already taken')
            return redirect('register')
        elif password1 in common:
            messages.error(request,'Choose a stronger password')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.is_active=False
            user.save()
            userprofile=Userprofile(user=user,bio=bio,profile_pic=profile_pic)
            userprofile.save()
            messages.success(request,'Registration succesfull waiting for approval')
            return redirect('wait')
    return render(request,'register.html')
def login_view(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                if user.is_superuser:
                    messages.success(request,'welcome f"{user.username}"')
                    return redirect('superuser')
                else:
                    messages.success(request,"Welcome f{user.username}")
                    return redirect('userprofile')
            else:
                messages.info(request,'You are in the waiting list f{username}')
                return redirect('wait')
        else:
            messages.error(request,'Invalid credentials')  
            return redirect('login') 
    return render(request,'login.html')
def wait(request):
    return render(request,'wait.html')
def superuser(request):
    return render(request,'superuser.html')
def userprofile(request):
    return render(request,'userprofile.html')