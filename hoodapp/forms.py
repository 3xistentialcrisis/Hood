from django import forms
from .models import Neighbourhood


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = fields = ['neighborhood_name','location', 'population']