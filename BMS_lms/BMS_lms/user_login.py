from django.shortcuts import render,redirect


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


    return render(request,'registration/register.html')