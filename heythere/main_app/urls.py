from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_index, name='events_index'),
    path('events/<int:event_id>', views.events_detail, name='events_detail'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('events/seed/', views.events_seed, name='events_seed'),
    path('employees/<int:employee_id>/assoc_event/<int:event_id>/', views.assoc_event, name='assoc_event'),
    path('employees/', views.employees_index, name='index'),
    path('employees/<int:employee_id>/', views.employees_detail, name='detail'),
    path('employees/create/', views.EmployeeCreate.as_view(), name='employees_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employees_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employees_delete'),
    path('pto_requests/', views.pto_requests_index, name='pto_requests_index'),
    path('pto_requests/<int:pto_request_id>', views.pto_requests_detail, name='pto_requests_detail'),
    path('pto_requests/create/', views.PTOCreate.as_view(), name='pto_requests_create'),
    path('pto_requests/<int:pk>/update/', views.PTOUpdate.as_view(), name='pto_requests_update'),
    path('pto_requests/<int:pk>/delete/', views.PTODelete.as_view(), name='pto_requests_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
