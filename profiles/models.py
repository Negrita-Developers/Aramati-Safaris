from django.db import models
from django.urls import reverse
import datetime as date
from datetime import datetime; datetime.now()


# Create your models here.
class Packages(models.Model):
    name=models.CharField(max_length=30, unique=True, default="title") 

    def __str__(self):
        return self.name 

class JoinedSafaris(models.Model):
   
    package=models.ForeignKey(Packages)
    Location=models.CharField(max_length=15, default="location")
    book_before=models.DateTimeField(default=datetime.now)
    depature_date=models.DateTimeField(default=datetime.now) 
    Season=(
        ('Low Season', 'Low Season'),
        ('High Season','High Season'),
        ('Peak Season','Peak Season'),
    )
    Season=models.CharField(choices=Season, max_length=20, default="season")
    Hotel_Star=(
        ('2 star', '2 star'),
        ('3 star','3 star'),
        ('4 star','4 star'),
        ('Treetops ','Treetops Aberdare'),
        ('Ark ','Ark Aberdare')
    )
    Hotel_Star=models.CharField(choices=Hotel_Star, max_length=20, default="hotelstar")
    Accomodation=(
        ('bg', 'Budget'),
        ('lx','Luxury')
    )
    Accomodation=models.CharField(choices=Accomodation, max_length=20, default="accomodation")
    people_booked=models.IntegerField(default=0)

    def __str__(self):
        return self.package.name



class LowSeason(models.Model):
    package=models.ForeignKey(Packages)
    price1=models.IntegerField(default=0)
    price2=models.IntegerField(default=0) 
    price3=models.IntegerField(default=0)
    price4=models.IntegerField(default=0)
    price5=models.IntegerField(default=0)
    price6=models.IntegerField(default=0)
    price7=models.IntegerField(default=0)
    SRS=models.IntegerField(default=0, blank=True)

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
    SRS=models.IntegerField(default=0, blank=True)

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
    SRS=models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.package.name 

 



   
