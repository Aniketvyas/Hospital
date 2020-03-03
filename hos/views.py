from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse ,JsonResponse
from .models import appointments , doctors , DaySchedule , patient , receptionist
from django.contrib.auth.models import User , auth 
from django.core.mail import send_mail
from django.conf import settings
import random 
import datetime as dt
from datetime import *
from django.contrib import messages
import json
from django.core import serializers
from django.conf import settings
# Imported for backwards compatibility and for the sake
# of a cleaner namespace. These symbols used to be in
# django/core/mail.py before the introduction of email
# backends and the subsequent reorganization (See #10355)





#from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'test.html')

def about(request):
    print(request,"hell" ,id)
    return render(request,'about.html')

def services(request):
    print(request,"hell" ,id)
    return render(request,'services.html')
def appointment(request):
    return render(request,'appointment.html')
def lab(request):
    return render(request,'lab_reports.html')
def blood(request):
    return render(request,'blood_availability.html')
def medical(request):
    return render(request,'medical_certificate.html')
def contact(request):
    return render(request,'contact.html')


def red(request,id):
    print(request,"hello",id)
    if id==1:
        return redirect('/')
    elif id==2:
        #return HttpResponse("hello")
        return redirect('/about')
    elif id==3:
        return redirect('/services')
    elif id==4:
        return redirect('/appointment')
    elif id==5:
        return redirect('/lab')
    elif id==6:
        return redirect('/blood')
    elif id==7:
        return redirect('/medical')
    elif id==8:
        return redirect('/contact')
   
    elif id==9:
        return render(request,'receptionist.html')
   
def index1(request):
    appointment = appointments.objects.all().count()
    docto = doctors.objects.all().count()
    return render(request,'index.html',{'appointment':appointment,'docto':docto})



def book(request):
    if request.method == 'POST':
        app_id=random.randint(1000,9999)
        name = request.POST['name']
        age = request.POST['age']
        location= request.POST['location']
        pincode = request.POST['pincode']
        a = request.POST['email']
        gender = request.POST['gender']
        phn_no = request.POST['phn_no']
        slot_date = request.POST['date']
        doctor_name=request.POST['doc_name']
        request.session['doctor_name']=doctor_name
        request.session['slot_date']=slot_date
        request.session['patient_appointment_id']=app_id
        datetimeobject= datetime.strptime(slot_date,'%d-%m-%Y')
        slot_date = datetimeobject.strftime('%Y-%m-%d')
        c_date = dt.datetime.now().strftime('%d-%m-%Y')
        c_date= datetime.strptime(c_date,'%d-%m-%Y')
        now = datetime.now()
        doc_id=""
        print("else me")
        print(a,type(a))
        doc_id = doctors.objects.filter(name=doctor_name).values('id')
        for i in doc_id :
            doc_id = i['id']
        print(doc_id)
        if gender in ['m','f','M','F'] and datetimeobject>=c_date:
            slot_date = datetimeobject.strftime('%Y-%m-%d')
            c_date = dt.datetime.now().strftime('%Y-%m-%d')
            db=appointments(
                doctor_id=doc_id,
                pincode=pincode,
                patient_appointment_id=app_id,
                patient_phone=phn_no ,
                patient_email = a,
                patient_name = name,
                patient_age=age,
                patient_gender=gender,
                slot_date=slot_date,
                created_at=c_date,
                udated_at=c_date)
            print("migration")
            db.save()
            print("db saved")
                
            return redirect("patient/timeslot/50",{'doc':doctor_name})
                        #counter=0

            #send_mail=(subject,message,from_email,to_list,fail_silently=True)
        else:
            docs= doctors.objects.all()   
            print(docs) 
            messages.info(request , "invalid credentials")
            return render(request,'booking.html' , {'docs':docs})
            
   

        #send_mail=(subject,message,from_email,to_list)
      
    else:   
        docs= doctors.objects.all()   
        print(docs)  
        return render(request,'booking.html', {'docs' : docs})

def locate(request):
    if request.method =="POST":
        city = request.POST['city']
        code = request.POST['pincode']
        docs = doctors.objects.filter(location=city,pincode=code)
        return render(request,'dash_users.html',{'docs':docs})
    else:
        return render(request,'dash_users.html')

def track(request):
    p = patient.objects.filter(id=request.user)
    if p.exists() :
        return redirect('/patient')
    else:
        messages.error(request,'You Must Login to continue')
        return redirect('/accounts/login')


    

