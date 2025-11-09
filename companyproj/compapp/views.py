from django.shortcuts import render
from .models import Employee
from django.shortcuts import get_object_or_404

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})


def employee_detail(request, pk):
    """Show a single employee and their projects."""
    employee = get_object_or_404(Employee, pk=pk)
    # access projects via related_name 'projects'
    projects = employee.projects.all().order_by('start_date')
    return render(request, 'employee_detail.html', {'employee': employee, 'projects': projects})