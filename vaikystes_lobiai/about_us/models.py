from django.db import models

class AboutUsPage(models.Model):
    about_us_title = models.CharField(max_length=255)
    about_us_description = models.TextField()
    hero_photo = models.ImageField(upload_to='hero_photos/', blank=True, null=True)
    team_photo = models.ImageField(upload_to='hero_photos/', blank=True, null=True)

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

class TeamMember(models.Model):
    about_us_page = models.ForeignKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name='team_members'
    )
    job_title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.job_title}"

class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DailyRoutine(models.Model):
    group = models.ForeignKey(Grupe, on_delete=models.CASCADE, related_name='routines')
    day = models.CharField(max_length=14, choices=[
        ('Pirmadienis', 'Pirmadienis'),
        ('Antradienis', 'Antradienis'),
        ('Trečiadienis', 'Trečiadienis'),
        ('Ketvirtadienis', 'Ketvirtadienis'),
        ('Penktadienis', 'Penktadienis'),
    ])
    activities = models.ManyToManyField(Activity, related_name='routines')

    class Meta:
        unique_together = ('group', 'day')

    def __str__(self):
        return f"{self.group.name} - {self.day}"
