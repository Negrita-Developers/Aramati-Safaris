from django.shortcuts import render

# Create your views here.
def home(request):
    context = locals()
    template = 'base.html'

    return render(request, template, context)

def home(request):
  return render(request, 'home.html')