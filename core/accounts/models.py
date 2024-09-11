from django.db import models
from django import forms

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone_number=models.IntegerField()
    contact_message=models.TextField()
    time_stamp = models.DateField(auto_now_add=True,blank=True)
    
    
class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    SEASON_CHOICES = [('Spring','Spring'),
                      ('Summer','Summer'),
                      ('Spring','Spring'),
                      ('Winter','Winter')]
    best_time_to_visit = models.CharField(max_length=6,choices=SEASON_CHOICES,
                                          default='Spring')
    BUDGET_CHOICES = [('Budget','Budget'),
                      ('Mid-range','Mid-range'),
                      ('Luxury','Luxury')]
    budget_type = models.CharField(max_length=10,
                                   choices=BUDGET_CHOICES,
                                   default='Mid-range')
    image = models.ImageField(upload_to='destinations/',blank=True,null=True)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
