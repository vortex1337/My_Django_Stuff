from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    email = models.EmailField(max_length = 264)

# Create your models here.
