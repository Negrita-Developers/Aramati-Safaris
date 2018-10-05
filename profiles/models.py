from django.db import models

# Create your models here.
class Profiles(models.Model):
    name=models.CharField(max_length=120)
    description =models.TextField(null=True)
    location = models.CharField(max_length=40, default='my location default')
    def __unicode__(self):
        return self.name