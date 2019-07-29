import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'fresh.settings')
import django
django.setup()
import random
from freshapp.models import Users
from faker import Faker
fakegen = Faker()
def populate(n = 10):
    for entry in range(n):
        user = Users.objects.get_or_create(first_name = fakegen.name().split()[0], last_name = fakegen.name().split()[0], email = fakegen.email().split())
print('population starting')
populate(5)
print('population end')
