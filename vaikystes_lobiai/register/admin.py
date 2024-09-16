# register/admin.py
from django.contrib import admin
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'child_first_name', 
        'child_last_name', 
        'child_personal_code', 
        'father_info', 
        'mother_info',
        'download_document'
    )
    search_fields = ('child_first_name', 'child_last_name', 'child_personal_code')
    list_filter = ('admission_date',)
    readonly_fields = ('document_date', 'admission_date') # If you want certain fields to be read-only

    def download_document(self, obj):
        if obj.document:
            return f'<a href="{obj.document.url}">Download Document</a>'
        return "No Document"

    download_document.allow_tags = True
    download_document.short_description = "Download Document"

    def get_urls(self):
        urls = super().get_urls()
        return urls


admin.site.register(Registration, RegistrationAdmin)
