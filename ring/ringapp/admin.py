from django.contrib import admin
from ringapp.models import Topic,Webpage,AccessRecord

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# Register your models here.
