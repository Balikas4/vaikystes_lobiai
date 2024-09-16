# Generated by Django 5.1 on 2024-09-16 07:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_alter_registration_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='admission_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Priėmimo data'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='document_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Dokumento data'),
        ),
    ]
