from django.db import models
from django.urls import reverse

class Employee(models.Model):
    # id = models.AutoField()

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    birthdate = models.DateField()

    # attending_events = models.ForeignKey('Event')
    # pto_requests = models.ForeignKey('pto_requests')
    # manager_id = models.ForeignKey('Employee')
    # actual = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'employee_id': self.id})