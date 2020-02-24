from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def hello(request):
    #Query Data From Model
    data=Post.objects.all()
    return render(request,'index.html',{'posts':data})

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def loginForm(request):
    return render(request,'login.html')

def addUser(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'UserName นีมีคนใช้แล้ว')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้เคยลงทะเบียนแล้ว')
            return redirect('/createForm')
        else :
            user=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
            )
            user.save()    
            return redirect('/')
    else :
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/createForm')

def login(request):
    username=request.POST['username']
    password=request.POST['password']

    #check username ,password
    user=auth.authenticate(username=username,password=password)

    if user is not None :
       auth.login(request,user)
       return redirect('/')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/')