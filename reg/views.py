from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login as us_login,logout as us_logout,authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth.models import  User as us_user
from .forms import SignUpForm,d_form,t_form,s_form
from . models import department,teacher,student

# Create your views here.
def base(request):
    return render(request,'base.html')

def profile(request):
    return render(request,'profile.html')


def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Registered...'))
			return redirect('base')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'register.html', context)

def logout(request):
    us_logout(request)
    messages.success(request,('logout'))
    return redirect('base')

def home(request):
    user=us_user.objects.all()
    return render(request,'home.html',{'data':user})


def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username,password)
            my_user = authenticate(request ,username=username, password=password)
            if my_user is not None:
                print(my_user)
                us_login(request,my_user)
                messages.success(request, ('You Have Been Logged In!'))
                return redirect('home')
            else:
                messages.success(request, ('Error Logging In - Please Try Again...'))
                return redirect('login')
                
                
    else:
        fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})



def department_view(request):
    if request.method =='POST':
        fm = d_form(request.POST)
        if fm.is_valid():
            dname = fm.cleaned_data['dept_name']
            department(dept_name = dname).save()
            messages.success(request,'succesfully added')
            return redirect('department')
    else:
        fm = d_form()
        return render(request,'department.html',{'form':fm})
    
def teacher_view(request):
    if request.method =='POST':
        fm = t_form(request.POST)
        if fm.is_valid():
            tname = fm.cleaned_data['tname']
            dname = fm.cleaned_data['tdept_name']
            teacher(tname = tname, tdept_name = dname ).save()
            messages.success(request,' Added succesfully ')
            return redirect('teacher')
    else:
        fm = t_form()
        return render(request,'teacher.html',{'form':fm})


def student_view(request):
    if request.method =='POST':
        fm = s_form(request.POST)
        if fm.is_valid():
            Roll = fm.cleaned_data['roll']
            name = fm.cleaned_data['sname']
            f_name = fm.cleaned_data['father_name']
            contact = fm.cleaned_data['contact']
            sdept_name = fm.cleaned_data['sdept_name']
            student(roll=Roll,sname=name,father_name=f_name,contact=contact,sdept_name=sdept_name).save()
            return redirect('student')
    else:
        fm = s_form()
        return render(request,'student.html',{'form':fm})


def ddetails(request):
    fm = department.objects.all()
    return render(request,'ddetails.html',{'data':fm})


def delete(request,did):
    rem = department.objects.filter(id = did)
    rem.delete()
    return redirect('ddetails')
    

def update(request,did):
    pk = department.objects.get(id = did)
    if request.method =='POST':
        fm = d_form(request.POST ,instance=pk)
        if fm.is_valid():
            dname = fm.cleaned_data['dept_name']
            department(id= did,dept_name = dname).save()
            messages.success(request,' update succesfully ')
            return redirect('department')
    else:
        fm = d_form(instance=pk)
        return render(request,'department.html',{'form':fm})