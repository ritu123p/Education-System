"""
URL configuration for Education_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views as hviews
from student import views as sviews
from faculty import views as fviews
from myAdmin import views as aviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home',hviews.home),
    path('about',hviews.about),
    path('add',hviews.add),
    path('contact',hviews.contact),
    path('faq',hviews.faq),
    path('galary',hviews.galary),
    path('index',hviews.index),
    path('login',hviews.login),
    path('register',hviews.register),
    path('viewData',hviews.viewData),
    path('edit',hviews.edit),
    path('update',hviews.update),



    path('student',sviews.student),
    path('sHome',sviews.sHome),



    path('faculty',fviews.faculty),
    path('fHome',fviews.fHome),




    path('myadmin',aviews.myAdmin),
    path('aHome',aviews.aHome),
]
