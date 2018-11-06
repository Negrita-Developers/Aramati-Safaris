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
    Enter_Safari_Package=models.CharField(choices=SafariPackagesChoices, max_length=20, default="title")
    book_before=models.DateField()
    SeasonChoices=(
        ('lw','low'),
        ('hi', 'high'),
        ('pk','peak'),
    )
    Enter_Season=models.CharField(choices=SeasonChoices, max_length=20, default="seasons") 
    hotel_star=(
        ('2', '2 star'),
        ('3','3 star'),
        ('4', '4 star')
    )
    Enter_Hotel_Star=models.CharField(choices=hotel_star, max_length=20, default="hotels")
    people_booked=models.IntegerField(default=0)



