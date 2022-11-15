from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'index.html')

def fetch(request):
    data_list = models.employe.objects.all()
    return render(request,'display.html',{'data_list':data_list})

def data(request):     
    x = request.GET["eid"]
    y = request.GET["ename"]
    z = request.GET["edes"]
    g = request.GET["sal"] 
    if models.employe.objects.filter(id=x).exists():
        return HttpResponse("id already exists")
    else:   
        a = models.employe(x,y,z,g)
        a.save()
        data_list = models.employe.objects.all()
        return redirect(fetch)

def update(request,id):
    data_list = models.employe.objects.get(id=id)
    if request.method=="POST":
        x = request.POST["eid"]
        y = request.POST["ename"]
        z = request.POST["edes"]
        g = request.POST["sal"]
        data_list.id=x
        data_list.ename=y
        data_list.e_des=z
        data_list.e_sal=g
        data_list.save()
        messages.success(request,"succesly updated")
        return redirect('fetch')
    return render(request,'update.html',{'data_list':data_list})

def delete(request,id):
    data_list = models.employe.objects.get(id=id)
    data_list.delete()
    messages.success(request,"successfully deleted")
    return redirect('fetch')


    