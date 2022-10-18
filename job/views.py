# from tkinter import Image
# from email import message
# from email.mime import image
# from tkinter import image_names
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import request
from django.http import HttpResponseRedirect
from .models import Articles, Capacity_development, Info, Information_session, Partners, Projects, Team, Daily_Opportunie, Job_Vacancies, Internship, Scholarship, Grant, Fully_Funded_Program, Fellowship, Online_course, Competition
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .forms import SubscriptionForm
# import requests
import time
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    information = Info.objects.all()
    team = Team.objects.all()
    icon = Partners.objects.all()
    programs = Information_session.objects.all()
    cap_dev = Capacity_development.objects.all()
    projects = Projects.objects.all()
    articles = Articles.objects.all()
    
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        
        # send mail command
        send_mail(
            message_subject, # subject
            "Hi, i'm " + message_name + '\r\n' + message, # message
            message_email, # sender's email
            ['theupfolio@gmail.com'], # addressed to email
            fail_silently=False)
        return render(request, 'index.html', {'message_name':message_name, 'information' : information, 'team' : team, 'icon':icon, 'programs':programs, 'cap_dev':cap_dev, 'projects':projects, 'articles':articles})
    else:
        return render(request, 'index.html', {'information' : information, 'team' : team, 'icon':icon, 'programs':programs, 'cap_dev':cap_dev, 'projects':projects, 'articles':articles})

def about_upfolio(request):
    Information = Info.objects.all()
    team = Team.objects.all()
    return render(request, 'about_upfolio.html', {'Information' : Information, 'team' : team})

def team(request):
    return render(request, 'team.html')

def job_vacancies(request):
    jobs = Job_Vacancies.objects.all() 
    return render(request, 'job_vacancies.html', {'jobs':jobs})

def internships(request):
    jobs = Internship.objects.all() 
    return render(request, 'internships.html', {'jobs':jobs})

def grants(request):
    grants = Grant.objects.all()
    return render(request, 'grants.html', {'grants':grants})

def online_courses(request):
    courses = Online_course.objects.all()
    return render(request, 'online_courses.html', {'courses': courses})

def scholarships(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'scholarships.html', {'scholarships': scholarships})

def fellowships(request):
    fellowships = Fellowship.objects.all()
    return render(request, 'fellowships.html', {'fellowships': fellowships})

def competitions(request):
    competitions = Competition.objects.all()
    return render(request, 'competitions.html', {'competitions': competitions})

def volunteering(request):
    return render(request, 'volunteering.html')

def fully_funded_programs(request):
    fully_funded = Fully_Funded_Program.objects.all()
    return render(request, 'fully_funded_programs.html', {'fully_funded': fully_funded})

def daily_opportunities(request):
    opportunities = Daily_Opportunie.objects.all()
    return render(request, 'daily_opportunities.html', {'opportunities': opportunities})

def programs(request):
    programs = Information_session.objects.all()
    cap_dev = Capacity_development.objects.all()
    return render(request, 'programs.html', {'programs': programs, 'cap_dev':cap_dev})

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects.html', {'projects':projects})

def mailing_list_form(request):
    # submitted = False
    # if request.method == "POST":
    #     form = SubscriptionForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse("mailing_list_form") + '?submitted=True')
    #         # url = 'https://bit.us4.list-manage.com/subscribe/post?u=6626aa149ad8c147094e0d282&amp;id=fbdc92be1f'
    #         # payload = {'Token':'My-Secret_Token', 'EMAIL': request.POST.get("email"), 'FNAME':request.POST.get("first_name"), 'LNAME':request.POST.get("Last_name"), 'MMERGE6':request.POST.get("phone"), 'birthday':request.POST.get("birthday") }
    #         # r = request.POST(url, data = payload)
    #         # if r .status_code == 200:
    #         #     data =r.json()
    #         #     return Response(data, status=status.HTTP_200_OK)
    #         # else:
    #         #     return HttpResponseRedirect(reverse("mailing_list_form") + '?submitted=True')
    #     else:
    #         messages.info(request,'Please enter a valid Phone number')
    #         print("Something's wrong", form)
    # else:
    #     form = SubscriptionForm
    #     if 'submitted' in request.GET:
    #         submitted=True
    #         print("I'm Here!!!")
            
    return render(request, 'mailing_list_form.html')

def contact_us(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        
        # send mail command
        send_mail(
            message_subject, # subject
            "Hi, i'm " + message_name + '\r\n' + message, # message
            message_email, # sender's email
            ['theupfolio@gmail.com'], # addressed to email
            fail_silently=False)
        
        # email = EmailMessage(
        # message_subject,
        # "Hi, i'm " + message_name + '\r\n' + message,
        # from_email='theupfolio@zoho.com',
        # to=['toluwalope.david@gmail.com'],
        # reply_to=[ message_email ]
        # )
        # sent = email.send(fail_silently=False)
        # if sent:
        #     return render(request, 'contact_us.html', {'message_name':message_name})
        return render(request, 'contact_us.html', {'message_name':message_name})
    else:
        return render(request, 'contact_us.html', {})
    
def gallery_of_doings(request):
    return render(request, 'comingsoon.html')

def uip_placements(request):
    return render(request, 'comingsoon.html')

def annivesary_picnics(request):
    return render(request, 'comingsoon.html')

def uip_certificates(request):
    return render(request, '')