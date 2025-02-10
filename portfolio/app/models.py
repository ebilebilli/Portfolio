from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='static/img')
    date = models.IntegerField()