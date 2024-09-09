from django.db import models
from ckeditor.fields import RichTextField

class AboutUsPage(models.Model):
    about_us_title = models.CharField(max_length=255)
    about_us_description = models.TextField()
    hero_photo = models.ImageField(upload_to='hero_photos/', blank=True, null=True)
    team_photo = models.ImageField(upload_to='hero_photos/', blank=True, null=True)
    about_us_description = RichTextField()  # Changed from TextField to RichTextField
    team_description = RichTextField()  # Add this field for team members description


    def __str__(self):
        return self.about_us_title

class Grupe(models.Model):
    about_us_page = models.ForeignKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name='grupes'
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)  # Field to set order

    class Meta:
        ordering = ['order']  # Order by 'order' field

    def __str__(self):
        return self.name

class DailyRoutineActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    dailyroutine = models.ForeignKey('DailyRoutine', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Order activities within routine

    class Meta:
        ordering = ['order']
        unique_together = ('activity', 'dailyroutine')

    def __str__(self):
        return f"{self.activity.name} in {self.dailyroutine.group.name} - {self.dailyroutine.day}"

class DailyRoutine(models.Model):
    group = models.ForeignKey(Grupe, on_delete=models.CASCADE, related_name='routines')
    day = models.CharField(max_length=14, choices=[
        ('Pirmadienis', 'Pirmadienis'),
        ('Antradienis', 'Antradienis'),
        ('Trečiadienis', 'Trečiadienis'),
        ('Ketvirtadienis', 'Ketvirtadienis'),
        ('Penktadienis', 'Penktadienis'),
    ])
    activities = models.ManyToManyField(Activity, through='DailyRoutineActivity', related_name='routines')

    class Meta:
        unique_together = ('group', 'day')

    def __str__(self):
        return f"{self.group.name} - {self.day}"