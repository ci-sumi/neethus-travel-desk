from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{'show_services':True})

def register(request):
    return render(request,'register.html',{'show_services':False})


def login(request):
    return render(request,'login.html',{'show_services':False})