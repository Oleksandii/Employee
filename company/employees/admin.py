from django.contrib import admin
from employees.models import Employees, Department,Pseudonym,Tasks,Description


admin.site.register([Employees, Department,Pseudonym,Tasks,Description])

# Register your models here.
