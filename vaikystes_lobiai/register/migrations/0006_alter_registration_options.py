# Generated by Django 5.1 on 2024-09-10 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_registration_child_first_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name': 'Registracija', 'verbose_name_plural': 'Registracijos'},
        ),
    ]
