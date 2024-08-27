from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html',{'show_services':True})

def register(request):
    if request.method=="POST":
       form = SignupForm(request.POST)
       if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect('login')
       else:
           messages.error(request,"Error")
    else:
        form = SignupForm()
        
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POSt.get('password')
        if username is not None:
            login(request,username)
            return redirect('index')
        else:
            pass
    else:
        return render(request,'login.html',{'show_services':False})