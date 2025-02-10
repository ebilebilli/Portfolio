from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=500)
    date = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'