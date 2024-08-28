from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from .models import GalleryCategory, Review

from django.shortcuts import render

def home(request):
    reviews = Review.objects.all()
    return render(request, 'main.html', {'reviews': reviews})

def about(request):
    return render(request, 'about.html')

def education(request):
    return render(request, 'education.html')

def nutrition(request):
    return render(request, 'nutrition.html')

def admissions(request):
    return render(request, 'admissions.html')

def gallery(request):
    our_moments = GalleryCategory.objects.get(name='Mūsų akimirkos').images.all()
    environment = GalleryCategory.objects.get(name='Darželio aplinka').images.all()
    
    context = {
        'our_moments': our_moments,
        'environment': environment,
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
