from django.shortcuts import render

# Create your views here.
def excursions(request):
   return render(request, 'excursions.html') 
