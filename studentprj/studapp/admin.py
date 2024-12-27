from django.contrib import admin
from studapp import models



#Display from admin side 
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','mail','phonenumber',)


# Register your models here.
admin.site.register(models.Student,StudentAdmin)
#admin.site.register(models.LoginForm)