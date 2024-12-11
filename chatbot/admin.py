from django.contrib import admin
from .models import Employee
from import_export import resources
from import_export.admin import ExportMixin, ImportMixin

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee

class EmployeeAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = EmployeeResource

admin.site.register(Employee, EmployeeAdmin)
