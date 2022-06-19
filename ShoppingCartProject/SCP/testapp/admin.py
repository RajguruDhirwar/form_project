from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
