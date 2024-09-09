from django.db import models

class MainPage(models.Model):
    # Fields for MainPage
    pass

    class Meta:
        verbose_name = "Pagrindinis puslapis"  # Singular name
        verbose_name_plural = "Pagrindiniai puslapiai"  # Plural name

class Hero(models.Model):
    main_page = models.OneToOneField(MainPage, on_delete=models.CASCADE, related_name='hero')
    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField()
    hero_button_text = models.CharField(max_length=50)
    hero_button_url = models.URLField()
    hero_photo = models.ImageField(upload_to='hero_photos/', blank=True, null=True)


class MainGallery(models.Model):
    main_page = models.ForeignKey(MainPage, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='main_gallery/')

class MainReview(models.Model):
    main_page = models.ForeignKey(MainPage, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    text = models.TextField()
