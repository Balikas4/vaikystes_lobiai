from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from about_us.models import AboutUsPage, Grupe, DailyRoutineActivity
from gallery.models import GalleryCategory
from main_page.models import MainReview, MainPage
from nutrition.models import NutritionPage, WeeklyNutrition
from admissions.models import LankymoKaina, NuolaidosIrKompensacijos
from register.models import Registration
from register.forms import RegistrationForm
from django.db.models import Case, When, Value, IntegerField
from contact.models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



def home(request):
    main_page = MainPage.objects.first()
    reviews = MainReview.objects.filter(main_page=main_page)
    return render(request, 'main.html', {'main_page': main_page, 'reviews': reviews})

def about(request):
    about_us_page = AboutUsPage.objects.first()  # Assuming there's only one AboutUsPage
    groups = Grupe.objects.filter(about_us_page=about_us_page)

    # Define days of the week in Lithuanian
    days_of_week = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis"]

    # Prepare routine data
    routine_data = {}
    for group in groups:
        group_routines = {day: None for day in days_of_week}
        for routine in group.routines.all():
            # Fetch activities ordered by the 'order' field
            activities = DailyRoutineActivity.objects.filter(dailyroutine=routine).order_by('order')
            # Prepare a list of activity objects in the correct order
            ordered_activities = [activity.activity for activity in activities]
            group_routines[routine.day] = {
                'routine': routine,
                'activities': ordered_activities
            }
        routine_data[group.id] = group_routines

    context = {
        'about_us_page': about_us_page,
        'groups': groups,
        'routine_data': routine_data,
        'days_of_week': days_of_week,
    }
    return render(request, 'about.html', context)

def education(request):
    return render(request, 'education.html')

def nutrition(request):
    # Fetch the NutritionPage
    nutrition_page = NutritionPage.objects.first()  # Adjust as needed to get the specific NutritionPage
    
    # Define the correct order of days
    days_order = ['Pirmadienis', 'Antradienis', 'Trečiadienis', 'Ketvirtadienis', 'Penktadienis']
    
    # Fetch Weekly Nutrition data, grouped by week and sorted by day order
    weeks = {}
    for week in range(1, 5):
        weeks[week] = WeeklyNutrition.objects.filter(
            week_number=week
        ).order_by(
            Case(
                *[When(day=day, then=Value(index)) for index, day in enumerate(days_order)],
                output_field=IntegerField()
            )
        )

    context = {
        'nutrition_page': nutrition_page,
        'weeks': weeks,
    }
    return render(request, 'nutrition.html', context)


def admissions(request):
    lankymo_kaina = LankymoKaina.objects.first()  # Adjust if there are multiple instances
    nuolaidos_ir_kompensacijos = NuolaidosIrKompensacijos.objects.first()  # Get the first instance

    context = {
        'lankymo_kaina': lankymo_kaina,
        'nuolaidos_ir_kompensacijos': nuolaidos_ir_kompensacijos
    }

    return render(request, 'admissions.html', context)


def gallery(request):
    categories = GalleryCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'gallery.html', context)

def contact(request):
    context = {
        'contact': Contact.objects.first(),  # Example, adjust according to your context
    }
    return render(request, 'contact.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()

            # Pr`epare admin email
            admin_subject = 'Naujas registracijos pateikimas'
            admin_message = f'''
            Naujas registracijos įrašas buvo pateiktas su šiais duomenimis:

            **Tėvų/Globėjų Informacija**
            - Vardas: {registration.first_last_name}
            - Kontaktinis Telefonas: {registration.contact_phone}
            - El. Paštas: {registration.email}
            - Namų Adresas: {registration.home_address}

            **Dokumento ir Priėmimo Datos**
            - Dokumento Data: {registration.document_date}
            - Vaiko Vardas: {registration.child_first_last_name}
            - Priėmimo Data: {registration.admission_date}

            **Vaiko Informacija**
            - Vaiko Vardas: {registration.child_first_name}
            - Vaiko Pavardė: {registration.child_last_name}
            - Vaiko Asmens Kodas: {registration.child_personal_code}
            - Vaiko Namų Adresas: {registration.child_home_address}

            **Tėvų Informacija**
            - Tėčio Informacija: {registration.father_info}
            - Mamos Informacija: {registration.mother_info}

            **Vaiko Sveikatos ir Gebėjimų Informacija**
            - Vaiko Sveikatos Informacija: {registration.child_health_info}
            - Vaiko Talentai: {registration.child_talents}
            '''
            try:
                # Send admin email
                send_mail(
                    admin_subject,
                    admin_message,
                    'admin@vaikysteslobiai.lt',
                    ['registracija@vaikysteslobiai.lt'],
                    fail_silently=False,
                )

                # Prepare welcome email
                welcome_subject = 'Welcome to Our Service'
                welcome_message = f'''
                Dėkojame,

                Jūsų prašymas buvo gautas, netrukus susisieksime

                Pagarbiai "vaikystės lobiai" administracija

                '''

                # Send welcome email
                if registration.email:
                    send_mail(
                        welcome_subject,
                        welcome_message,
                        'admin@vaikysteslobiai.lt',
                        [registration.email],
                        fail_silently=False,
                    )

                # Success message and redirect
                messages.success(request, 'Sėkmingai pateikėte registracijos formą')
                return redirect('register')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                # Log the error message for further inspection
                print(f"Error sending email: {e}")
                messages.error(request, 'Įvyko klaida siunčiant el. laišką. Bandykite dar kartą.')

        else:
            messages.error(request, 'Įvyko klaida registruojantis')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})