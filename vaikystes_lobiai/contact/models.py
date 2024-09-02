from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    description = RichTextField()
    additional_info = RichTextField()
    hero_photo = models.ImageField(upload_to='contact_photos/', blank=True, null=True)

    def __str__(self):
        return "Contact Information"
