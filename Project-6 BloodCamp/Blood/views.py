from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from . models import patient,donardetail
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import Formdonar
from django.contrib import messages
import random
from django.http import JsonResponse
from datetime import datetime
def home(request):
    return render(request,'home.html')
def registration(request):
    if request.method=="POST":
        Full_Name=request.POST['Full_Name']
        password=request.POST['password']
        Email=request.POST['Email']
        Date_of_Birth=request.POST['Date_of_Birth']
        confirmation_password=request.POST['confirmation_password']
        present_date=datetime.today().year
        date_obj=datetime.strptime(Date_of_Birth,"%Y-%m-%d").date()
        year=date_obj.year
        D_O_B=present_date-year
        if password == confirmation_password:
            exist=User.objects.filter(username=Full_Name)
            if exist :
                message='username already exist user another'
                return render(request,'registration.html',{'error':message}) 
            else:
                email=User.objects.filter(email=Email)
                if email :
                    message='Email already exist user another'
                    return render(request,'registration.html',{'error':message})
                else:
                    if D_O_B <=17:
                        message="You'r not Eligible to create Account.Age should be greater than 16"
                        return render(request,'registration.html',{'error':message})
                    else:
                        user=User.objects.create_user(username=Full_Name,password=password,email=Email)
                        user.save()
                        user = authenticate(request,username=Full_Name ,password=password)
                        login(request,user)
                        message="Saved Sucessfully"
                        return render(request,'home.html',{'error':message})             
        else:
            message='please check all fields once'
            return render(request,'registration.html',{'error':message})
    return render(request,'registration.html')
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username ,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message='please check login details'
            return render(request,'login.html',{'error':message})
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def addpatient(request):
    if request.method=="POST":
        Full_Name=request.POST['Full_Name']
        Phone =request.POST['Phone']
        Email=request.POST['Email']
        Blood_type=request.POST['Blood_type']
        patients=patient.objects.create(Full_Name=Full_Name,Phone=Phone,Email=Email,Blood_type=Blood_type)
        patients.save()
        message="Saved Sucessfully"
        return render(request,'addpatient.html',{'error':message})
    return render(request,'addpatient.html')
@login_required(login_url='login')
def search_view(request):
    search = None
    if request.method=="POST":
        blood=request.POST['Blood_type']
        if blood:
            search=donardetail.objects.filter(Blood_type=blood)
            if search :
                return render(request,'search.html',{'search':search})
            else:
                message="No list found"
                return render(request,'search.html',{'message':message})
    return render(request,'search.html',{'search':search})
@login_required(login_url='login')
def profile_view(request):
    if hasattr(request.user, 'donardetail'):
        profile = request.user.donardetail
        return render(request,'profile.html',{'profile':profile})
    else:
        profile = None
        if request.method=="POST":
            Name=request.POST['Name']
            Phone =request.POST['Phone']
            Blood_type=request.POST['Blood_type']
            Date_of_Birth=request.POST['D_O_B']
            current_Address=request.POST['current_Address']
            Address=request.POST['Address']
            drinking = 'Drinking' in request.POST and request.POST['Drinking'] == 'on'
            smoking = 'Smoking' in request.POST and request.POST['Smoking'] == 'on'
            Health_issue=request.POST['Health_issue']
            donar=donardetail.objects.create(Full_Name=request.user,Name=Name,Phone=Phone,Blood_type=Blood_type,Health_issue=Health_issue, Smoking=smoking, Drinking= drinking,Address=Address,current_Address=current_Address,Date_of_Birth=Date_of_Birth)
            donar.save()
            return redirect('profile')
    return render(request,'profile.html')
def custom_404_view(request, exception):
    return render(request,'error.html', status=404)
def editprofile_view(request):
    if request.method=="POST":
        form =Formdonar(request.POST,request.FILES,instance=request.user.donardetail)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form=Formdonar(instance=request.user.donardetail)
    return render(request, 'editprofile.html',{'form':form})