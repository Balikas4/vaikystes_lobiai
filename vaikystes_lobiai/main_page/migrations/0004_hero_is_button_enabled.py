# Generated by Django 5.1 on 2024-10-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_mainpage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='is_button_enabled',
            field=models.BooleanField(default=True),
        ),
    ]