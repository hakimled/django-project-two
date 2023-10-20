from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h2>hello world </h2>')
    return render(request , 'boards/home.html')
