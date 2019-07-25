from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('Peshkata')
def help(request):
    helpdic = {'help_insert':'HELP PAGE'}
    return render(request, 'project_app/help.html',context=helpdic)

# Create your views here.
