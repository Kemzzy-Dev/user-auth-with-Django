from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404


# Create your views here.
def loginPage(request):
    form = LoginUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            raise Http404("You are not authorized")

    return render(request, 'userauth/loginPage.html', {'form':form})


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    return render(request, 'userauth/registerPage.html', {'form':form})


#change the name to profile later
def index(request):

    return render(request, 'userauth/profile.html')