from django.contrib import admin
from . models import Position, Employee

admin.site.register (Position)
# admin.site.register (Employee)
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ('fullname','emp_code','mobile','position')
    list_filter = ('fullname',)


# Register your models here.
