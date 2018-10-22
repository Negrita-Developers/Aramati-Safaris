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


