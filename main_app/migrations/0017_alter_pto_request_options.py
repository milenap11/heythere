# Generated by Django 5.0.1 on 2024-02-11 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_employee_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pto_request',
            options={'ordering': ['-start_date']},
        ),
    ]