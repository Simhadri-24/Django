from django.urls import path
from . import views
urlpatterns=[
				path('',views.index,name="index"),
				path('stud_post/',views.stud_post,name="stud_post"),
				path('stud_archieve/',views.stud_archieve,name="stud_archieve"),
			]