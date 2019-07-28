from django.conf.urls import url
from ringapp import views
urlpatterns = [
url(r'^$', views.index, name = 'index')
]
