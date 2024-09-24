from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def myAdmin(request):
    return HttpResponse('<h1>myadmin</h1>')

def aHome(request):
    return render(request,'aHome.html')