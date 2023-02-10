from enum import unique
from django.db import models

# Create your models here.

class User_data(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=264, unique=True)


    