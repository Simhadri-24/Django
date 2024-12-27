from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.empList, name='empList'),
    path('employees/add/', views.addEmp, name='addEmp'),
    path('employees/delete/<int:emp_id>/', views.delEmp, name='delEmp'),
    path('products/add/', views.addProduct, name='addProduct'),
    path('products/sold/<str:name>/<int:pquantity>/', views.sold_items, name='sold_items'),
    path('products/stock/', views.stock, name='stock'),
    path('products/availability/<str:pname>/', views.product_stock, name='product_stock'),
]
