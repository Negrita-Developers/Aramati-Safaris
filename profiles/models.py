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
    travelers_that_have_booked=models.FloatField()
    image1=models.ImageField()
    accomodation=(
        ('budget'),
        ( 'standard')

    )
    itinerary= models.TextField()
    created_on=models.DateField(auto_now_add=True)
    bookbefore=models.DateField()

    def __str__(self):
        return self.title 

        


