from django.db import models
from django.urls import reverse

# Create your models here.
class Profiles(models.Model):
    name=models.CharField(max_length=120)
    email =models.CharField(max_length=40, blank=False, default='my email default')
    location = models.CharField(max_length=40, default='my location default')
    
    def __unicode__(self):
        return self.name


class JoinGroup(models.Model):
    title=models.CharField(max_length=120, default=0)
    location=models.CharField(max_length=20)
    travelers_that_have_booked=models.IntegerField(default=0)
    # image=models.ImageField(blank=False)
    price=models.IntegerField(default=0)
    bookbefore=models.DateField()
    

    def __str__(self):
        return self.title 


class GuaranteedSafaris(models.Model):
    SafariPackagesChoices=(
        ('Excursions-lakenakuru', 'Excursions-lakenakuru'),
        ('Excursions-lakenaivasha' ,'Excursions-lakenaivasha'),
        ('Excursions-nairobiexcursions' ,'Excursions-nairobiexcursions'),
        ('2dyabedare' ,'2 days - aberdare'),
        ('2dyamboseli' ,'2 days - amboseli'),
        ('2dynakuru' ,'2 days - nakuru'),
        ('2dynaivasha' ,'2 days - naivasha'),
        ('2dysweetwaters' ,'2 days - sweetwaters'),
        ('3dyamboseli' ,'3 days - amboseli'),
        ('3dymaasaimara' ,'3 days - maasaimara '),
        ('3dynakuru' ,'3 days - nakuru'),
        ('3dysamburu' ,'3 days - samburu'),
        ('3dysweetwaters' ,'3 days - sweetwaters'),
        ('4dymaranakuru' ,'4 days - maranakuru'),
        ('5dyamboseli' ,'5 days - amboseli'),

    )
    Enter_Safari_Package=models.CharField(choices=SafariPackagesChoices, max_length=50, default="title")
    book_before=models.DateField()
    price1=models.IntegerField(default=0)
    price2=models.IntegerField(default=0)
    price3=models.IntegerField(default=0)
    price4=models.IntegerField(default=0)
    price5=models.IntegerField(default=0)
    price6=models.IntegerField(default=0)
    price7=models.IntegerField(default=0)
    hotel_star=(
        ('2', '2 star'),
        ('3','3 star'),
        ('4', '4 star')
    )
    Enter_Hotel_Star=models.CharField(choices=hotel_star, max_length=20, default="hotels")
    people_booked=models.IntegerField(default=0)
    show=models.BooleanField(blank=True)

    def __str__(self):
        return self.Enter_Safari_Package
