from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    
    @classmethod
    def get_neighbourhoods(cls):
        estates = Neighbourhood.objects.all()
        return estates
    
    @classmethod
    def get_one_hood(cls,id):
        chosen_hood = cls.objects.get(id=id)
        return chosen_hood

#User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # user= models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    name = models.CharField(blank=True, max_length=120)
    # neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
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
    description = models.TextField(default='Tell Us More About Your Business')
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
    
    @classmethod
    def find_business(cls,neighbourhood_id):
        messages = cls.objects.all().filter(hood=neighbourhood_id)
        return messages
    
#Post 
class Post(models.Model):
    title = models.CharField(max_length=155)
    image=models.ImageField(upload_to='photos/',null=True,blank=True)
    image_name=models.CharField(max_length=30)
    message=models.TextField(max_length=100,null=True,blank=True)
    estate=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True,blank=True)
    user_profile=models.ForeignKey(Profile)
    user=models.ForeignKey(User)

    def __str__(self):
        return f'{self.title}'

    def save_post(self):     
        self.save()

    def delete_post(self):     
        self.delete()

    @classmethod
    def get_posts(cls):      
        messages = cls.objects.all()
        return messages

#Security
class Security(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=200)

    def __str__(self):
        return self.company

#Health
class Health(models.Model):
    # neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

    def save_health(self):
        self.save()
    
    def delete_health(self):
        self.delete()