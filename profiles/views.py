from django.shortcuts import render, get_object_or_404
from .models import Package, Excursion

# Create your views here.
def home(request):
   return render(request, 'home.html') 

def aboutus(request):
   return render(request, 'about.html') 

def offers(request):
   return render(request, 'offers.html') 

def contact(request):
   return render(request, 'contacts.html') 

def excursions(request ):
   excur = Excursion.objects.all()

   return render(request, 'excursions/excursions.html', {"excur": excur })   

def singleexcur(request, excursions_id):
    
    excur = Excursion.objects.get(id=excursions_id)
   
      
    return render(request, "excursions/single.html", {"excur": excur })

def shortsafaris(request):

    ssf = ShortSafaris.objects.all()
    return render(request, 'shortsafaris/excursions.html', {"ssf": ssf })  

def booking(request):
    excur = Excursion.objects.all()
    return render(request, 'bookings/booking-traveler.html', {"excur": excur })

def confirming(request):
    excur = Excursion.objects.all()
    return render(request, 'bookings/booking-confirm.html', {"excur": excur })

def payment(request):
    excur = Excursion.objects.all()
    return render(request, 'bookings/booking-payment.html', {"excur": excur })
