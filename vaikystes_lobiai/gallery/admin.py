from django.contrib import admin
from .models import GalleryCategory, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryCategoryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('name',)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('category', 'image', 'description')
    list_filter = ('category',)

admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryImage)
