# Generated by Django 5.1 on 2024-09-03 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_registration_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='last_name',
        ),
    ]
