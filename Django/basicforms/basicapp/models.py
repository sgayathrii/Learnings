from django.db import models

# Create your models here.

class Contact_Info(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField()
    text = models.TextField()