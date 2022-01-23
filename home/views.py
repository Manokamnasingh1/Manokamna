from django.shortcuts import render
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'index.html')
def success(request):
    return render(request, 'success.html')
    

 
