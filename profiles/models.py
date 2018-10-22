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
    details= models.TextField()
    travelers_that_have_booked=models.IntegerField()
    price1=models.FloatField()
    price2=models.IntegerField()
    price3=models.IntegerField()
    price4=models.IntegerField()
    price5=models.IntegerField()
    price6=models.IntegerField()
    price7=models.IntegerField()
    image1=models.IntegerField()
    image2=models.IntegerField()
    image3=models.IntegerField()
    image4=models.IntegerField()
    image5=models.IntegerField()
    image6=models.IntegerField()
    image7=models.IntegerField()
    accomodation=(
        ('budget'),
        ( 'standard')

    )
    itinerary= models.TextField()
    created_on=models.DateField(auto_now_add=True)
    bookbefore=models.DateField()

    def __str__(self):
        return self.title 


