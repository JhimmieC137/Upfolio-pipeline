from django.urls import path 
from .import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('about', views.about_upfolio, name='about_upfolio'),
    path('team', views.team, name='team'),
    path('job-vacancies', views.job_vacancies, name='job_vacancies'),
    path('internships', views.internships, name='internships'),
    path('grants', views.grants, name='grants'),
    path('online-courses', views.online_courses, name='online_courses'),
    path('scholarships', views.scholarships, name='scholarships'),
    path('fellowships', views.fellowships, name='fellowships'),
    path('competitions', views.competitions, name='competitions'),
    path('volunteering', views.volunteering, name='volunteering'),
    path('fully-funded-programs', views.fully_funded_programs, name='fully_funded_programs'),
    path('opportunities', views.daily_opportunities, name='daily_opportunities'),
    path('programs', views.programs, name='programs'),
    path('projects', views.projects, name='projects'),
    path("join-our-community", views.mailing_list_form, name='mailing_list_form'),
    path("contact-us", views.contact_us, name='contact_us'),
    path('uip-placements', views.uip_placements, name='uip_placements'),
    path('annivesary-picnics', views.annivesary_picnics, name='annivesary_picnics'),
    path('gallery-of-doings', views.gallery_of_doings, name='gallery_of_doings'),
    path('uip-certificates/<int:code>', views.uip_certificates, name='uip-certificates'),
]