#from django.shortcuts import render
#from django.db import models
from .models import Department,Description,Pseudonym,Employees,Tasks
from django.template import loader
from django.http import HttpResponse




def mainpage(request):
    template = loader.get_template('main.html')    
    return HttpResponse(template.render())


def employees(request):
    mydata = Employees.objects.all().values()
    template = loader.get_template('employees.html')
    context = {

        'mymembers': mydata   
    }
    return HttpResponse(template.render(context,request))
def description(request,id):
    employeebyid = Employees.objects.get(id=id)
    myemployee=[]
    for x in range(len(Employees.objects.get(id=id).tasks.all())):
        myemployee.append(Employees.objects.get(id=id).tasks.all()[x].taskName)

    myemployeetasddesc =[]
    for x in range(len(Employees.objects.get(id=id).tasks.all())):
        myemployeetasddesc.append(Employees.objects.get(id=id).tasks.all()[x].taskdescription)
    template = loader.get_template('description.html')
    context = {
    'mymembertasks': myemployee,
    'mymemberid': employeebyid,
    'mymembertaskdecr': myemployeetasddesc
    }
    return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('templates.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

