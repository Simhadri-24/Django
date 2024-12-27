from django.urls import path
from . import views
urlpatterns=[
				path('',views.insert,name="insert"),
				path('display/',views.display,name="display"),
			]