# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = 'Your Name must have at least 2 letters, letters only please'
        if len(postData['username']) < 2:
            errors['username'] = 'Your UserName must have at least 2 characters please'
        
        if len(postData['password']) < 8:
            errors['password'] = 'Password must have at least 8 characters, any type'
        if postData['password'] != postData['confirm']:
            errors['confirm'] = 'Confirm must match your Password'
        return errors


#Not sure what happened here.  LogAndReg were working.

#Moved startdate, enddate, and plan from Trip to User.
#   Can't stop the error train.


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    startdate = models.DateField('%m/%d/%Y')#???
    enddate = models.DateField(None)
    plan = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=50)
    
    traveller = models.ManyToManyField(User)

    def __str__(self):
        return self.destination

