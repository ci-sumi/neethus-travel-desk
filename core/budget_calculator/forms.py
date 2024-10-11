from django import forms
from accounts.models import Destination

class BudgetCalculatorForm(forms.Form): 
    destination = forms.ModelChoiceField(
        queryset=Destination.objects.all(),
        label="Destination",
        empty_label= "Selected Destination")
    accomadation_cost = forms.DecimalField(label="Accomadation cost",max_digits=10,decimal_places=2,initial=0)
    transportation_cost = forms.DecimalField(label="Transportation cost",max_digits=10,decimal_places=2,initial=0)
    food_cost = forms.DecimalField(label="Food cost",max_digits=10,decimal_places=2,initial=0)
    activity_cost = forms.DecimalField(label="Activity cost",max_digits=10,decimal_places=2,initial=0)
    number_of_adults = forms.IntegerField(label="Number of Adults",min_value=1,initial=1)
    number_of_infants = forms.IntegerField(label="Number of Infants", min_value=0, initial=0)