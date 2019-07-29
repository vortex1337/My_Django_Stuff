# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESSFUL!")
            print('NAME:' + form.cleaned_data['name'])
            print('EMAIL:' + form.cleaned_data['email'])
            print('TEXT:' + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form':form})
# Create your views here.
