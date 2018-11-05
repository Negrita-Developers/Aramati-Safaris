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
    title = (
        ('2dys' '2 days Lake Naivasha'),
        ('3dys' '2 days Lake Naivasha'),
    )
    location=models.CharField(max_length=20)
    travelers_that_have_booked=models.IntegerField(default=0)
    image=models.ImageField()
    price=models.IntegerField(default=0)
    accomodation=(
        ('budget'),
        ( 'standard')
    ) 
    bookbefore=models.DateField()
    
    def __unicode__(self):
        return self.title

  