def timeslot(request,id):
    print(id)
    docs = request.session.get('doctor_name')
    da = request.session.get('slot_date')
    id1 = request.session.get('patient_appointment_id')
    print("id1",id1)
    datetimeobject= datetime.strptime(da,'%d-%m-%Y')
    da = datetimeobject.strftime('%Y-%m-%d')

    apptime = DaySchedule.objects.filter(doctor_name=docs)
    doc = doctors.objects.filter(name=docs)
    for i in doc:
        x = i.id
    time1 = dt.time(11,00,00)
    time = dt.time(2,00,00)
    time.strftime("%H-%M-%S")
    u = request.user.username
    print("u",u)
    print("ferg",appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time1))
    if id:
        if id==1:
            time = dt.time(9,1,00)
            time = time.strftime("%H:%M:%S")
            print(time)
            print(time,type(time))
            if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                print("user",u)
                if patient.objects.filter(id=u):
                    return redirect('/patient')
                elif receptionist.objects.filter(recep_id=u):
                    return redirect('/receptionist')
                else:
                    return redirect('/')
        elif id==2:
            time = dt.time(9, 15, 00)
            time.strftime("%H-%M-%S")
            print(time)
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u):
                    return redirect('/patient')
                    
                else:
                   return redirect('/receptionist')
        elif id==3:
            time = dt.time(9,30,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                print("entry Done")
                if patient.objects.filter(id=u):
                    return redirect('/patient')
                else:
                    return redirect('/receptionist')
        elif id==4:
            time = dt.time(9,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==5:
            time = dt.time(10,00,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==6:
            time = dt.time(10,15,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==7:
            time = dt.time(10,30,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==8:
            time = dt.time(10,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==9:
            time = dt.time(11,00,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==10:
            time = dt.time(11,15,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==11:
            time = dt.time(11,30,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==12:
            time = dt.time(11,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==13:
            time = dt.time(13,30,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==14:
            time = dt.time(13,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==15:
            time = dt.time(14,00,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==16:
            time = dt.time(14,15,00)
            time.strftime("%H-%M-%S")
            print(time)

            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==17:
            time = dt.time(14,30,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==18:
            time = dt.time(14,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id == 19:
            time = dt.time(15,00,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                print("if")
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                print("esle")
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==20:
            time = dt.time(15,15,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==21:
            time = dt.time(15,30,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==22:
            time = dt.time(15,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==23:
            time = dt.time(17,00,00)
            time.strftime("%H-%M-%S")
            print("time",time)
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==24:
            time = dt.time(17,15,00)
            time.strftime("%H-%M-%S")
            print(time)
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id ==25:
            time = dt.time(17,30,00)
            time.strftime("%H-%M-%S")
            print(time)
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==26:
            time = dt.time(17,45,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==27:
            time = dt.time(18,00,00)
            time.strftime("%H-%M-%S")
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==28:
            time = dt.time(19,15,00)
            time.strftime("%H-%M-%S")
            time = time.strftime("%H-%M-%S")
            print(time)
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        elif id==29:
            time = dt.time(19,30,00)
            time.strftime("%H-%M-%S")
            print(time)
            if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
                messages.info(request,'time is already taken')
                return redirect("/patient/timeslot/50")
            else:
                appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
                if patient.objects.filter(id=u).exists():
                    return redirect('/patient')
             
                else:
                    return redirect('/receptionist')
        else:
            return render(request,'timeslot.html')



def dashboard(request):
    return render(request,'dash_index.html')


def patient_dash(request):
    docs = doctors.objects.all()
    u=request.user.username     
    print(u)
    previous = appointments.objects.filter(patient_email=u).order_by('-created_at')
    print(previous)
    return render(request,'patient/dash_users.html',{'docs':docs,'appointment':previous})

def prescription(request,id):
    if id:
        print(id)
        pres = appointments.objects.filter(patient_appointment_id=id)
    return render(request,'patient/view_prescription.html',{'pres':pres})


#------------------------------------PATIENT DASHBOARD----------------------------------
def receptionists(request):
    appointment = appointments.objects.filter(slot_date = datetime.now().strftime('%Y-%m-%d'),status="pending")
    print(appointment)

    return render(request,'dash_index.html',{'apps':appointment})



#------------DOCTOR DASHBOARD ___________________________

def doc_dash(request):
    appointment = appointments.objects.filter(slot_date = datetime.now().strftime('%Y-%m-%d'),status="pending")
    print(appointment)

    return render(request , 'doc_dash.html',{'apps':appointment})

def appointment_doctor_view(request,id):
    id=int(id)
    print(id,type(id))
    if request.method == "POST":
        med = request.POST['medicine']
        print(med,type(med))
        appointments.objects.filter(patient_appointment_id=id).update(prescription=med,status="done")
        return redirect('/doctor')
    else:
        app=appointments.objects.filter(patient_appointment_id=id)
        return render(request,'patient/prescription.html',{'apps':app})


def check(request):
    us = request.user.username
    if patient.objects.filter(id=us).exists():
        return redirect('/patient')
    elif doctors.objects.filter(id=us).exists():
        return redirect('/doctor')
    elif receptionist.objects.filter(recep_id=us).exists():
        return redirect('/receptionist')
    else:
        return redirect('/')

#<----------------------Receptionist copied-------------------------->
'''def receptionist(request):
    return render(request, "receptionist/dashboard.html", {})



def receptionist_dev(request):
    vdatetime = datetime.datetime.now() - datetime.timedelta(hours=4)
    vtime = vdatetime.time()
    vdate = vdatetime.date()
    userName = u
    obj = Appointment.objects.filter(date__gte=vdate, startTime__gte=vtime, status_id=1)

    return render(request, "receptionist/receptionist_dev.html", {'object': obj, 'userName': userName})



def receptionist_appointment_history(request):
    vdatetime = datetime.datetime.now() - datetime.timedelta(6 * 365 / 12)
    vtime = vdatetime.time()
    vdate = vdatetime.date()
    userName = u
    obj = Appointment.objects.filter(date__gte=vdate,status__in=(1,3,4)).order_by('-date')
    context = {
        'object': obj,
        'userName': userName,
        'title': "Appointments"
    }

    return render(request, "receptionist/appointment_history.html", context)


def receptionist_appointment_history_archive(request):
    vdatetime = datetime.datetime.now() - datetime.timedelta(6 * 365 / 12)
    vtime = vdatetime.time()
    vdate = vdatetime.date()
    userName = u
    obj = Appointment.objects.all().order_by('-date')
    context = {
        'object': obj,
        'userName': userName,
        'title': "Archived Appointments"
    }

    return render(request, "receptionist/appointment_history.html", context)

'''

#<-------------------------------------Receptionist ------------------------------------>

