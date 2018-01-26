# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    users = User.objects.filter(username=request.POST['username'])
    user_id = users.first().id
    
    request.session['user_id'] = user_id
    request.session['name'] = users.first().name
    if users.count() == 0:
        messages.error(request, 'Unknown Username', extra_tags='username')
        return redirect('/')
    if not bcrypt.checkpw(request.POST['password'].encode(), users.first().password.encode()):
        messages.error(request, 'Password Invalid', extra_tags='password')
        return redirect('/')
    return redirect('/success')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    User.objects.create(name=request.POST['name'],
        username=request.POST['username'],
        
        password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    return redirect('/success')


def success(request):
    return render(request, 'success.html')