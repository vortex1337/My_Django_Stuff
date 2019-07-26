# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    my_dict = {'insert_me': 'kvo stava'}
    return render(request, 'app5/index.html',context = my_dict)
# Create your views here.
