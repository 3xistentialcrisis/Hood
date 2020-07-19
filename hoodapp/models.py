from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Neighbourhood 
class Neighbourhood(models.Model):
    neighbourhood_name= models.CharField(max_length=100)
    location=models.CharField(max_length=30)
    