from django.contrib import admin

# Register your models here.
from .models import JoinGroup, GuaranteedSafaris, Packages , LowSeason

admin.site.register(JoinGroup)
admin.site.register(GuaranteedSafaris)
admin.site.register(Packages)
admin.site.register(LowSeason)
 
