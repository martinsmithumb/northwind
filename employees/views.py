from django.shortcuts import render

def employeehome(request):
    context = {}
    return render(request, 'employees/employeehome.html', context)
