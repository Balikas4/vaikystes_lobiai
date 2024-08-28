from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                        # Home page
    path('about/', views.about, name='about'),                # Apie Mus
    path('education/', views.education, name='education'),    # Ugdymas
    path('nutrition/', views.nutrition, name='nutrition'),    # Maitinimas
    path('admissions/', views.admissions, name='admissions'), # Priemimo Tvarka
    path('gallery/', views.gallery, name='gallery'),          # Galerija
    path('contact/', views.contact, name='contact'),          # Kontaktai
]
