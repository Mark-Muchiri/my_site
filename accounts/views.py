from django.shortcuts import render
from . import views

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return