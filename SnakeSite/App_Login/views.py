from django.shortcuts import render, HttpResponseRedirect
from .forms import Sign_Up_Form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.


def home(request):
    return render(request, 'App_Login/home.html', context={})


def sign_up(request):
    form = Sign_Up_Form()
    signed_up = False
    if request.method == 'POST':
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
            signed_up = True
    diction = {'form': form, 'signed_up': signed_up}
    return render(request, 'App_Login/sign_up.html', context=diction)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Login:home'))
    diction = {'form': form}
    return render(request, 'App_Login/login.html', context=diction)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:home'))

