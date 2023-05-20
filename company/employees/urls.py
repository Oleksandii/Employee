from django.contrib import admin
from django.urls import path
from employees.views import *

urlpatterns = [
    path('employees/', employees, name='mainpage'),
    path('employees/description/<int:id>', description, name = 'description'),
    path('', mainpage, name = 'mainpage'),
    path('testing/', testing, name='testing'),

]
