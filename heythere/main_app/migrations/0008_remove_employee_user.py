# Generated by Django 5.0.1 on 2024-02-07 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]