from django.shortcuts import render
from django.http import HttpResponse
from ringapp.models import Topic,Webpage, AccessRecord
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request,'ringapp/index.html' ,context = date_dict)
# Create your views here.
