from django.db import models
from django.utils import timezone

class Agency(models.Model):
    
    agency = models.CharField(max_length=100)
    added_on = models.DateTimeField(default=timezone.now)
    provide_haj = models.BooleanField(default=False , null=False)
    
    def __str__(self):
        return f'{self.agency} '
 

class Member(models.Model):
    member_name = models.CharField(max_length=100)
    agency_name = models.ManyToManyField(Agency)
    created_on = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.member_name}'