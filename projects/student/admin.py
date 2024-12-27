from django.contrib import admin

# Register your models here.
from .models import student

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('rno','name','m1','m2','m3')
    ordering=('rno',)