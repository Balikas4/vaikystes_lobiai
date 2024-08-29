# Generated by Django 5.1 on 2024-08-29 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_galleryimage_category_delete_gallerycategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='main_page',
        ),
        migrations.RemoveField(
            model_name='maingallery',
            name='main_page',
        ),
        migrations.RemoveField(
            model_name='mainreview',
            name='main_page',
        ),
        migrations.RemoveField(
            model_name='weeklynutrition',
            name='nutrients',
        ),
        migrations.DeleteModel(
            name='NutritionPage',
        ),
        migrations.AlterUniqueTogether(
            name='weeklynutrition',
            unique_together=None,
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='MainGallery',
        ),
        migrations.DeleteModel(
            name='MainPage',
        ),
        migrations.DeleteModel(
            name='MainReview',
        ),
        migrations.DeleteModel(
            name='Nutrient',
        ),
        migrations.DeleteModel(
            name='WeeklyNutrition',
        ),
    ]
