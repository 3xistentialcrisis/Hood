from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Neighbourhood 
class Neighbourhood(models.Model):
    neighbourhood_name= models.CharField(max_length=100)
    location=models.CharField(max_length=30)
    population=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.neighborhood

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

#User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # user= models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user
    
    @receiver(post_save, sender=User)
    def create_userprofile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_userprofile(sender, instance, **kwargs):
        instance.profile.save()

#Business
class Business(models.Model):
    image=models.ImageField(upload_to='business/', default = '/media/default.png')
    description = models.TextField(default='Welcome')
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=70,blank=True)
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
    
    @classmethod
    def search_business(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses
    

    