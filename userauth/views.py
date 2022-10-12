from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def SignOutUser(request):
    logout(request)
    return redirect('login')


def SignInUser(request):
    form = LoginUserForm()

    if request.user.is_authenticated:
        return redirect ('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user != None:
                login(request, user)
                return redirect('profile')
            else:
                raise Http404("You are not authorized")

    return render(request, 'userauth/loginPage.html', {'form':form})


def registerUser(request):
    form = CreateUserForm()

    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('login')
        
    return render(request, 'userauth/registerPage.html', {'form':form})


@login_required(login_url='login')
def profile(request):
    username = request.user.username
    email = request.user.email

    context = {
        'username':username,
        'email':email,
    }    

    return render(request, 'userauth/profile.html', context)