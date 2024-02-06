from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Event
import requests
import os

# Home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  events = Event.objects.all()
  return render(request, 'home.html', {
    'events': events
  })

# Events index view
def events_index(request):
  response = requests.get(f'https://app.ticketmaster.com/discovery/v2/events.json?city=Miami&apikey={os.environ["TICKETMASTER_APIKEY"]}')
  for i in range(len(response.json()['_embedded']['events'])):
    event = response.json()['_embedded']['events'][i]
    if event.get('dates').get('timezone') == None:
      tz = 'none specified'
    else:
      tz = event.get('dates').get('timezone')
    new_event = Event(
      id=i,
      event_name=event['name'],
      event_venue=event['_embedded']['venues'][0]['name'],
      event_address=event['_embedded']['venues'][0]['address']['line1'],
      event_city=event['_embedded']['venues'][0]['city']['name'],
      event_state=event['_embedded']['venues'][0]['state']['stateCode'],
      event_zip=event['_embedded']['venues'][0]['postalCode'],
      event_latitude=event['_embedded']['venues'][0]['location']['latitude'],
      event_longitude=event['_embedded']['venues'][0]['location']['longitude'],
      event_localdate=event['dates']['start']['localDate'],
      event_localtime=event['dates']['start']['localTime'],
      event_timezone=tz
    )
    new_event.save()
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