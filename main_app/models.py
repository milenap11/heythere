from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illonois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('DC', 'Washington, D.C.'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

STATUS = (
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('D', 'Denied'),
)

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_venue = models.CharField(max_length=255)
    event_address = models.CharField(max_length=255)
    event_city = models.CharField(max_length=100)
    event_state = models.CharField(
        max_length=2,
        choices=STATES,
        default=STATES[0][0]
    )
    event_zip = models.IntegerField()
    event_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    event_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    event_localdate = models.DateField()
    event_localtime = models.TimeField()
    event_timezone = models.CharField(max_length=100)
    event_img_url = models.TextField(default='#')

    def __str__(self):
        return f"{self.event_name} in {self.event_city}, {self.event_state} {self.event_zip}"
    
    #check this line for possible error
    def get_absolute_url(self):
        return reverse('events_detail', kwargs={'event_id': self.id})
    
    class Meta:
        ordering = ['-event_localdate']

class Employee(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True    
    )
    employee_name = models.CharField(max_length=100)
    employee_email = models.CharField(
        max_length=255,
        unique=True
    )
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    birthdate = models.DateField()
    manager_id = models.IntegerField(default=0)
    attending_events = models.ManyToManyField(Event)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        unique=True
    )

    def __str__(self):
        return f"{self.employee_name}, user_id: {self.user}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'employee_id': self.id})
    
class PTO_request(models.Model):
    employee_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )
    start_date = models.DateField()
    end_date = models.DateField()
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"STATUS {self.get_status_display()}: {self.employee} asked for time off from {self.start_date} to {self.end_date}"
    
    def get_absolute_url(self):
        return reverse('pto_requests_detail', kwargs={'pto_request_id': self.id})
    
    class Meta:
        ordering = ['-start_date']

class Memo(models.Model):
    date = models.DateField(
        'delivery date',
        default=timezone.now
    )
    message = models.TextField(max_length=250)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message} delivered to {self.employee.name} on {self.date}."
    
    class Meta:
        ordering = ['-date']