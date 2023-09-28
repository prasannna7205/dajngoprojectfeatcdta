from django.contrib import admin
from featchapp.models import employees

# Register your models here.
class employeesData(admin.ModelAdmin):
    list_display = ['name','eno','esal','addrs']

admin.site.register(employees,employeesData)
