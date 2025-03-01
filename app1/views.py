from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app1.models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        new_todo=todo(user=request.user, todo_name=task)
        new_todo.save()
    all_todos=todo.objects.filter(user=request.user)
    context={'todos':all_todos}
    return render(request,'todo.html',context)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home')
        else:
            messages.error(request,"Error, wrong user details or user does not exist.")
            return redirect('loginpage')
    return render(request,'login.html',context)
def logoutpage(request):
    logout(request)
    return redirect('loginpage')
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if len(password)<4:
            messages.error(request, 'Password must to at-least 4 character')
            return redirect('register')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()

    return render(request,'register.html',context)
def Deletetask(request,id):
    get_todo=todo.objects.get(user=request.user,id=id)
    get_todo.delete()
    return redirect('home')
def Updatetask(request,id):
    get_todo=todo.objects.get(user=request.user,id=id)
    get_todo.status=True
    get_todo.save()
    return redirect('home')
