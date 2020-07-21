from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignupForm, UpdateProfileForm, UpdateUserProfileForm, PostMessageForm, BusinessForm, NeighbourhoodForm
from .models import Neighbourhood, Profile, Business, Post, Security, Health

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
    business=Business.find_business
    return render(request, 'homepage.html', {'user':current_user, "posts":post, "hoods":hoods, "business":business})


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
            return redirect('hoodapp:homepage')
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
                return redirect('hoodapp:homepage')
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

#Display All Businesses
@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    business_hood = profile.location
    businesses = Business.objects.filter(name=business_hood)

    return render(request,'all_businesses.html',{"businesses":businesses})

#Create New Business
@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user=request.user
    profile =Profile.objects.get(user=current_user)

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.user = current_user
            Neighbourhood.hood = profile.location
            business.save()

        return HttpResponseRedirect('/all_businesses')

    else:
        form = BusinessForm()

    return render(request,'new_business.html',{"form":form})

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
            Post = form.save(commit=False)
            Post.user = current_user
            Post.user_profile = posts
            Post.save()
        return redirect('hoodapp:homepage')

    else:
        form = PostMessageForm()

    return render(request,'new_post.html',{"form":form})


#Create Neighbourhood
@login_required(login_url='/accounts/login')
def create_neighbourhood(request):
    if request.method=='post':
        form=NeighbourhoodForm(request.POST,request.files)
        if form.is_valid():
            neighbourhood=form.save(commit=False)
            neighbourhood.user=current_user
            neighbourhood.save()
            return redirect('hoodapp:homepage')

        else:
            form=NeighbourhoodForm()
        return render(request,'neighbourhood.html',{"form":form})

#All Neighbourhoods
def neighbourhoods(request):
    current_user=request.user
    hoods=Neighbourhood.get_neighbourhoods
    return render (request,'allneighbourhoods.html',{"user":current_user,"hoods":hoods})

#One Neighbourhood
@login_required(login_url='/accounts/login')
def hood_details(request,neighbourhood_name):
    if len(Follow.objects.all().filter(user=request.user))>0:
        details=Neighbourhood.get_one_hood(neighbourhood_name)
        exists=Follow.objects.all().get(user=request.user)
    else:
        details=Neighbourhood.get_one_hood(neighbourhood_name)
        exists=0
    return render(request,'one_hood.html',{"exists":exists,"details":details})

#Security
@login_required(login_url='/accounts/login/')
def security(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    security_details = profile.location
    security = Security.objects.filter(company=security_details)

    return render(request,'security.html',{"security":security})

#Health 
@login_required(login_url='/accounts/login/')
def health(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    health_services = profile.location
    healthy = Health.objects.filter(name=health_services)
    return render(request,'health.html',{"healthy":healthy})

