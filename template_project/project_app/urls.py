from django.conf.urls import url
from project_app import views

urlpatterns = [

    url(r'^$', views.help, name = 'help'),
]
