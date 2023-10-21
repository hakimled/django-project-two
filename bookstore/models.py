from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from os import path , remove 
from random import sample


def upload_location(instance, filename):
	today = timezone.now()
	base , ext = path.splitext(filename)

	randomList = [
		'1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f',
		'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'w','x','y','z']
	rando = sample(randomList, 10)
	new_random = ''.join(rando).upper() 

	file_path = 'pictures/{date}-{basename}{filename}'.format(date=today, basename=new_random,  filename=ext)
	return file_path



class Bookstore(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description =models.TextField()
    price = models.DecimalField( max_digits=7,  decimal_places=2)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to=upload_location)
    
    def __str__(self):
        return f'{self.author} added this book {self.title}'
    