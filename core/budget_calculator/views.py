from django.shortcuts import render
from .forms import BudgetCalculatorForm
from accounts.models import Destination
# Create your views here.


def budget_calculator(request):
    total_cost = None
    form = BudgetCalculatorForm()
    if request.method == 'POST':
        form = BudgetCalculatorForm(request.POST)
        if form.is_valid():
            accomadation_cost = form.cleaned_data['accomadation_cost']
            food_cost = form.cleaned_data['food_cost']
            transportation_cost = form.cleaned_data['transportation_cost']
            activity_cost = form.cleaned_data['activity_cost']
            number_of_adults = form.cleaned_data['number_of_adults']
            number_of_infants = form.cleaned_data['number_of_infants']
            destination = form.cleaned_data['destination']
            
            
            total_food_cost = food_cost * (number_of_adults + number_of_infants)
            total_cost = (accomadation_cost + transportation_cost + activity_cost+total_food_cost)
            
    return render(request, 'budget.html',{'form':form, 'total_cost':total_cost})
            
        