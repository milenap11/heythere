from django.shortcuts import render

# Add here below list of employees dictionaries

# Home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# Events view
def events(request):
  return render(request, 'events.html')

# Employees index view
def employees_index(request):
  return render(request, 'employees/index.html', {
    'employees': employees
  })