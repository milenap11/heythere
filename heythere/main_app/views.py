from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Event

# Home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# Events index view
def events_index(request):
  events = Event.objects.all()
  return render(request, 'events/index.html', {
    'events': events
  })

# Events detail view
def events_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  return render(request, 'events/detail.html', { 
    'event': event, 
  })

# PTO Request view
# def pto_request(request):
#   return render(request, 'pto_request.html')

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