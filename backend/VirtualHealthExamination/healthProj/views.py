from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .dataset import doctor_data_set
from random import choice
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import os
from pathlib import Path

def upload_msg(msg):
    return '''
    We have received your request.
    We are done scanning it.
    Thank You for using our portal.
    Please Take Care.
    
    The probability of You being CORONA affected is :''' + msg + '''
    Virtual Health Examiner
    Copyright 2020
    ''' 

# Create your views here.
def index(request):
    return render(request,'healthProj/index.html',{})

def contact(request):
    return render(request,'healthProj/contactUS.html',{})

@login_required
def find(request):
    return render(request,'healthProj/find.html',{})

@login_required
def doctors(request):
    special = request.GET['doctor']
    if special in doctor_data_set.data_set:
        doctors = doctor_data_set.data_set[special]
        button = True
        if len(doctors) == 1:
            button = False
        context = {'special':special, 'button' : button}
        context.update(choice(doctors))
        return render(request,'healthProj/doctors.html',context)

@login_required    
def fullList(request,specialisation):
    sp = specialisation
    print(sp)
    if sp in doctor_data_set.data_set:
        doctors = doctor_data_set.data_set[sp]
        return render(request,'healthProj/doctors.html',{'doctors':doctors,'special':sp})

@login_required
def upload(request):
    if request.method=='POST':
        from . import xray as XX
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        print(uploaded_file.name)
        print(uploaded_file.size)
        messages.success(request,('File successfully uploaded.'))# + str(XX.predict(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name))))))
        print(XX.predict(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name))))
        send_mail(
			'Request Received',
			upload_msg(str(XX.predict(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name))))),
			settings.EMAIL_HOST_USER,
			[request.user.email]
		)
        return redirect('upload')
    
    return render(request,'healthProj/upload.html',{})

@login_required
def appointment(request,email):
    if request.method == "POST":
        print('Sufiyan')
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message = request.POST['message']     
        # sending email to user
        print('mail')
        send_mail(
			'Message From '+ message_name,
			message,
			settings.EMAIL_HOST_USER,
			[message_email]
		)
        
        return render(request,'healthProj/appointment.html',{'message_name':message_name})
    email_id = email
    fill = False
    if '@' in email and ('.in' in email or '.com' in email):
        fill = True
    return render(request,'healthProj/appointment.html',{'email':email_id,'fill':fill})