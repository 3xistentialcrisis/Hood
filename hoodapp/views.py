from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Neighbourhood, Profile

# Create your views here.
#Index Page
def index(request):
    return render(request, 'index.html')

#Profile
@login_required(login_url='/accounts/login/')
def profile(request, username):
    return render(request, 'profile.html')

#User Profile
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)
