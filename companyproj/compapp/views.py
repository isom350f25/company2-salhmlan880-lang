from django.shortcuts import render
from .models import Employee
from django.shortcuts import get_object_or_404

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employee_detail.html', {'employee':employee})