from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Neighbourhood

# Create your views here.
#Index Page
def index(request):
    return render(request, 'index.html')

#Profile
@login_required(login_url='/accounts/login/')
def profile(request, username):
    return render(request, 'profile.html')
