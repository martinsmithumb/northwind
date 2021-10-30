from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['employee_id','last_name','first_name', 'title', 'title_of_courtesy', 'birth_date', 'hire_date', 'address', 'city', 'region', 'postal_code', 'country', 'home_phone', 'extension', 'photo', 'notes', 'reports_to', 'photo_path', ]
    list_display = ['employee_id','last_name','first_name', 'title', 'title_of_courtesy', 'birth_date', 'hire_date', 'address', 'city', 'region', 'postal_code', 'country', 'home_phone', 'extension', 'photo', 'reports_to', 'photo_path', ]
    list_display_links = ['last_name']
    list_filter = ['title']
    search_fields = ['first_name','last_name']


