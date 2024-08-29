# Generated by Django 5.1 on 2024-08-29 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial_squashed_0017_remove_hero_main_page_remove_maingallery_main_page_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='about_us_page',
        ),
        migrations.RemoveField(
            model_name='dailyroutine',
            name='activities',
        ),
        migrations.AlterUniqueTogether(
            name='dailyroutine',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='dailyroutine',
            name='group',
        ),
        migrations.DeleteModel(
            name='Grupe',
        ),
        migrations.DeleteModel(
            name='AboutUsPage',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='DailyRoutine',
        ),
    ]