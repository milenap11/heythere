from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('employees/', views.employees_index, name='index'),
    path('employees/<int:employee_id>/', views.employees_detail, name='detail'),
]