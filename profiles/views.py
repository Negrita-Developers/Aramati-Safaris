from django.shortcuts import render

# Create your views here.
def home(request):
   context = locals()
   template = 'home.html'

   return render(request, template, context)

# def home(request):
#   return render(request, 'home.html')

def aboutus(request):
   return render(request, 'about.html') 

def offers(request):
   return render(request, 'offers.html') 