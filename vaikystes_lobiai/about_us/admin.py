from django.contrib import admin
from .models import DailyRoutine, Grupe, TeamMember, Activity, AboutUsPage

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

class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

class GrupeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DailyRoutineInline]  # If you want to include routines here

class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ('about_us_title', 'about_us_description')
    inlines = [GrupeInline, TeamMemberInline]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Grupe, GrupeAdmin)
admin.site.register(TeamMember)
admin.site.register(DailyRoutine, DailyRoutineAdmin)  # Ensure DailyRoutineAdmin is registered
admin.site.register(AboutUsPage, AboutUsPageAdmin)
