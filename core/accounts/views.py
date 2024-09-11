from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .forms import ContactForm
from .forms import DestinationForm
from .models import Destination

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Corrected to pass 'user' instead of 'username'
                return redirect('index')  # Redirect to the index page after successful login
            else:
                messages.error(request, "Invalid username or password.")  # Feedback for invalid credentials
        else:
            messages.error(request, "Username and password are required.")  # Feedback for missing fields
    
    # Render the login template with additional context if needed
    return render(request, 'login.html', {'show_services': False})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
            messages.success(request,"Your form is submitted")
            
        
    else:
        form=ContactForm()
        messages.error(request,"Please fill the fiels properly")
    return render(request,'contact.html',{'form':form})
    
def destination_list(request):
    destinations = Destination.objects.all()
    return render(request,'destination_list.html',{'destinations':'destinations'})