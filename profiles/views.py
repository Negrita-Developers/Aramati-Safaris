from django.shortcuts import render

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
   return render(request, 'excursions/excursions.html') 