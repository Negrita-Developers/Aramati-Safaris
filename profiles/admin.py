from django.contrib import admin

# Register your models here.
from .models import Profiles, Package, Excursion,TwoSSF

admin.site.register(Profiles)
admin.site.register(Excursion)
admin.site.register(TwoSSF)

