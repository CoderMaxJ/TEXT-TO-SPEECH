from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import userInformation

from django. urls import reverse
from django.shortcuts import HttpResponse
import time
import random 
import string
import pyttsx3

# def page(request):
#     return HttpResponse('hello world')
datetime = time.ctime
def home(request):
    
   
      if request.method=="POST":
        if 'create' in request.POST:
            return redirect('create')
        elif 'login' in request.POST:
            return redirect('login')
        elif 'admin' in request.POST:
            return redirect('check')
      
      return render(request,'mainpage.html',{"date":datetime})
    

def create(request):
    return render(request,'registrationForm.html')

def login(request):
        if request.method == 'POST':
            useremail = request.POST['email']
            usercode = request.POST['code']
            try:
                user = userInformation.objects.get(email=useremail, code=usercode)
                
                time.sleep(1)
                
                return render(request,'app.html')
            except userInformation.DoesNotExist:
                errorspeak = pyttsx3.init()
                errorspeak.say("Account not exist! make sure you have written your account correctly")
                errorspeak.runAndWait()
                err = 'Account not exist! make sure you have written your account correctly.'
                
                return render(request,'codevalidation.html',{"err":err})
        return render(request,'codevalidation.html')

def saveInfo(request):
        if request.method=='POST':
            username = request.POST.get('firstname')
            userlastname = request.POST.get('lastname')
            useremail = request.POST.get('email')
            useraccount_type = request.POST.get('account_type')
            if username=="" and userlastname=="" and useremail=="" and useraccount_type !="free" and useraccount_type != "premium":
                res="Form can't be emty!!!"
                engine1 = pyttsx3.init()
                engine1.say("emty field is unacceptable")
                engine1.runAndWait()
                return render(request,"registrationForm.html",{"res":res})
            else:
                length=6
                characters = string.ascii_letters + string.digits

                random_code=''.join(random.choice(characters) for i in range(length))
                info = userInformation(name=username,lastname=userlastname,email=useremail,account_type=useraccount_type,code=random_code)
                info.save()
                response="Account created successfully!"
                label = "Use this One Time Password (OTP) to access the App"
                engine=pyttsx3.init()
                voices = engine.getProperty("voices")
                engine.setProperty("voice",voices[1].id)
                engine.setProperty("rate",180)
                engine.say("Account Created Succefully. use the code above to access the app.")
                engine.runAndWait()
                return render(request,"registrationForm.html",{"code":random_code,"response":response,"label":label})
        
                
        
           
     
    
def user(request):
    users=userInformation.objects.all()
    context={'users':users}
    return render(request,'userlist.html',context)     
        

# def show(request):
#     return render(request,'app.html')


evan="Philip voice"
lovelyn="Lovelyn voice"


def speak(request):
    voice1=request.GET['evanvoice']
    engine = pyttsx3.init()
    engine.setProperty("rate",130)
    voices = engine.getProperty("voices")
    if voice1 == evan:
        voice1=evan
        engine.setProperty("voice",voices[0].id)
        text = request.GET['textvalue']
        engine.say(text)
        engine.runAndWait()
        return render(request,'app.html',{"evan":evan,"lovelyn":lovelyn,"voice":voice1})
        
    else:
        voice1=lovelyn
        engine.setProperty("voice",voices[1].id)
        text = request.GET['textvalue']
        engine.say(text)
        engine.runAndWait()
        return render(request,'app.html',{"evan":evan,"lovelyn":lovelyn,"voice":voice1})
   
def admincheck(request):

    if request.method=="POST":
         password=request.POST.get('pass')
         if password=="johnsen21":
             return redirect('userlist')
         
         else:
              error_response="Invalid code !!!"
              return render(request,'admin_verification.html',{"error_response":error_response})
    return render(request,"admin_verification.html")
    
def gotologin(request):
    if request.method=="POST":
        if 'btn' in request.POST:
            return redirect('login')
    
    




    








