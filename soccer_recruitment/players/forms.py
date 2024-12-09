from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Player

# Registration Form
class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email")
    name = forms.CharField(max_length=100, label="First Name")
    surname = forms.CharField(max_length=100, label="Last Name")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if the email already exists in the User model
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Password should be at least 8 characters long
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # Ensure the passwords match
        if password != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


# Sign In Form
class SignInForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if the email exists in the User model
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Email not found.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Ensure password length is valid
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters.")
        return password


# Player Information Form for Questionnaire
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player  # Make sure you have a Player model created with fields
        fields = [
            'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'country_of_residence', 'nationality',
            'gpa', 'english_proficiency', 'sat_score', 'act_score', 'soccer_experience_years', 'soccer_team', 'soccer_position',
            'soccer_achievements', 'soccer_level', 'international_experience', 'coach_reference', 'commitment_to_study',
            'comply_with_rules', 'available_for_tryouts', 'scholarship_interest', 'motivation'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gpa': forms.NumberInput(attrs={'step': 0.01}),
            'sat_score': forms.NumberInput(),
            'act_score': forms.NumberInput(),
            'soccer_experience_years': forms.NumberInput(),
            'soccer_achievements': forms.Textarea(),
            'soccer_level': forms.TextInput(),
            'coach_reference': forms.Textarea(),
            'motivation': forms.Textarea(),
        }
