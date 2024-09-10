from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone_number=models.IntegerField()
    contact_message=models.TextField()
    time_stamp = models.DateField(auto_now_add=True,blank=True)