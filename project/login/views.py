from django.shortcuts import render
from .models import User
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, 'login.html')


def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User(username=username, password=password)
    user.save()
    return redirect('/')
