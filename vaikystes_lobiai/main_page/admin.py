from django.contrib import admin
from .models import Hero, MainGallery, MainReview, MainPage

class HeroInline(admin.StackedInline):
    model = Hero
    can_delete = False
    max_num = 1
    verbose_name_plural = 'Hero Section'
    fields = ['hero_title', 'hero_description', 'hero_button_text', 'hero_button_url', 'hero_photo']  # Include the new field

class MainGalleryInline(admin.StackedInline):
    model = MainGallery
    extra = 1
    max_num = 6
    verbose_name_plural = 'Main Gallery'

class ReviewInline(admin.StackedInline):
    model = MainReview
    extra = 0
    verbose_name_plural = 'Reviews'

class MainPageAdmin(admin.ModelAdmin):
    inlines = [HeroInline, MainGalleryInline, ReviewInline]

admin.site.register(MainPage, MainPageAdmin)
