# register/admin.py
from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'child_first_name', 
        'child_last_name', 
        'child_personal_code', 
        'father_info', 
        'mother_info'
    )
    search_fields = ('child_first_name', 'child_last_name', 'child_personal_code')
    list_filter = ('admission_date',)
    readonly_fields = ('document_date', 'admission_date') # If you want certain fields to be read-only

admin.site.register(Registration, RegistrationAdmin)
