from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect



# import emlpoyee data from the apps/ medels.ppy 
from employee_app.models import Employees


# Create your views here.

def index(request):
    emp = Employees.objects.all()

    context ={
        'emp':emp,
    }
    return render(request, "index.html",context)

#1. addempview for view the form that where we can add the details and add will perform adding opertaion and its redirect the home page with the new data

def addempview(request):
    return render(request, "add.html")


def ADD(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
       

 # first name is the model name and second is in the html name file
#  this is for saving the new data
        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
# This will help to save the data
        emp.save()
    return redirect('index')




# 2. edit

def editview(request, id):
    emp = Employees.objects.all()
    context ={
        'emp':emp,
    }
    return render(request, "edite.html",context)
 
    # return render(request,'edit.html', {'emp':emp})


def edit(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
       

        emp = Employees.objects.get(id=request.POST['empid'])
        emp.name = name,
        emp.email = email,
        address = address,
        phone = phone,
        emp.save()
    return render(request, 'edit.html')


def deleteView(request):
    emp = Employees.objects.get(id=request.POST['empid'])
    emp.delete()
    return HttpResponseRedirect ("/")








