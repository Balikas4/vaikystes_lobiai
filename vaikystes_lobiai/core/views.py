from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from about_us.models import AboutUsPage, Grupe, Activity, TeamMember
from gallery.models import GalleryCategory
from main_page.models import MainReview, MainPage
from nutrition.models import NutritionPage, WeeklyNutrition
from admissions.models import LankymoKaina, NuolaidosIrKompensacijos
from register.models import Registration
from register.forms import RegistrationForm
from django.db.models import Case, When, Value, IntegerField


def home(request):
    main_page = MainPage.objects.first()
    reviews = MainReview.objects.filter(main_page=main_page)
    return render(request, 'main.html', {'main_page': main_page, 'reviews': reviews})

def about(request):
    about_us_page = AboutUsPage.objects.first()  # Assuming there's only one AboutUsPage
    groups = Grupe.objects.filter(about_us_page=about_us_page)
    team_members = TeamMember.objects.filter(about_us_page=about_us_page)

    # Define days of the week in Lithuanian
    days_of_week = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis"]

    # Prepare routine data
    routine_data = {}
    for group in groups:
        group_routines = {day: None for day in days_of_week}
        for routine in group.routines.all():
            group_routines[routine.day] = routine
        routine_data[group.id] = group_routines

    context = {
        'about_us_page': about_us_page,
        'groups': groups,
        'routine_data': routine_data,
        'days_of_week': days_of_week,
        'team_members': team_members,
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
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to avoid form resubmission
        else:
            messages.error(request, 'There was an error submitting your form. Please try again.')
    else:
        form = EmailForm()
    
    return render(request, 'contact.html', {'form': form})  # Pass form to the template

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save form data to the Registration model
            Registration.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                contact_phone=form.cleaned_data['contact_phone'],
                email=form.cleaned_data['email'],
                home_address=form.cleaned_data['home_address'],
                document_date=form.cleaned_data['document_date'],
                admission_date=form.cleaned_data['admission_date'],
                child_first_name=form.cleaned_data['child_first_name'],
                child_last_name=form.cleaned_data['child_last_name'],
                child_personal_code=form.cleaned_data['child_personal_code'],
                child_home_address=form.cleaned_data['child_home_address'],
                father_info=form.cleaned_data['father_info'],
                mother_info=form.cleaned_data['mother_info'],
                child_health_info=form.cleaned_data['child_health_info'],
                child_talents=form.cleaned_data['child_talents'],
            )

            # Display success message and redirect
            messages.success(request, 'Registration form submitted successfully.')
            return redirect('register')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
