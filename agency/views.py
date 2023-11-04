from django.shortcuts import render
from . models import Agency

def agency(request):
    
    context = {}
    return render(request, 'agency/agency.html' , context)