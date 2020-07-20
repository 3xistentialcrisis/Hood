from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Neighbourhood, Profile, Business, Post

#Neighbourhood
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = fields = ['neighbourhood_name','location', 'population']

#UpdateUser
class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')

#Update User's Profile        
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'email']
        exclude=['user'] 

#User Signup
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=230)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#Business
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['image','name', 'email', 'description']
        exclude= ['hood', 'user']

#Post
class PostMessageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','message']