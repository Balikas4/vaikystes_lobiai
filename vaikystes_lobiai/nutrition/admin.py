from django.contrib import admin
from .models import Nutrient, WeeklyNutrition, NutritionPage

class NutrientAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

class WeeklyNutritionAdmin(admin.ModelAdmin):
    list_display = ('week_number', 'day')
    list_filter = ('week_number',)  # Allows filtering by week number
    filter_horizontal = ('nutrients',)  # Allows multiple selection of nutrients

class NutritionPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Nutrient, NutrientAdmin)
admin.site.register(WeeklyNutrition, WeeklyNutritionAdmin)
admin.site.register(NutritionPage, NutritionPageAdmin)