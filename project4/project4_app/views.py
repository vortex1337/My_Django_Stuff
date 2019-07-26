from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':"I am from project4_app" }
    return render(request, 'project4_app/index.html', context = my_dict)
# Create your views here.
