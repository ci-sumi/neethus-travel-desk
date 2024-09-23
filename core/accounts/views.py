from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .forms import ContactForm
from .forms import DestinationForm
from .models import Destination
from django.core.paginator import Paginator
from django.db.models import Q
from django import forms
from .forms import DestinationSearchForm
from django.contrib.auth.decorators import login_required


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
    form = DestinationSearchForm(request.GET or None)
    query = request.GET.get('query','')
    if query:
        destinations_list = Destination.objects.filter(
           Q(name__icontains=query) |
           Q(country__icontains=query) |
           Q(description__icontains=query) |
           Q(best_time_to_visit__icontains=query)|
           Q(budget_type__icontains=query)
           
           
           
        )
           
    else:
        destinations_list = Destination.objects.all()
    paginator = Paginator(destinations_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'destination_list.html',{'page_obj':page_obj})

@login_required
def destination_create(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        destination = form.save(commit=False)
        destination.user = request.user
        destination.save()
        return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request,'destination_form.html',{'form':form})


def destination_detail(request,id):
    destination = get_object_or_404(Destination,id=id)
    return render(request,'destination_detail.html',{'destination':destination})

@login_required
def mydestination(request):
    destinations = Destination.objects.filter(user = request.user)
    
    return render(request,'mydestination.html',{'destinations':destinations,'username': request.user.username})