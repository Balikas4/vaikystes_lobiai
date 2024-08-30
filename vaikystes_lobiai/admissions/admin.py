from django.contrib import admin
from .models import LankymoKaina, NuolaidosIrKompensacijos

@admin.register(LankymoKaina)
class LankymoKainaAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(NuolaidosIrKompensacijos)
class NuolaidosIrKompensacijosAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
