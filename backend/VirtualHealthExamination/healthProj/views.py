from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'healthProj/index.html',{})

def contact(request):
    return render(request,'healthProj/contactUS.html',{})

def find(request):
    return render(request,'healthProj/find.html',{})

def upload(request):
    return render(request,'healthProj/upload.html',{})