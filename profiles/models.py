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
        ('Excursions - Lake Nakuru', 'Excursions-lakenakuru'),
        ('Excursions - Lake Naivasha' ,'Excursions-lakenaivasha'),
        ('Excursions - Nairobi Excursions' ,'Excursions-nairobiexcursions'),
        ('2 DAYS ABERDARE NATIONAL PARK' ,'2 days - aberdare'),
        ('2 DAYS AMBOSELI SAFARI' ,'2 days - amboseli'),
        ('2 DAYS LAKE NAKURU NATIONAL PARK' ,'2 days - nakuru'),
        ('2 DAYS NAIVASHA SAFARI' ,'2 days - naivasha'),
        ('2 DAYS MAASAI MARA SAFARI' ,'2 DAYS MAASAI MARA SAFARI'),
        ('2 DAYS SWEETWATERS/ OL PEJETA CONSERVANCY SAFARI' ,'2 days - sweetwaters'),
        ('3 DAYS AMBOSELI SAFARI' ,'3 days - amboseli'),
        ('3 DAYS MAASAI MARA SAFARI' ,'3 days - maasaimara '),
        ('3 DAYS LAKE NAKURU NATIONAL PARK' ,'3 days - nakuru'),
        ('3 DAYS SAMBURU SAFARI' ,'3 days - samburu'),
        ('3 DAYS SWEETWATERS/ OL PEJETA CONSERVANCY SAFARI' ,'3 days - sweetwaters'),
        ('4 DAYS MAASAI MARA/NAKURU SAFARI' ,'4 days - maranakuru'),
        ('5 DAYS AMBOSELI - NAKURU - MARA SAFARI' ,'5 days - amboseli'),
    )
    Enter_Safari_Package=models.CharField(choices=SafariPackagesChoices, max_length=40)
    Location=models.CharField(max_length=15, default="location")
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

 



   
