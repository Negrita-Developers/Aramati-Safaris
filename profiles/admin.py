from django.contrib import admin

# Register your models here.
from .models import Profiles, Package, Excursion

admin.site.register(Profiles)
admin.site.register(Package) 
admin.site.register(Excursion)

