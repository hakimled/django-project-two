from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    group_admin = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True)
    

    def __str__(self):
        return self.group_name 
    

class Group_member(models.Model):
    group_id = models.ForeignKey(Group , on_delete=models.CASCADE)
    joined_on = models.DateTimeField(default=timezone.now)
    member = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return f' {self.member} joined {self.group_id} '

