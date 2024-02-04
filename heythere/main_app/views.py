from django.shortcuts import render
from .models import Employee

# Add here below list of employees dictionaries
# employees = [
#   {'name': 'Jae', 'department': 'IT', 'position': 'asdf', 'salary': 12345},
#   {'name': 'Jason', 'department': 'IT', 'position': 'asdf', 'salary': 12345},
#   {'name': 'Milena', 'department': 'IT', 'position': 'asdf', 'salary': 12345},
#   {'name': 'Scott', 'department': 'IT', 'position': 'asdf', 'salary': 12345},
#   {'name': 'Devlin', 'department': 'IT', 'position': 'asdf', 'salary': 12345},
# ]

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
  return render(request, 'employees/detail.html', { 'employee': employee })