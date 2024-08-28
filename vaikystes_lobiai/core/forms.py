from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'email', 'message']  # Fields to be included in the form
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email Address',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Message',
                'rows': 5,
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message',
        }

    # Optional: Custom validation for fields (if needed)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Additional custom email validation can go here
        return email
