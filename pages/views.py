from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser


# Create your views here.
@login_required(login_url='/')
def home(request):
    return render(request, 'pages/home.html')


def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    data = {
        'user': user,
    }
    return render(request, 'pages/profile.html', data)


def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            # customuser.profile_pic = profile_pic

            if password is not None and password != "":
                customuser.set_password(password)
            if profile_pic is not None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile updated Successfully!')
            return redirect('home')
        except:
            messages.error(request, 'Failed to Update your Profile!')
    return render(request, 'pages/profile.html')
