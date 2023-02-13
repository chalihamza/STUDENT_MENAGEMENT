from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse

from accounts.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
#
def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user is not None:
            auth_login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('home')
            elif user_type == '2':
                return HttpResponse('This is teacher panel')
            elif user_type == '3':
                return HttpResponse('This is student panel')
            else:
                messages.error(request, 'Email and password are invalid')
                return redirect('login')
        else:
            messages.error(request, 'Email and password are invalid')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')


