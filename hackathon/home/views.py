from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User






# Create your views here.
def home(request):
    return render(request,"home/home.html")
def about(request):
    return render(request,"home/about.html")
def contact(request):
    return render(request,"home/contact.html")

def handleSignUp(request):
    if(request.method=="POST"):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

       
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        messages.success(request,"New user registered")
        return redirect('home')

    ## changed here
    else:
        return HttpResponse("404")


def handleLogin(request):
    if(request.method=="POST"):
        loginusername = request.POST['loginuser']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password=loginpass)
        if(user is not None):
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials")
            return redirect('home')
    else:
        ## changed here 
        # return render(request,'home/loginpage.html')
        return HttpResponse("404")

def handleLogout(request):
   
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')

# new added code will be deleted if not works

# def upload(request):
#     return (request,'home/upload.html')