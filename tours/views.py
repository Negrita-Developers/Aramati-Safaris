from django.shortcuts import render
from profiles import views

# Create your views here.

def excursions(request):
   return render(request, 'excursions/excursions.html') 
