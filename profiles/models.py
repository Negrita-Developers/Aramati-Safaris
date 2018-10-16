from django.db import models

# Create your models here.
class Profiles(models.Model):
    name=models.CharField(max_length=120)
    email =models.CharField(max_length=40, blank=False, default='my email default')
    location = models.CharField(max_length=40, default='my location default')
    
    def __unicode__(self):
        return self.name

class SpecialOffers(models.Model):
    title=models.CharField(max_length=120)
    depature=models.DateField(auto_now_add=True)
    # images=
    # bookbefore=
    # duration=
    # accomodation=
    # itinerary=
    # included=
    # notincluded=

class Package(models.Model):
    title=models.CharField(max_length=120)
    location=models.CharField(max_length=20)
    details= models.TextField()
    depature=models.DateField(auto_now_add=True)
    price1=models.IntegerField()
    price2=models.IntegerField()
    price3=models.IntegerField()
    price4=models.IntegerField()
    price5=models.IntegerField()
    price6=models.IntegerField()
    price7=models.IntegerField()
    image=models.ImageField(upload_to = 'package/')
    accomodation=(
        ('budget'),
        ( 'standard')

    )
    itinerary= models.TextField()
    bookbefore=models.DateField(auto_now_add=True)



