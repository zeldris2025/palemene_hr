from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    employment_commencement_date = models.DateField(blank=True, null=True)
    annual_leave = models.CharField(max_length=100, default=0)
    sick_leave = models.CharField(max_length=100, default=0)
    toil = models.CharField(max_length=100, blank=True, default=0)
    bereavement_leave = models.CharField(max_length=100, default=0)
    maternity_leave = models.CharField(max_length=100, default=0)
    paternity_leave = models.CharField(max_length=100, default=0)
    comments = models.CharField(max_length=255, default="n/a")

    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"
