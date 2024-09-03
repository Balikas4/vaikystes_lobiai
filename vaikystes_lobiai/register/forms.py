# register/forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'first_last_name', 'contact_phone', 'email', 'home_address',
            'document_date', 'admission_date', 'child_first_last_name', 
            'child_first_name', 'child_last_name', 'child_personal_code', 
            'child_home_address', 'father_info', 'mother_info', 
            'child_health_info', 'child_talents'
        ]
        widgets = {
            'document_date': forms.DateInput(attrs={'type': 'date'}),
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'child_home_address': forms.Textarea(attrs={'rows': 3}),
            'father_info': forms.Textarea(attrs={'rows': 2}),
            'mother_info': forms.Textarea(attrs={'rows': 2}),
            'child_health_info': forms.Textarea(attrs={'rows': 3}),
            'child_talents': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'first_last_name': 'Vardas, Pavardė (mamos, tėvo, globėjo)',
            'contact_phone': 'Kontaktinis telefonas',
            'email': 'El. paštas',
            'home_address': 'Namų adresas',
            'document_date': 'Dokumento data',
            'admission_date': 'Priėmimo data',
            'child_first_last_name': 'Vaiko vardas ir pavardė',
            'child_first_name': 'Vaiko vardas',
            'child_last_name': 'Vaiko pavardė',
            'child_personal_code': 'Vaiko asmens kodas',
            'child_home_address': 'Namų adresas (faktinė ir deklaruota, jei nesutampa)',
            'father_info': 'Tėtis (vardas, pavardė, kontaktinis telefonas, el. paštas)',
            'mother_info': 'Mama (vardas, pavardė, kontaktinis telefonas, el. paštas)',
            'child_health_info': 'Duomenys apie vaikučio sveikatą',
            'child_talents': 'Vaikučio išskirtiniai gebėjimai, talentai, pomėgiai',
        }
        help_texts = {
            'child_health_info': 'Informacija apie vaiko sveikatą (alergijos, regos, klausos problemos ir kt.)',
        }
