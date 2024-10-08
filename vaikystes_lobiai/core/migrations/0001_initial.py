# Generated by Django 5.1 on 2024-08-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField(blank=True, max_length=100000)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
