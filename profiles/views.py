from django.shortcuts import render, get_object_or_404
from .models import JoinGroup

# Create your views here.
def home(request):
   return render(request, 'home.html') 

def aboutus(request):
   return render(request, 'about.html') 

def contact(request):
   return render(request, 'contacts.html') 

def joingroup(request):

    excur = JoinGroup.objects.all()

    return render(request, 'joingroup/joining.html', {"excur": excur})

def jointrial(request):

    excur = JoinGroup.objects.all()

    return render(request, 'joingroup/trial.html', {"excur": excur})

def guaranteedsafaris(request):

    
    return render(request, 'joingroup/joining.html')

def bookings(request):
   return render(request, 'bookings/booking-traveler.html')  

def excursions (request):
    return render(request, 'excursions/excursions.html')

def lakenaivasha (request):
    return render(request, 'excursions/lakenaivasha.html')
    
def lakenakuru (request):
    return render(request, 'excursions/lakenakuru.html') 

def nairobiexcursion (request):
    return render(request, 'excursions/nairobiexcursions.html')

def longsafaris(request):
    return render(request, 'longsafaris/longsafaris.html')

def shortsafaris (request):
    return render(request, 'shortsafaris/shortsafaris.html')

def ssfnakuru(request):
    return render (request, 'shortsafaris/2days/lakenakuru.html')

def aberdaressf(request):
    return render (request, 'shortsafaris/2days/aberdare.html')

def  amboselissf(request):
    return render (request, 'shortsafaris/2days/amboseli.html') 

def naivashassf(request):
    return render (request, 'shortsafaris/2days/naivasha.html')

def maasaimarassf(request):
    return render (request, 'shortsafaris/2days/maasaimara.html')

def pajetassf(request):
    return render (request, 'shortsafaris/2days/sweetwaters.html')

def amboselissf3(request):
    return render (request, 'shortsafaris/3days/amboseli.html') 

def sweetwaterssf3(request):
    return render (request, 'shortsafaris/3days/sweetwaters.html') 

def maasaimarassf3(request):
    return render (request, 'shortsafaris/3days/maasaimara.html') 

def nakurussf3(request):
    return render (request, 'shortsafaris/3days/nakuru.html') 

def samburussf3(request):
    return render (request, 'shortsafaris/3days/samburu.html') 

def maranakurussf4(request):
    return render (request, 'shortsafaris/4days/mara-nakuru.html') 

def amboselissf5(request):
    return render (request, 'shortsafaris/5days/amboseli.html') 




