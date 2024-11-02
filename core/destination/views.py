from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import Destination
from .forms import DestinationForm, DestinationSearchForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from accounts.models import Destination



# Create your views here.
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
        
        if form.cleaned_data.get('is_favorite'):
            destination.is_favorite = True 
            destination.favorites.add(request.user)
            destination.save()
            messages.success(request,"Destination added successfully")
        
        return redirect('destination_list')
    
    else:
        form = DestinationForm()
    return render(request,'destination_form.html',{'form':form,'is_update': False })


def destination_detail(request,id):
    destination = get_object_or_404(Destination,id=id)
    return render(request,'destination_detail.html',{'destination':destination})

@login_required
def mydestination(request):
    destinations = Destination.objects.filter(user = request.user)
    
    return render(request,'mydestination.html',{'destinations':destinations,'username': request.user.username})


def destination_update(request,destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request,'Destination updated')
            return redirect('destination_detail', id=destination_id)
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destination_form.html', {'form': form, 'is_update': True,'destination':destination})


def destination_delete(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.method == 'POST':
        destination.delete()
        return redirect('mydestination')

    return render(request,'destination_delete.html', {'destination':destination})


@login_required
def favorite_destination(request,destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.user in destination.favorites.all():
        destination.favorites.remove(request.user)
        messages.success(request,"Removed from favorites")
    else:
        destination.favorites.add(request.user)
        messages.success(request,"Add to favorites")
        
    return redirect('destination_detail', id=destination.id)


@login_required

def my_favorites(request):
    favorite_destination = Destination.objects.filter(favorites=request.user)
    
    return render(request,'my_favorites.html',{'favorite_destination':favorite_destination})


def likes_destination(request, destination_id):
    destination =get_object_or_404(Destination,id=destination_id)
    if request.user in destination.likes.all():
        destination.likes.remove(request.user)
        
    else:
        destination.likes.add(request.user)
        
    return redirect('destination_detail', id=destination.id)


