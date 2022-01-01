from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'app1/home.html')

def map(request):
    return render(request, 'app1/grid_map_2109.html')


def about(request):
    return render(request, 'app1/about.html')

def proj_about(request):
    return render(request, 'app1/proj_about.html')