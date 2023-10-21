from django.shortcuts import render
from django.http import HttpResponse
from . models import Board , Post , Topic

def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    #return HttpResponse('<h2>hello world </h2>')
    return render(request , 'boards/home.html' , context)

