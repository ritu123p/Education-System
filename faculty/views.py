from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def faculty(request):
    return HttpResponse('<h1>faculty<h1>')


def fHome(request):
    return render(request,'fHome.html')