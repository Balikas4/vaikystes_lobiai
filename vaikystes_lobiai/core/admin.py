from django.contrib import admin
from .models import Email, GalleryCategory, GalleryImage, Review

class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # Fields to display in the admin list view
    search_fields = ('name', 'email')                # Fields to enable search functionality
    list_filter = ('submitted_at',)                  # Filters for the admin list view
    ordering = ('-submitted_at',)                    # Default ordering (newest first)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryCategoryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('name',)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('category', 'image', 'description')
    list_filter = ('category',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    search_fields = ('name', 'text')

admin.site.register(Email, EmailAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Review)