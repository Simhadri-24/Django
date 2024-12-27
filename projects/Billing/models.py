from django.db import models

# Create your models here.
class market(models.Model):
    empnumber=models.IntegerField(default=0);
    empname=models.CharField(max_length=50);
    DESIGNATION_CHOICES=[('Manager','Manager'),
                            ('Supervisor','Supervisor'),
                            ('Seller','Seller'),
                            ('Cashier','Cashier'),
                            ('Cleaner','Cleaner'),
                            ('Security','Security'),
                        ];
    designation=models.CharField(max_length=25,choices=DESIGNATION_CHOICES);
    mnumber=models.CharField(max_length=9);
class product(models.Model):
    pname=models.CharField(max_length=30);
    category=models.CharField(max_length=30);
    quantity=models.IntegerField();
    mrp=models.IntegerField();
    disper=models.IntegerField();
   
    