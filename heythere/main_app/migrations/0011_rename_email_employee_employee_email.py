# Generated by Django 5.0.1 on 2024-02-08 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_employee_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='email',
            new_name='employee_email',
        ),
    ]
