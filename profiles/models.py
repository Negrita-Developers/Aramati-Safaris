from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime; datetime.today
from datetime import date 


# Create your models here.
class Packages(models.Model):
    name=models.CharField(max_length=30, unique=True, default="title") 

    def __str__(self):
        return self.name 

    @classmethod
    def search_by_name(cls,search_term):
        search = cls.objects.filter(name__icontains=search_term)
        return search

class JoinedSafaris(models.Model):
   
    package=models.ForeignKey(Packages)
    Location=models.CharField(max_length=15, default="location")
    book_before=models.DateField(default=date.today)
    depature_date=models.DateField(default=date.today)
    today_date=models.DateField(auto_now_add=True)
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
        ('Budget', 'Budget'),
        ('Luxury','Luxury')
    )
    Accomodation=models.CharField(choices=Accomodation, max_length=20, default="accomodation")
    people_booked=models.IntegerField(default=0)

    def __str__(self):
        return self.package.name

    def datediff(self):
        date2 = self.book_before
        delta= date2 - timezone.now().date()
        return delta.days
        
    def seatsremaining(self):
        booked = self.people_booked
        seatsrem = 7 - booked
        return seatsrem

    @classmethod
    def search_by_depature_date(cls,search_term):
        package = cls.objects.filter(depature_date_icontains=search_term)
        return package
    
    

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

class ExcursionPrices(models.Model):
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



   
