from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('employees/', views.employees_index, name='index'),
    path('employees/<int:employee_id>/', views.employees_detail, name='detail'),
    path('employees/create/', views.EmployeeCreate.as_view(), name='employees_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employees_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employees_delete'),
]
