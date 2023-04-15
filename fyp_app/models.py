from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


class Registeration(models.Model):
    sno = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


