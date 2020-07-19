from django import forms
from django.contrib.auth.models import User
from .models import Neighbourhood, Profile

#Neighbo
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = fields = ['neighbourhood_name','location', 'population']

class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')
        
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'email']
        exclude=['user'] 