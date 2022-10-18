# from distutils.command.upload import upload
# from optparse import Option
# from xml.dom.xmlbuilder import Options
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class Info(models.Model):
    heading = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    about = models.CharField(max_length=100, null=True)
    

class Images(models.Model):
    img = models.ImageField(upload_to= 'media')
    description = models.CharField(max_length=200, null=True) 

class Team(models.Model):
    team = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100, null=True)
    name = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to= 'media')
    
class Subscribe(models.Model):
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField()
    # birthday = models.CharField(max_length=15, null=True)


class Daily_Opportunie(models.Model):
    name = models.CharField(max_length=30, null=False)
    pic = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)

class Job_Vacancies(models.Model):
    name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='media')
    role = models.CharField(max_length=100, null=True)
    job_description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    id_name = models.CharField(max_length=500, null=True)
    
class Internship(models.Model):
    name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='media')
    role = models.CharField(max_length=100, null=False)
    job_description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    
class Grant(models.Model):
    name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='statics')
    title = models.CharField(max_length=100, null=False)
    job_description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    
class Online_course(models.Model):
    name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='media')
    subject = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    
class Scholarship(models.Model):
    organisation_name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    
class Fellowship(models.Model):
    name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='media')
    description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)

class Fully_Funded_Program(models.Model):
    organisation = models.CharField(max_length=150, null=False)
    name = models.CharField(max_length=150, null=False)
    pic = models.ImageField(upload_to='media')
    description = models.TextField(max_length=30000, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    
class Competition(models.Model):
    organisation_name = models.CharField(max_length=50, null=False)
    pic = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, null=False)
    link = models.CharField(max_length=300, null=False)
    deadline = models.CharField(max_length=300, null=True)
    
class Information_session(models.Model):
    theme = models.TextField(max_length=100, null=False)
    venue = models.TextField(max_length=100, null=True)
    guests = models.TextField(max_length=200, null=False)
    date = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=500, null=False)
    link_caption = models.CharField(max_length=500, null=True)
    description = models.TextField(max_length=700, null=True)
    flier_1 = models.ImageField(upload_to='media', null=True)
    flier_2 = models.ImageField(upload_to='media', null=True)
    flier_3 = models.ImageField(upload_to='media', null=True)
    flier_4 = models.ImageField(upload_to='media', null=True)
    flier_5 = models.ImageField(upload_to='media', null=True)

class Capacity_development(models.Model):
    theme = models.TextField(max_length=100, null=False)
    venue = models.TextField(max_length=100, null=True)
    guests = models.TextField(max_length=200, null=False)
    date = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=500, null=True)
    link_caption = models.CharField(max_length=500, null=True)
    description = models.TextField(max_length=700, null=True)
    flier_1 = models.ImageField(upload_to='media', null=True)
    flier_2 = models.ImageField(upload_to='media', null=True)
    flier_3 = models.ImageField(upload_to='media', null=True)
    
class Partners(models.Model):
    img = models.ImageField(upload_to='media', null=False)


class Articles(models.Model):
    title = models.TextField(max_length=100, null=False)
    link = models.CharField(max_length=500, null=False)
    flier_1 = models.ImageField(upload_to='media', null=True)
    
    
class Projects(models.Model):
    theme = models.TextField(max_length=100, null=False)
    description1 = models.TextField(max_length=500, null=True)
    description2 = models.TextField(max_length=500, null=True)
    description3 = models.TextField(max_length=500, null=True)
    link = models.CharField(max_length=500, null=False)
    caption = models.CharField(max_length=500, null=True)
    flier_1 = models.ImageField(upload_to='media', null=True)
    

    