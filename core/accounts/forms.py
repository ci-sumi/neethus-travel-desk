from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact

class SignupForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email=forms.EmailField(required=True)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        
        
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This user already taken")
        return username
    
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email alrady taken")
        return email
    
    
    def clean_password2(self):
        clean_data = super().clean()
        passsword1 = clean_data.get("password1")
        password2 = clean_data.get("password2")
        if passsword1 and password2 and passsword1!=password2:
            raise forms.ValidationError("Password do not match")
        return password2
        
    

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"