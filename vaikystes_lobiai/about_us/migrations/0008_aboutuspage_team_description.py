# Generated by Django 5.1 on 2024-09-02 13:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0007_alter_aboutuspage_about_us_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuspage',
            name='team_description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
