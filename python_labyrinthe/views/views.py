from django.http import HttpResponse

from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'home.html')

def easyLab(request):
    return render(request, 'easyLab.html')

def hardLab(request):
    return render(request, 'hardLab.html')
