from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from pyexpat.errors import messages


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already Exists !')
            return redirect('register')

        #check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username Already exists !')
            return redirect('register')

        user =User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request,'registration/register.html')