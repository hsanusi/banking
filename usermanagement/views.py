from django.shortcuts import redirect, render
from .forms import RegisterForm,UserCreationForm
from django.contrib.auth import login,logout

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('/manageuser/home')
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request,"registration/sign-up.html",context)

def registerUser(request):
    page = 'register'
    myform = UserCreationForm()
    if request.method == "POST":
        myform = UserCreationForm(request.POST)
        if myform.is_valid():
            user = myform.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
       
    context = {
       'form': myform
    }
    return render(request,'safemanager/login_register.html',context)

def handleLogout(request):
    logout(request)
    return redirect('login')
