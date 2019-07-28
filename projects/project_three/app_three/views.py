# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def display_pesho(response):
    return HttpResponse('Pesho')

# Create your views here.
