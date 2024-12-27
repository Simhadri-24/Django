from django.db import models

# Create your models here.

class name(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    date=models.DateField()
    """def __str__(self):
        return f"{self.firstname} {self.lastname}"""
