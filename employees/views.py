from django.shortcuts import render, get_object_or_404
from .models import Employee

def employeehome(request):
    employees = Employee.objects.all()
    context = {'employees':employees,}
    return render(request, 'employees/employeehome.html', context)

def employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'employees/employee.html', context)