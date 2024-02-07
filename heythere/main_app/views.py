from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Event, PTO_request
import requests
import os

# Home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  events = Event.objects.all()
  return render(request, 'home.html', {
    'events': events
  })

#to seed with events from ticketmaster api
def events_seed(request):
  Event.objects.all().delete()
  response = requests.get(f'https://app.ticketmaster.com/discovery/v2/events.json?city=Miami&apikey={os.environ["TICKETMASTER_APIKEY"]}')
  events_list_api = response.json()['_embedded']['events']
  for i in range(len(events_list_api)):
    event = events_list_api[i]
    if event.get('dates').get('timezone') == None:
      tz = 'none specified'
    else:
      tz = event.get('dates').get('timezone')
    new_event = Event(
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
      event_timezone=tz,
      event_img_url=event['images'][0]['url']
    )
    new_event.save()
  events = Event.objects.all()
  return render(request, 'events/index.html', {
    'events': events
  })

# Test pto_request objects
pto_requests = [
  {'employee_name': 'Milena', 'status': 'P', 'start_date': '2024-02-07', 'end_date': '2024-2-10', 'employee': 1},
  {'employee_name': 'Jason', 'status': 'A', 'start_date': '2024-02-08', 'end_date': '2024-02-13', 'employee': 2},
  {'employee_name': 'Jae', 'status': 'D', 'start_date': '2024-02-10', 'end_date': '2024-02-11', 'employee': 3},
]

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

# PTO Request index view
def pto_request_index(request):
  pto_requests = PTO_request.objects.all()
  employee = Employee.objects.get(id = pto_requests.employee)
  return render(request, 'pto_request/index.html', {
    'pto_requests': pto_requests,
    'employee': employee
  })

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

# def assoc_event(request, employee_id, event_id):
#   Employee.objects.get(id=employee_id).attending_events.add(event_id)
#   return redirect('events_detail', event_id=event_id)

class EmployeeCreate(CreateView):
  model = Employee
  fields = '__all__'

class EmployeeUpdate(UpdateView):
  model = Employee
  fields = ['employee_name', 'department', 'position', 'salary', 'birthdate']

class EmployeeDelete(DeleteView):
  model = Employee
  success_url = '/employees'

class EventCreate(CreateView):
  model = Event
  fields = '__all__'

class EventUpdate(UpdateView):
  model = Event
  fields = '__all__'

class EventDelete(DeleteView):
  model = Event
  success_url = '/events'