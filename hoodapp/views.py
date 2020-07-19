from django.shortcuts import render

# Create your views here.
#Index Page

def index(request):
    return render(request, 'index.html')
