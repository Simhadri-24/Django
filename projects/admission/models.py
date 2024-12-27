from django.db import models

# Create your models here.
class Personal(models.Model):
    appid=models.IntegerField()
    name=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    mno=models.CharField(max_length=10)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
class Mark(models.Model):
    appid = models.OneToOneField(Personal, on_delete=models.CASCADE, unique=True)
    m1=models.IntegerField()
    m2=models.IntegerField()
    m3=models.IntegerField()
    m4=models.IntegerField()
    m5=models.IntegerField()
    total=models.IntegerField(editable=False,null=True)
    
    def save(self, *args,**kwargs):
        self.total=self.m1+self.m2+self.m3+self.m4+self.m5
        super().save(*args,**kwargs)
    