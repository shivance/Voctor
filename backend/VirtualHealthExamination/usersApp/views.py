from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,'usersApp/login.html',{})

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created. Login To Continue')
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request,'usersApp/register.html',{'form':form})