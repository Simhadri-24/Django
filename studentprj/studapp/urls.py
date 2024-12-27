"""
URL configuration for studentapp project.
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path,include
from studapp import views
urlpatterns = [
    path('addstudent/',views.createst,name='createst'),
    path('dispall/',views.studentlist, name='studentlist'),
    path('dispall/details/<int:id>/',views.studentdetails,name='studentdetails'),
    path('dispall/updatest/<int:id>/',views.updatest,name='updatest'),
    path('dispall/deletest/<int:id>/',views.deletest,name='deletest'),
    path('findstudent/',views.search,name='search'),
    path('', views.home, name='home'),

]
