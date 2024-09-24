from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import user_master
from .models import contact_master
def home(request):
    return HttpResponse('<h1>Hello World</h1>')




def index(request):
    return render(request,'index.html')




def about(request):
    return render(request,'about.html')





def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ob=contact_master.objects.create(name=name,email=email,message=message)
        ob.save()
        return render(request,'contact.html',{'output':'contact sucessful'})
    return render(request,'contact.html')






def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            ob = user_master.objects.get(username=username,password=password)
            if ob.role =='admin':
                obj=user_master.objects.all()
                return render(request, 'viewData.html',{'user':obj})
            elif ob.role == 'student':
                return render(request, 'sHome.html',{'user':ob})
            elif ob.role == 'faculty':
                ob1=user_master.objects.filter(role='student')
                return render(request, 'fHome.html',{'user':ob,'role':ob1})
            else:
                return render(request,'login.html')
        except Exception as e:
            return render(request,'login.html',{'data':'invalid username and password'})
    return render(request,'login.html')





def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        password= request.POST['password']
        ob=user_master.objects.create(username=username,email=email,mobile=mobile,role=role,password=password)
        ob.save()
        return render(request,'register.html',{'output':'register sucessful'})
    return render(request,'register.html')






def galary(request):
    return render(request,'galary.html')






def faq(request):
    return render(request,'faq.html')






def add(request):
    # result=0
    if request.method == 'POST':
        val1=int(request.POST["num1"])
        val2=int(request.POST["num2"])
        result=val1+val2
        return render(request,'add.html',{'output':result})
    return render(request,'add.html')







def viewData(request):
    ob=user_master.objects.all()
    if request.method == "POST":
        btn = request.POST['btn']
        if btn == "edit":
            email = request.POST["email"]
            try:
                ob = user_master.objects.filter(email=email);
                return render(request,"edit.html",{'data1':ob})
            except Exception as e:
                return render(request,"viewData.html",{'data1':"invalid"+str(e)})
        if btn == "delete":
            email = request.POST["email"]
            try:
                ob = user_master.objects.filter(email=email).delete()
                ob = user_master.objects.all()
                return render(request,"viewData.html",{'user':ob})
            except Exception as e:
                return render(request,"viewData.html",{'user':"invalid"+str(e)})
        return render (request,'viewData.html',{'user':ob})
    return render(request,'viewData.html',{'user':ob})







def edit(request):
    return render(request,'edit.html')



def update(request):
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        try:
            user_master.objects.filter(email=email).update(mobile=mobile,name=name)
            ob = user_master.objects.all()
            return render(request,'viewData.html',{'user':ob})
        except Exception as e:
            return render(request,'viewData.html',{'user':"invalid"})
    return render (request,'viewData.html')