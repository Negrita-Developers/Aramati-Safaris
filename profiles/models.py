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
    brief_details= models.TextField()
    travelers_that_have_booked=models.IntegerField()
    image=models.ImageField()
    accomodation=(
        ('budget'),
        ( 'standard')

    )
    bookbefore=models.DateField()

    def __str__(self):
        return self.title 

        


