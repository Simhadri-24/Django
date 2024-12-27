from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=150)
    rno=models.IntegerField(default=True)
    m1=models.IntegerField(default=True)
    m2=models.IntegerField(default=True)
    m3=models.IntegerField(default=True)
    m4=models.IntegerField(default=True)
    @property
    def average(self):
        return (self.m1+self.m2+self.m3+self.m4)/4

    def __str__(self):
        return self.name
    #class Meta:
        ordering=('avg',)
        
