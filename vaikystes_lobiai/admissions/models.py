from django.db import models

class LankymoKaina(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    additional_info = models.TextField()
    
    def __str__(self):
        return self.title

class NuolaidosIrKompensacijos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='discounts_and_compensations/')
    
    def __str__(self):
        return self.title