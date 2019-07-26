# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    my_dict = {'insert_content':"HELLO I AM FROM FIRSTAPP!!"}
    return render(request, 'firstapp/index.html', context = my_dict)
# Create your views here.
