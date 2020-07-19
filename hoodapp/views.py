from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignupForm, UpdateProfileForm, UpdateUserProfileForm, PostMessageForm
from .models import Neighbourhood, Profile, Business, Post

# Create your views here.
#Index Page
def index(request):
    return render(request, 'index.html')

#Homepage
@login_required(login_url='/accounts/login/')
def homepage(request):
    current_user =request.user
    hoods=Neighbourhood.get_neighbourhoods
    post=Post.objects.all()
    home=Follow.objects.get(user = request.user)
    business=Business.find_business(home.estates)
    return render(request, 'homepage.html', {'user':current_user, "posts":post, "estates":home,"hoods":hoods, "business":business})


#User Signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index.html')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form })

#User Login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request = request, template_name = "registration/login.html", context={"form":form})

#User Logout
def logout(request):
    auth.logout(request)
    return redirect('hoodapp:login')

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

#Update User Profile
@login_required(login_url='/accounts/login/')
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateProfileForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('hoodapp:profile', user.username)
    else:
        user_form = UpdateProfileForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'update.html', params)

#Search Businesses
def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search_results.html', {"message": message, "businesses": searched_business})

    else:
        message = "You have not searched for any business"
        return render(request, 'search_results.html', {"message": message})

#New Post
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    posts =Profile.objects.get(user = request.user.id)
    if request.method =='POST':
        form = PostMessageForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.user_profile = posts
            project.save()
        return redirect('welcome')

    else:
        form = PostMessageForm()

    return render(request,'new_post.html',{"form":form})
