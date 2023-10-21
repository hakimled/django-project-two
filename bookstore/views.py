from django.shortcuts import render



def bookstore(request):
    
    return render(request , 'bookstore/bookstore.html' , {})