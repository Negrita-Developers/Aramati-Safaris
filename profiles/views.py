from django.shortcuts import render, get_object_or_404
from .models import Packages , LowSeason, JoinedSafaris , HighSeason, PeakSeason

# Create your views here.

# General view pages
def home(request):
   return render(request, 'home.html') 

def aboutus(request):
   return render(request, 'about.html') 

def contact(request):
   return render(request, 'contacts.html') 

#excursions
def excursions (request):
    return render(request, 'excursions/excursions.html')

def lakenaivasha (request):
    return render(request, 'excursions/lakenaivasha.html')

def joinlakenaivasha (request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render(request, 'joingroup/excursions/lakenaivasha.html', {"guaras": guaras}, {" single":  single})

def lakenakuru (request):
    return render(request, 'excursions/lakenakuru.html')  

def joinlakenakuru (request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render(request, 'joingroup/excursions/lakenakuru.html', {"guaras": guaras}, {" single":  single})    

def nairobiexcursion (request):
    return render(request, 'excursions/nairobiexcursions.html')
 

#short safaris

def shortsafaris (request):
    return render(request, 'shortsafaris/shortsafaris.html')

def ssfnakuru(request):
    return render (request, 'shortsafaris/2days/lakenakuru.html')

def joinssfnakuru(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/2days/lakenakuru.html', {"guaras": guaras}, {" single":  single})

def aberdaressf(request):
    return render (request, 'shortsafaris/2days/aberdare.html')

def aberdarejoinssf(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/2days/aberdare.html', {"guaras": guaras}, {" single":  single})

def amboselissf(request):
    return render (request, 'shortsafaris/2days/amboseli.html') 

def amboselijoinssf(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/2days/amboseli.html', {"guaras": guaras}, {" single":  single}) 

def naivashassf(request):
    return render (request, 'shortsafaris/2days/naivasha.html')

def naivashajoinssf(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/2days/naivasha.html', {"guaras": guaras}, {" single":  single})

def maasaimarassf(request):
    return render (request, 'shortsafaris/2days/maasaimara.html')

def maasaimarajoinssf(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/2days/maasaimara.html', {"guaras": guaras}, {" single":  single})

def pajetassf(request):
    return render (request, 'shortsafaris/2days/sweetwaters.html')

def pajetajoinssf(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/2days/sweetwaters.html', {"guaras": guaras}, {" single":  single})

def amboselissf3(request):
    return render (request, 'shortsafaris/3days/amboseli.html') 

def amboselijoinssf3(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/3days/amboseli.html', {"guaras": guaras}, {"single":  single})

def sweetwaterssf3(request):
    return render (request, 'shortsafaris/3days/sweetwaters.html') 

def sweetwaterjoinssf3(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/3days/sweetwaters.html', {"guaras": guaras}, {"single":  single})

def maasaimarassf3(request):
    return render (request, 'shortsafaris/3days/maasaimara.html') 

def maasaimarajoinssf3(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/3days/maasaimara.html', {"guaras": guaras}, {"single":  single})

def nakurussf3(request):
    return render (request, 'shortsafaris/3days/nakuru.html') 

def nakurujoinssf3(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/3days/nakuru.html', {"guaras": guaras}, {"single":  single})

def samburussf3(request):
    return render (request, 'shortsafaris/3days/samburu.html') 

def samburujoinssf3(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/3days/samburu.html', {"guaras": guaras}, {"single":  single})

def maranakurussf4(request):
    return render (request, 'shortsafaris/4days/mara-nakuru.html') 

def maranakurujoinssf4(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/4days/mara-nakuru.html', {"guaras": guaras}, {"single":  single}) 

def amboselissf5(request):
    return render (request, 'shortsafaris/5days/amboseli.html') 

def amboselijoinssf5(request):
    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    return render (request, 'joingroup/5days/amboseli.html', {"guaras": guaras}, {"single":  single}) 

#long safaris
def longsafaris(request):
    return render(request, 'longsafaris/longsafaris.html')

#joining groups
def guaranteedsafaris(request):

    guaras = JoinedSafaris.objects.all()
    single = Packages.objects.all()
    
    return render(request, 'joingroup/joining.html', {"guaras": guaras}, {" single":  single})

#booking and checkout
def bookings(request):
    return render(request, 'bookings/booking-traveler.html') 
