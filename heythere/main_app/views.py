from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee

# Home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# Events view
def events(request):
  return render(request, 'events.html')

# Employees index view
def employees_index(request):
  employees = Employee.objects.all()
  return render(request, 'employees/index.html', {
    'employees': employees
  })

def employees_detail(request, employee_id):
  employee = Employee.objects.get(id=employee_id)
  manager = Employee.objects.get(id=employee.manager_id)
  return render(request, 'employees/detail.html', { 
    'employee': employee,
    'manager': manager 
  })

class EmployeeCreate(CreateView):
  model = Employee
  fields = '__all__'

class EmployeeUpdate(UpdateView):
  model = Employee
  fields = ['employee_name', 'department', 'position', 'salary', 'birthdate']

class EmployeeDelete(DeleteView):
  model = Employee
  success_url = '/employees'