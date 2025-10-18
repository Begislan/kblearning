from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import DataUser
from django.views.decorators.http import require_POST


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('adm:dashboard')
        else:
            return redirect('login')
    return render(request, 'userregister/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')