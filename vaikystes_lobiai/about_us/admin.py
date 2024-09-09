from django.contrib import admin
from .models import DailyRoutine, Grupe, Activity, AboutUsPage, DailyRoutineActivity

# Inline for managing activities within a DailyRoutine
class DailyRoutineActivityInline(admin.TabularInline):
    model = DailyRoutineActivity
    extra = 1
    ordering = ['order']  # Order inline by the 'order' field
    fields = ['activity', 'order']  # Show activity and order fields in the inline

class DailyRoutineAdmin(admin.ModelAdmin):
    list_display = ('group', 'day')
    inlines = [DailyRoutineActivityInline]  # Add the inline here

# Admin for Activity with ordering by 'order' field
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ['order']

# Inline for managing routines within Grupe
class DailyRoutineInline(admin.TabularInline):
    model = DailyRoutine
    extra = 1

# Admin for Grupe to use routines inline
class GrupeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DailyRoutineInline]  # Include routines inline in Grupe admin

class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ('about_us_title', 'about_us_description', 'hero_photo_display', 'team_photo_display', 'team_description')

    def hero_photo_display(self, obj):
        if obj.hero_photo:
            return "<img src='%s' width='100' height='50' />" % obj.hero_photo.url
        return "No photo"
    hero_photo_display.allow_tags = True
    hero_photo_display.short_description = "Hero Photo"

    def team_photo_display(self, obj):
        if obj.team_photo:
            return "<img src='%s' width='100' height='100' style='object-fit: cover;' />" % obj.team_photo.url
        return "No photo"
    team_photo_display.allow_tags = True
    team_photo_display.short_description = "Team Photo"

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Grupe, GrupeAdmin)
admin.site.register(DailyRoutine, DailyRoutineAdmin)  # Ensure DailyRoutineAdmin is registered
admin.site.register(AboutUsPage, AboutUsPageAdmin)
