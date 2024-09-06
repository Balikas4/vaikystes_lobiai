from django.db import models

class Nutrient(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class WeeklyNutrition(models.Model):
    week_number = models.PositiveIntegerField(
        choices=[(1, 'Week 1'), (2, 'Week 2'), (3, 'Week 3'), (4, 'Week 4')],
        default=1  # Temporary default value
    )
    day = models.CharField(max_length=16, choices=[
        ('Pirmadienis', 'Pirmadienis'),
        ('Antradienis', 'Antradienis'),
        ('Trečiadienis', 'Trečiadienis'),
        ('Ketvirtadienis', 'Ketvirtadienis'),
        ('Penktadienis', 'Penktadienis'),
    ])
    nutrients = models.ManyToManyField(Nutrient, related_name='weekly_nutrition')

    class Meta:
        unique_together = ('week_number', 'day')

    def __str__(self):
        return f"Week {self.week_number} - {self.day}"

class NutritionPage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
