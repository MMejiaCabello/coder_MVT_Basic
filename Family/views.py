from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia

# Create your views here.
def inicio(request):
    return HttpResponse('<h1>Inicio</h1>')

def family(request):
    familias = Familia.objects.all()
    return render(request, 'family.html', {'familias':familias})