from django.conf.urls import url
from project4_app import views

urlpatterns = [
url(r'^$', views.index, name = 'index'),
]
