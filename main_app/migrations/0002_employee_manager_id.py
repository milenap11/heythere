# Generated by Django 5.0.1 on 2024-02-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager_id',
            field=models.IntegerField(default=0),
        ),
    ]
