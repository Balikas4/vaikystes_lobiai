from django.db import models
from ckeditor.fields import RichTextField

class LankymoKaina(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()  # Changed to RichTextField
    additional_info = RichTextField()  # Changed to RichTextField

    def __str__(self):
        return self.title

class NuolaidosIrKompensacijos(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()  # Changed to RichTextField
    image = models.ImageField(upload_to='discounts_and_compensations/')

    def __str__(self):
        return self.title