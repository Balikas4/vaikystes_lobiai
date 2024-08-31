# register/forms.py
from django import forms

class RegistrationForm(forms.Form):
    # Parent/Guardian Information
    first_name = forms.CharField(max_length=100, label='Vardas', required=False)
    last_name = forms.CharField(max_length=100, label='Pavardė (mamos, tėvo, globėjo)', required=False)
    contact_phone = forms.CharField(max_length=15, label='Kontaktinis telefonas', required=False)
    email = forms.EmailField(label='El. paštas', required=False)
    home_address = forms.CharField(max_length=255, label='Namų adresas', required=False)

    # Document and Admission Dates
    document_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Dokumento data', required=False)
    admission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Priėmimo data', required=False)

    # Child Information (Mandatory Fields)
    child_first_name = forms.CharField(max_length=100, label='*Vaiko vardas', required=True)
    child_last_name = forms.CharField(max_length=100, label='*Vaiko pavardė', required=True)
    child_personal_code = forms.CharField(max_length=20, label='*Vaiko asmens kodas', required=True)
    child_home_address = forms.CharField(
        max_length=255, 
        label='*Namų adresas (faktinė ir deklaruota, jei nesutampa)', 
        required=True
    )

    # Parent Information (Mandatory)
    father_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}), 
        label='*Tėtis (vardas, pavardė, kontaktinis telefonas, el. paštas)', 
        required=True
    )
    mother_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}), 
        label='*Mama (vardas, pavardė, kontaktinis telefonas, el. paštas)', 
        required=True
    )

    # Child's Health and Abilities (Optional)
    child_health_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), 
        label='*Duomenys apie vaikučio sveikatą (alergija, rega, klausa, kalba, ligos, skiepai, kt.)', 
        required=True
    )
    child_talents = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), 
        label='Vaikučio išskirtiniai gebėjimai, talentai, pomėgiai', 
        required=False
    )
