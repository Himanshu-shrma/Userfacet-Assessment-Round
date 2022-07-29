
import json
from datetime import date, datetime, timedelta
from django import http
import requests
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import scheduled_classes
from .forms import StudentSlotForm
import smtplib

# Create your views here.
def home(request):
    timings=requests.get('https://raw.githubusercontent.com/rohit-userfacet/userfacet-backend-testcase/main/teacher_availability.json').json()
    available_days=timings['availability'].keys()
    if request.method=="POST":
        form=StudentSlotForm(request.POST)
        #checking validity of the form Submitted
        if form.is_valid():
            week_day=form.cleaned_data['weekday'].lower()
            start_time=form.cleaned_data['start_time']
            end_time=form.cleaned_data['end_time']

            #checking if teacher teaches on the submitted data's day

            if week_day in available_days:
                temp=form.save(commit=False)
                temp.teacher_name=timings["full_name"]
                booked_slot=scheduled_classes.objects.filter(weekday=week_day,start_time__gte=start_time,end_time__lte=end_time).order_by('-class_date')
                days={
                    "monday":0,
                    "tuesday":0,
                    "wednesday":0,
                    "thursday":0,
                    "friday":0,
                    "saturday":0,
                    "sunday":0,
                }

                #checking for the next available day according to the database

                if booked_slot:
                    last_date=booked_slot.first().class_date
                    temp.class_date= (last_date+timedelta(days=7))
                    temp.save()
                else:
                    temp.class_date= (date.today()+timedelta(days=(days[week_day]-date.today().weekday())%7))
                    temp.save()
                data={
                        "slot_confirmed": "true",
                        "weekday": week_day,
                        "start_time": str( start_time),
                        "end_time": str(end_time),
                        "date": str(temp.class_date)
                    }
                #call for sending the email
                #send_email(temp,timings)
                
                return HttpResponse(json.dumps(data))
            else:
                data={
                    "slot_confirmed": "false",
                    "reason": "teacher is not available on this day"
                    }
                return HttpResponse(json.dumps(data))
    else:
        form=StudentSlotForm
        return render(request,'Solution/home.html',{
            'form':form,
        })



def send_email(shared_form,timings):
    message_for_mail="""Congratulation {student_name},Your Class has been booked\n
                        Date-{date}\n
                        Start Time-{start_time} to
                        End Time- {end_time}""".format(student_name=shared_form.name,date=str(date),start_time=str(shared_form.start_time),end_time=str(shared_form.end_time))
    sender=timings["email"]
    receiver=shared_form.email
    password="Password of the sender's email"
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(sender,password)
    server.sendmail(sender, receiver, message_for_mail)
    server.quit()