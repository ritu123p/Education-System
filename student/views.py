from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def student(request):
    return HttpResponse('<h1>hello</h1>')

def sHome(request):
    return render(request,'sHome.html')