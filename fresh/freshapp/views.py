from django.shortcuts import render
from django.http import HttpResponse
from freshapp.models import Users

def index(request):
    users_list = Users.objects.all()
    my_dict = {'my_users': users_list}
    return render(request, 'freshapp/index.html' ,context = my_dict)

# Create your views here.
