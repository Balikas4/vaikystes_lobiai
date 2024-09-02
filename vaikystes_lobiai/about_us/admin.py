from django.contrib import admin
from .models import DailyRoutine, Grupe, Activity, AboutUsPage

class ActivityInline(admin.TabularInline):
    model = DailyRoutine.activities.through
    extra = 1

class DailyRoutineAdmin(admin.ModelAdmin):
    list_display = ('group', 'day')
    filter_horizontal = ('activities',)

class DailyRoutineInline(admin.StackedInline):
    model = DailyRoutine
    extra = 1
    inlines = [ActivityInline]

class GrupeInline(admin.StackedInline):
    model = Grupe
    extra = 1
    inlines = [DailyRoutineInline]

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class GrupeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DailyRoutineInline]  # If you want to include routines here

class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ('about_us_title', 'about_us_description', 'hero_photo_display', 'team_photo_display', 'team_description')
    inlines = [GrupeInline]

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
