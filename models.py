# allocation/models.py
from django.db import models

class Group(models.Model):
    group_id = models.IntegerField(unique=True)
    members = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Boys', 'Boys'), ('Girls', 'Girls'), ('Mixed', 'Mixed')])

class Hostel(models.Model):
    name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Boys', 'Boys'), ('Girls', 'Girls')])