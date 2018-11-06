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
    title=models.CharField(max_length=120)
    location=models.CharField(max_length=20)
    travelers_that_have_booked=models.IntegerField(default=0)
    image=models.ImageField()
    price=models.IntegerField(default=0)
    bookbefore=models.DateField()
    

    def __str__(self):
        return self.title 


class GuaranteedSafaris(models.Model):
    SafariPackages=(
        ('Excursions-lakenakuru'),
        ('Excursions-lakenaivasha'),
        ('Excursions-nairobiexcursions'),
    )

    bookbefore=models.DateField()
    Season=(
        ('low'),
        ('high'),
        ('peak')
    )
    hotelstar=(
        ('2 star'),
        ('3 star'),
        ('4 star')
    )
    peoplebooked=models.IntegerField(default=0)



