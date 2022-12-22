from django.db import models

# Create your models here.
class School(models.Model):
    Name=models.CharField(max_length=100)
    Principal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)

    def __str__(self):
        return self.Name