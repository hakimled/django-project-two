from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bookstore(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description =models.TextField()
    price = models.DecimalField(decimal_places=2)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='pictures')
    
    def __str__(self):
        return f'{self.author} added this book {self.title}'
    