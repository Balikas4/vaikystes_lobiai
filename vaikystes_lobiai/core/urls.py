from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                        # Home page
    path('apie-mus/', views.about, name='about'),                # Apie Mus
    path('ugdymas/', views.education, name='education'),    # Ugdymas
    path('maitinimas/', views.nutrition, name='nutrition'),    # Maitinimas
    path('priemimo-tvarka/', views.admissions, name='admissions'), # Priemimo Tvarka
    path('galerija/', views.gallery, name='gallery'),          # Galerija
    path('kontaktai/', views.contact, name='contact'),          # Kontaktai
    path('registracija/', views.register, name='register'),       # Registracija
]
