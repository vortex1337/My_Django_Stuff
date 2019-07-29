from django.conf.urls import url
from freshapp import views
urlpatterns = [
    url(r'^$', views.index, name = 'index')
    ]
