from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or 'No description'
    