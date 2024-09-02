from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import LankymoKaina, NuolaidosIrKompensacijos

class LankymoKainaForm(forms.ModelForm):
    class Meta:
        model = LankymoKaina
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'additional_info': CKEditorWidget(),
        }

class NuolaidosIrKompensacijosForm(forms.ModelForm):
    class Meta:
        model = NuolaidosIrKompensacijos
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

@admin.register(LankymoKaina)
class LankymoKainaAdmin(admin.ModelAdmin):
    form = LankymoKainaForm
    list_display = ('title',)

@admin.register(NuolaidosIrKompensacijos)
class NuolaidosIrKompensacijosAdmin(admin.ModelAdmin):
    form = NuolaidosIrKompensacijosForm
    list_display = ('title',)
    search_fields = ('title', 'description',)
