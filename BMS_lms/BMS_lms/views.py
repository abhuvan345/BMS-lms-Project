from django.shortcuts import redirect,render
from django.template.context_processors import request


def BASE(request):
    return render(request,'base.html')