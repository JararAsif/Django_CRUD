from django.contrib import admin
from .models import Employee,Department

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('First_Name','Last_Name','department_name')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name','description','code')


