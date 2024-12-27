from django.db import models

# Create your models here.
class student(models.Model):
    rno=models.IntegerField()
    name=models.CharField(max_length=100)
    m1=models.IntegerField()
    m2=models.IntegerField()
    m3=models.IntegerField()
    total=models.IntegerField(editable=False,null=True)
    average=models.FloatField(editable=False,null=True)
    result=models.CharField(max_length=4,editable=False,null=True)
    
    def save(self, *args, **kwargs):
       # Calculate total, average, and result before saving
       self.total = self.m1 + self.m2 + self.m3
       self.average = round(self.total / 3,2)
       self.result = "PASS" if self.m1 >= 50 and self.m2 >= 50 and self.m3 >= 50 else "FAIL"
       super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['rno']