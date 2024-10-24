from django.shortcuts import redirect,render
from django.template.context_processors import request


def BASE(request):
    return render(request,'base.html')


def HOME(request):
    return render(request,'Main/home.html')


def SINGLE_COURSE(request):
    return render(request,'Main/single_course.html')


def CONTACT_US(request):
    return render(request,'Main/contact_us.html')