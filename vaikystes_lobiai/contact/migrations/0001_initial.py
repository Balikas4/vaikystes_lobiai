# Generated by Django 5.1 on 2024-09-02 14:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('additional_info', ckeditor.fields.RichTextField()),
                ('hero_photo', models.ImageField(blank=True, null=True, upload_to='contact_photos/')),
            ],
        ),
    ]
