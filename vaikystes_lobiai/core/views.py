from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from about_us.models import AboutUsPage, Grupe, Activity, TeamMember
from gallery.models import GalleryCategory
from main_page.models import MainReview, MainPage
from nutrition.models import NutritionPage, WeeklyNutrition
from admissions.models import LankymoKaina, NuolaidosIrKompensacijos

from django.shortcuts import render

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
    
    # Fetch Weekly Nutrition data, grouped by week
    weekly_nutrition_data = WeeklyNutrition.objects.order_by('week_number', 'day')
    
    # Prepare a dictionary to hold weekly nutrition data
    weeks = {}
    for week in range(1, 5):
        weeks[week] = WeeklyNutrition.objects.filter(week_number=week).order_by('day')

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
    return render(request, 'register.html')  # Ensure you have a 'register.html' template
