from django.shortcuts import render,redirect , reverse
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User , auth
from hos.models import doctors , appointments, patient , receptionist , DaySchedule
from hos.models import receptionist
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random
from django.urls import reverse
# Create your views here.
#-----------------------------------------LOGIN-----------------------------------------
def index(request):
    if request.method == 'POST':
        type=request.POST['type']
        username = request.POST['email']
        passw = request.POST['password']
        print(type)
        user= auth.authenticate(username=username ,password=passw)
        print('authenticated',user is not None)
        if type =='patient' and user is not None:
            if patient.objects.filter(id=username).exists():
                print("user is not none")
                auth.login(request,user)
                return redirect('/patient/')
            else:
                messages.info(request,'Patient Does Not Exist')
                return redirect('/accounts/login')
        elif type =='doctor' and user is not None:
            if doctors.objects.filter(id=username):
                print("sdf")
                auth.login(request,user)
                return redirect('/doctor')
            else:
                messages.info(request,'Doctor Does Not Exist')
                return redirect('/accounts/login')
        elif type=="receptionist" and user is not None :
            if receptionist.objects.filter(recep_id=username):
                auth.login(request,user)
                return redirect('/receptionist')
            else:
                messages.info(request,'Receptionist Does Not Exist')
                return redirect('/accounts/login')
        else:
            print('else')
            messages.info(request,'invalid credentials') 
            return redirect('/accounts/login')

    else:
        return render(request , 'login.html')




#--------------------------------------REGISTRATION-------------------------------------------    



def logout(request):
    print('logout me')
    auth.logout(request)
    return redirect('/')

def patient_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_nam = request.POST['last_name']
        username = request.POST['email']
        password1 = request.POST['password']
        password = request.POST['password1']
        phn_no = request.POST['phn_no']
        gender = request.POST['gender']
        age=request.POST['age']
        
        #lol.append(username)
        if(password == password1):
            print("password match")
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'E-Mail Exists try different one..!!')
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(username=username , password=password,first_name=first_name , last_name=last_nam)
                patient(id=username,first_name=first_name,last_name=last_nam,phone_no=phn_no,gender=gender,age=age).save()
                user.save();
                return redirect('/patient/') 
        else:
            messages.info(request,'password must match')
            return redirect('/accounts/register')


    return render(request,'register.html')







































'''def login(request):
    if request.method == 'POST':
        print("login")
        e = request.POST['email']
        passw = request.POST['password']
        type = request.POST['type']
        print(e , passw , type)
        user= auth.authenticate(username=e ,password=passw)
        user1 = doctors.objects.filter(doctor_email = e)
        user2 = receptionist.objects.filter(recep_id = e)
        print(user, user1,user2)
        if user is not None or user1 is not None or user2 is not None:
            if User.objects.filter(username=e).exists():
                auth.login(request,user)
                return redirect('patient/')
            elif type == "doctor" and User.objects.filter(username=e).exists(): 
                if doctors.objects.filter(doctor_email = e).exists():
                    auth.login(request,user)
                    return redirect('doctor/')
                else:
                    messages.info(request , "Account doesn't exists")
                    return render(request, 'login.html')
            elif type == "receptionist" and User.objects.filter(username=e).exists():
                if receptionist.objects.filter(recep_id = e).exists():
                    auth.login(request,user)
                    return redirect('receptionist/')
                else:
                    messages.info(request,'Account doesnt exists')    
                    return render(request , 'login.html')
            else:    
                messages.info(request , "Account doesn't exists")
                return render(request, 'login.html')
           
        else:
            #print("else me")
            messages.info(request , "invalid credentials")
            return redirect('../login') 
       
    else:
        
        return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_nam = request.POST['last_name']
        username = request.POST['email']
        password1 = request.POST['password']
        password = request.POST['password1']
        phn_no = request.POST['phn_no']
        gender = request.POST['gender']
        type = request.POST['type']
        
        #lol.append(username)
        if(password == password1):
            print("password match")
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'E-Mail Exists try different one..!!')
                return redirect(reverse('../register'))

            else:
                if type == "doctor": 
                    id = random.randint(11111,999999)
                    user = User.objects.create_user(username=username , password=password,first_name=first_name , last_name=last_nam)
                    doctor=doctor(id=id,name = first_name+last_name,email=email, password=password,department=department,gender=gender)
                    docter.save();
                elif type == "receptionist":
                    if (User.objects.filter(recep_id = username).exists()):
                        hospital_id = hospital.objects.filter(hospital_name=hospital_name).hospital_id
                        receptionist = recepionist.objects.create_user(recep_id=username , password=password,recep_name=recep_name , hospital_name=hospital_name , hospital_id=hospital_id)
                        receptionist.save()
                        return redirect('receptionist/')
                    else:
                        messages.info(request,'Account doesnt exists')    
                        return render(request , 'login.html')
                user = User.objects.create_user(username=username , password=password,first_name=first_name , last_name=last_nam)
                user.save();
                return redirect('login/')
        else:
            messages.info(request, 'Password must match..!!')
            return redirect('../register')
    else:
        print("register else")
        return render(request,'register.html')






def verification(request):
    if request.method == 'POST':
        number = request.POST['otp']
        if number==otp:
            user = User.objects.create_user(username=username , password=password,first_name=first_name , last_name=last_nam)
            user.save();
            return redirect('/')
        else:
            message.info(request , 'verification failed')
    else:
        otp=random.randint(111111,999999)
        email = lol[0]
        print(email)
        subject , message1 , from_email , recipient_list = 'E-mail verficiation' , ('your one time password is' + str(otp)) , settings.EMAIL_HOST_USER , [email]
        send_mail(subject,
            message1,
            from_email,
            recipient_list,
            fail_silently=False, auth_user=None, auth_password=None,
            connection=None, html_message=None)
        lol = []
        return render(request , 'verification.html')
        '''