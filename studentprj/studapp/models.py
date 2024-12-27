from django.db import models
from django import forms

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    address=models.TextField()
    class Meta:
        db_table='student'

#Create Form from Models using ModelForm
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

#Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    def __str__(self):
        return self.username