from django.shortcuts import render
from .models import Bookstore
from django.contrib.auth import logout




def logout_view(request):
    logout(request)
    return render(request, 'boards/home.html')

def bookstore(request):
    books = Bookstore.objects.all().order_by('-added_on')
    
    
    context = {'books': books}
    for book in books:
        print(book.title)
        print(book.picture.url)
    
    
    return render(request , 'bookstore/bookstore.html' , context)