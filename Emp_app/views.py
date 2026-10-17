from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()

    search = request.GET.get('search')
    if search:
        employees = employees.filter(name__icontains=search) | employees.filter(department__icontains=search)

    total = Employee.objects.count()

    return render(request, 'employee_list.html', {
        'employees': employees,
        'total': total,
    })


def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        salary = request.POST['salary']
        joining_date = request.POST['joining_date']

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary,
            joining_date=joining_date
        )

        return redirect('employee_list')

    return render(request, 'add_employee.html')


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')