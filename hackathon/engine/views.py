from django.shortcuts import render,HttpResponse,redirect
from engine.models import Found,Lost
from django.contrib.auth.models import User
from django.contrib import messages

from DeepImageSearch import Index,LoadData,SearchImage
import os
import smtplib
from email.mime.text import MIMEText
email_sender = "officialap1812@gmail.com"
email_password = "tsfxvccdminnpcku"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

def emailLost(request,slug):
    # dl = slug.split('^')[1]
    obj = ""
    path = r"C:\Users\Pratham\OneDrive\Desktop\hackathon\media"
    for i in Found.objects.all():
        if(i.sno==slug):
            obj =i
    em = obj.email
    # message to be sent
    initial = User.objects.filter(username=request.user).values()[0]
    subject = "Re. Item Found"
    recipients = [em]
    
    
    message = "Hello "+obj.name+"\n" +"Your "+obj.itemname+","+"which was uploaded as found by you belongs to"+initial['first_name']+"\n He will contact you shortly with his id "+ initial['email']
    
    # sending the mail
    send_email(subject, message, email_sender, recipients, email_password)

    fin = os.path.join(path,obj.image.name)
    os.remove(fin)
    
    obj.delete()
    print(em)
    print(slug)

    messages.success(request,"informed successfully")
    return redirect('home')
def emailf(request,slug):
    # dl = slug.split('^')[1]dl
    obj = ""
    path = r"C:\Users\Pratham\OneDrive\Desktop\hackathon\media"
    for i in Lost.objects.all():
        if(i.sno==slug):
            obj =i
    
    em = obj.email
    recipients = [em]
    subject = "Re. Item Found"

    initial = User.objects.filter(username=request.user).values()[0]

    for i in Found.objects.all():
        if(i.sno==slug):
            obj =i
    em = obj.email
   
 
    # start TLS for security
    
    
    message = "Hello"+obj.name+"\n" +"Your "+obj.itemname+","+"which was uploaded as lost by you was found by "+initial.username+"\n Please contact him on his email id:"+ initial.email
    
    # sending the mail
    send_email(subject, message, email_sender, recipients, email_password)

    fin = os.path.join(path,obj.image.name)
    os.remove(fin)
    obj.delete()
    print(em)
    print(slug)
    messages.success(request,"informed successfully")
    return redirect('home')

def find(category,image):
    if(category == "Found"):
        path = r"C:\Users\Pratham\OneDrive\Desktop\hackathon\media\images\Found"
        
        image_list = LoadData().from_folder(folder_list = [path])

        Index(image_list).Start()
        return(SearchImage().get_similar_images(image_path=image,number_of_images=1))
    else:
        path = r"C:\Users\Pratham\OneDrive\Desktop\hackathon\media\images\Lost"
        # path = os.path.join(os.getcwd(),'media','images','Lost')
        
        image_list = LoadData().from_folder(folder_list = [path])

        Index(image_list).Start()
        return (SearchImage().get_similar_images(image_path=image,number_of_images=1))


params = User.objects.all()
# Create your views here.
def root(request):
    # lust1 = Lost.objects.all()
    # # for i in lust1:
    # #     print(i.sno)
    # s =lust1[0].image.name
    # print(s+"123")
    
    print(User.objects.filter(username=request.user).values()[0]['first_name'])
    return HttpResponse("Checking 101")
def force(request):
    if request.method=="POST":
        print("chal ja")
        item = request.POST['ite']
        name = ""
        email =request.POST['emal']
        image = request.FILES['img']
        for i in params:
                if i.email == email:
                    name = i.username
                    
        print(item,name,email)
        Eng = Lost(itemname=item,name=name,image=image,email=email)
        Eng.save()
        print("Everything worked")
        messages.success(request,"Your item has been uploaded in the database")

        return redirect('home')
    else:
        return HttpResponse("checking")
def forceadd(request):
    if request.method=="POST":
        print("chal ja")
        item = request.POST['item']
        name = ""
        email =request.POST['email']
        image = request.FILES['image']
        for i in params:
                if i.email == email:
                    name = i.username
                    
        print(item,name,email)
        Eng = Found(itemname=item,name=name,image=image,email=email)
        Eng.save()
        print("Everything worked")
        messages.success(request,"Your item has been uploaded in the database")

        return redirect('home')
    else:
        return HttpResponse("checking")
        

def add(request):
    if request.method=="POST":
        print("chal ja")
        item = request.POST['item']
        name = ""
        email =request.POST['email']
        image = request.FILES['image']
        dic = find("Lost",image)
        if(len(dic)=='None'):
            for i in params:
                if i.email == email:
                    name = i.username
                    
            print(item,name,email)
            Eng = Found(itemname=item,name=name,image=image,email=email)
            Eng.save()
            
            print("Everything worked")
            messages.success(request,"Your item has been uploaded in the database")

            return redirect('home')
        else:
            path = """images/Lost/"""+list(dic.values())[0].split('\\')[-1]
            # counter =0
            
            parameters = {}
            for i in Lost.objects.all():
                if i.image == path:
                    parameters['p1'] = i
                    break;
            if(len(parameters)==0):
                Eng = Found(itemname=item,name=name,image=image,email=email)
                Eng.save()
                print("Everything worked")
                messages.success(request,"Your item has been uploaded in the database")

                return redirect('home')

            print(parameters,path)
            # lust1 = Lost.objects.filter(image=s)
            # s2 = list(dic.values())[0].split('\\')[-1]
            # lust2 = Lost.objects.filter(image=s2)
            # print(lust1)
            
            # print(parameters['p1'].email)
            return render(request,"engine/found.html",parameters)
            # return HttpResponse("Checking 101")

        
def search(request):
    

    if request.method=="POST":
        print("chal ja")
        item = request.POST['ite']
        name = ""
        email =request.POST['emal']
        image = request.FILES['img']
        dic = find("Found",image)
        
        if(len(dic)==0):
            for i in params:
                if i.email == email:
                    name = i.username
                    
            print(item,name,email)
            Eng = Lost(itemname=item,name=name,image=image,email=email)
            Eng.save()
            
            print("Everything worked")
            messages.success(request,"Your item has been uploaded in the database")

            return redirect('home')
        else:
            path = """images/Found/"""+list(dic.values())[0].split('\\')[-1]
            # counter =0
            parameters = {}
            for i in Found.objects.all():
                if i.image == path:
                    parameters['p1'] = i
                    break;
            if(len(parameters)==0):
                Eng = Lost(itemname=item,name=name,image=image,email=email)
                Eng.save()
                print("Everything worked")
                messages.success(request,"Your item has been uploaded in the database")

                return redirect('home')
            
            # lust1 = Lost.objects.filter(image=s)
            # s2 = list(dic.values())[0].split('\\')[-1]
            # lust2 = Lost.objects.filter(image=s2)
            # print(lust1)
          
            
            # print(parameters['p1'].email)
            return render(request,"engine/lost.html",parameters)
            # return HttpResponse("Checking 101")
            return HttpResponse("Found")
                

 