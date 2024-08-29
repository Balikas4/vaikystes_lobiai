from django.contrib import admin
from .models import Email

class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)
    ordering = ('-submitted_at',)

admin.site.register(Email, EmailAdmin)
