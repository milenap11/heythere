from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Event, PTO_request
from .forms import CustomUserForm
import requests
import os
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import connection

# Home view
def home(request):
  events = Event.objects.all()
  if request.user.is_superuser:
      current_user = 'superuser'
  elif not request.user.is_anonymous:
      current_user = Employee.objects.get(employee_email=request.user.email)
  else:
      current_user = 'guest'
  return render(request, 'home.html', {
    'events': events,
    'current_user': current_user
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    employees = Employee.objects.all()
    users = User.objects.all()
    email_list = []
    useremail_list = []
    username_list = []
    for user in users:
      username_list.append(user)
      useremail_list.append(user.email)
    for employee in employees:
      email_list.append(employee.employee_email)
    if form.is_valid() and request.POST['email'] in email_list and request.POST['email'] not in useremail_list and request.POST['username'] not in username_list:
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid input. Either your username has already been taken, or your email did not match a valid employee email. Try again.'
  form = CustomUserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


#to seed with events from ticketmaster api
@login_required
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

# Events index view
@login_required
def events_index(request):
  if request.user.is_superuser:
    current_user = 'superuser'
  else:
    current_user = Employee.objects.get(employee_email=request.user.email)
  events = Event.objects.all()
  return render(request, 'events/index.html', {
    'events': events,
    'current_user': current_user
  })

# Events search view
@login_required
def search_events(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    events = Event.objects.filter(event_name__icontains=searched)
    return render(request, 'events/search_events.html', {
      'searched': searched,
      'events': events,
    })
  else:
    return render(request, 'events/search_events.html')

# Events detail view
@login_required
def events_detail(request, event_id):
  if request.user.is_superuser:
    current_user = 'superuser'
  else:
    current_user = Employee.objects.get(employee_email=request.user.email)
  event = Event.objects.get(id=event_id)
  venue = event.event_venue
  venue = '+'.join(venue.split())
  return render(request, 'events/detail.html', { 
    'event': event, 
    'current_user': current_user,
    'venue': venue,
  })

# PTO Request index view
@login_required
def pto_requests_index(request):
  if request.user.is_superuser:
    current_user = 'superuser'
  else:
    current_user = Employee.objects.get(employee_email=request.user.email)
  pto_requests = PTO_request.objects.all()
  return render(request, 'pto_request/index.html', {
    'pto_requests': pto_requests,
    'current_user': current_user
  })

# PTO Request detail view
@login_required
def pto_requests_detail(request, pto_request_id):
  if request.user.is_superuser:
    current_user = 'superuser'
  else:
    current_user = Employee.objects.get(employee_email=request.user.email)
  pto_request = PTO_request.objects.get(id=pto_request_id)
  return render(request, 'pto_request/detail.html', { 
    'pto_request': pto_request,
    'current_user': current_user
  })

# Employees index view
@login_required
def employees_index(request):
  if request.user.is_superuser:
    current_user = 'superuser'
  else:
    current_user = Employee.objects.get(employee_email=request.user.email)
  employees = Employee.objects.all()
  return render(request, 'employees/index.html', {
    'employees': employees,
    'current_user': current_user
  })

@login_required
def employees_detail(request, employee_id):
  if request.user.is_superuser:
    current_user = 'superuser'
  else:
    current_user = Employee.objects.get(employee_email=request.user.email)
  employee = Employee.objects.get(id=employee_id)
  manager = Employee.objects.get(id=employee.manager_id)
  return render(request, 'employees/detail.html', { 
    'employee': employee,
    'manager': manager,
    'current_user': current_user
  })

def assoc_event(request, employee_id, event_id):
  Employee.objects.get(id=employee_id).attending_events.add(event_id)
  return redirect('events_detail', event_id=event_id)

def unassoc_event(request, employee_id, event_id):
  Event.objects.get(id=event_id).employee_set.remove(employee_id)
  return redirect('events_detail', event_id=event_id)

class EmployeeCreate(LoginRequiredMixin, CreateView):
  model = Employee
  fields = ['employee_name', 'employee_email', 'department', 'position', 'salary', 'birthdate', 'manager_id']

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
  model = Employee
  fields = ['employee_name', 'department', 'position', 'salary', 'birthdate', 'manager_id']

class EmployeeDelete(LoginRequiredMixin, DeleteView):
  model = Employee
  success_url = '/employees'

class EventCreate(LoginRequiredMixin, CreateView):
  model = Event
  fields = '__all__'

class EventUpdate(LoginRequiredMixin, UpdateView):
  model = Event
  fields = '__all__'

class EventDelete(LoginRequiredMixin, DeleteView):
  model = Event
  success_url = '/events'

class PTOCreate(LoginRequiredMixin, CreateView):
  model = PTO_request
  fields = ['employee', 'start_date', 'end_date']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PTOUpdate(LoginRequiredMixin, UpdateView):
  model = PTO_request
  fields = ['status', 'start_date', 'end_date']

class PTODelete(LoginRequiredMixin, DeleteView):
  model = PTO_request
  success_url = '/pto_requests'