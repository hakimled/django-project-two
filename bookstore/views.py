from django.shortcuts import render
from .models import Bookstore


def bookstore(request):
    books = Bookstore.objects.all().order_by('-added_on')
    
    
    context = {'books': books}
    
    
    return render(request , 'bookstore/bookstore.html' , context)