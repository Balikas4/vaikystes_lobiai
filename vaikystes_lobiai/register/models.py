# register/models.py
from django.db import models

class Registration(models.Model):
    # Parent/Guardian Information
    first_last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Vardas, Pavardė (mamos, tėvo, globėjo)')
    contact_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Kontaktinis telefonas')
    email = models.EmailField(blank=True, null=True, verbose_name='El. paštas')
    home_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Namų adresas')

    # Document and Admission Dates
    document_date = models.DateField(blank=True, null=True, verbose_name='Dokumento data')
    child_first_last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Vaiko vardas ir pavarde')
    admission_date = models.DateField(blank=True, null=True, verbose_name='Priėmimo data')

    # Child Information (Mandatory Fields)
    child_first_name = models.CharField(max_length=100, verbose_name='Vaiko vardas')
    child_last_name = models.CharField(max_length=100, verbose_name='Vaiko pavardė')
    child_personal_code = models.CharField(max_length=20, verbose_name='Vaiko asmens kodas')
    child_home_address = models.TextField(verbose_name='Namų adresas (faktinė ir deklaruota, jei nesutampa)')

    # Parent Information (Mandatory)
    father_info = models.TextField(verbose_name='Tėtis (vardas, pavardė, kontaktinis telefonas, el. paštas)')
    mother_info = models.TextField(verbose_name='Mama (vardas, pavardė, kontaktinis telefonas, el. paštas)')

    # Child's Health and Abilities (Optional)
    child_health_info = models.TextField(verbose_name='Duomenys apie vaikučio sveikatą', blank=False, null=True)
    child_talents = models.TextField(verbose_name='Vaikučio išskirtiniai gebėjimai, talentai, pomėgiai', blank=True, null=True)

    def __str__(self):
        return f"{self.child_first_name} {self.child_last_name}"
    
    class Meta:
        verbose_name = "Registracija"  # Singular name
        verbose_name_plural = "Registracijos"  # Plural name
