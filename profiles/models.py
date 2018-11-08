from django.db import models
from django.urls import reverse
import datetime as date
from datetime import datetime; datetime.now()


# Create your models here.

class JoinGroup(models.Model):
    title=models.CharField(max_length=120, default="title")
    location=models.CharField(max_length=20)
    travelers_that_have_booked=models.IntegerField(default=0)
    # image=models.ImageField(blank=False)
    price=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class JoinedSafaris(models.Model):
    SafariPackagesChoices=(
        ('ExNk', 'Excursions-lakenakuru'),
        ('ExNv' ,'Excursions-lakenaivasha'),
        ('ExNai' ,'Excursions-nairobiexcursions'),
        ('2dyab' ,'2 days - aberdare'),
        ('2dyam' ,'2 days - amboseli'),
        ('2dynk' ,'2 days - nakuru'),
        ('2dynv' ,'2 days - naivasha'),
        ('2dysw' ,'2 days - sweetwaters'),
        ('3dyam' ,'3 days - amboseli'),
        ('3dyma' ,'3 days - maasaimara '),
        ('3dynk' ,'3 days - nakuru'),
        ('3dysa' ,'3 days - samburu'),
        ('3dysw' ,'3 days - sweetwaters'),
        ('4dymank' ,'4 days - maranakuru'),
        ('5dyam' ,'5 days - amboseli'),
    )
    Enter_Safari_Package=models.CharField(choices=SafariPackagesChoices, max_length=20)
    book_before=models.DateTimeField(default=datetime.now)
    depature_date=models.DateTimeField(default=datetime.now) 
    Accomodation=(
        ('bg', 'Budget'),
        ('lx','Luxury')
    )
    Accomodation=models.CharField(choices=Accomodation, max_length=20, default="accomodation")
    people_booked=models.IntegerField(default=0)

    def __str__(self):
        return self.Enter_Safari_Package 

class Packages(models.Model):
    name=models.CharField(max_length=30, unique=True) 

    def __str__(self):
        return self.name 

class LowSeason(models.Model):
    package=models.ForeignKey(Packages)
    price1=models.IntegerField(default=0)
    price2=models.IntegerField(default=0) 
    price3=models.IntegerField(default=0)
    price4=models.IntegerField(default=0)
    price5=models.IntegerField(default=0)
    price6=models.IntegerField(default=0)
    price7=models.IntegerField(default=0)

    def __str__(self):
        return self.package.name

class HighSeason(models.Model):
    package=models.ForeignKey(Packages)
    price1=models.IntegerField(default=0)
    price2=models.IntegerField(default=0) 
    price3=models.IntegerField(default=0)
    price4=models.IntegerField(default=0)
    price5=models.IntegerField(default=0)
    price6=models.IntegerField(default=0)
    price7=models.IntegerField(default=0)

    def __str__(self):
        return self.package.name


class PeakSeason(models.Model):
    package=models.ForeignKey(Packages)
    price1=models.IntegerField(default=0)
    price2=models.IntegerField(default=0) 
    price3=models.IntegerField(default=0)
    price4=models.IntegerField(default=0)
    price5=models.IntegerField(default=0)
    price6=models.IntegerField(default=0)
    price7=models.IntegerField(default=0)

    def __str__(self):
        return self.package.name

 



   
