from django.shortcuts import render
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

def excursions(request):
   excur = Excursion.objects.all()

   return render(request, 'excursions/excursions.html', {"excur": excur })   

def singleexcur(request):
    excur = Excursion.objects.all()
    return render(request, 'excursions/single.html', {"excur": excur })

def booking(request):
    excur = Excursion.objects.all()
    return render(request, 'booking-traveler.html', {"excur": excur })

def confirming(request):
    excur = Excursion.objects.all()
    return render(request, 'booking-confirm.html', {"excur": excur })

def payment(request):
    excur = Excursion.objects.all()
    return render(request, 'booking-payment.html', {"excur": excur })
