from django.contrib import admin

# Register your models here.
from .models import Packages , LowSeason, JoinedSafaris , HighSeason, PeakSeason


admin.site.register(JoinedSafaris) 
admin.site.register(Packages)
admin.site.register(LowSeason)
admin.site.register(HighSeason)
admin.site.register(PeakSeason)
 
