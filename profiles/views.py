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

def single(request, id):

    singlegroup = get_object_or_404(JoinGroup, id=id)

    return render(request, 'joingroup/single.html', {"singlegroup": singlegroup}) 

def bookings(request):
   return render(request, 'bookings/booking-traveler.html')  

def excursions (request):
    return render(request, 'excursions/excursions.html')

def longsafaris(request):
    return render(request, 'longsafaris/longsafaris.html')

def shortsafaris (request):
    return render(request, 'shortsafaris/shortsafaris.html')




