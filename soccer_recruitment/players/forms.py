# INF601 - Advanced Programming in Python
# Marcos German
# Final Project
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Player

# Registration Form
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError("Passwords do not match.")
        return cleaned_data


# Sign In Form
class SignInForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Email not found.")
        return email


# Player Information Form for Questionnaire
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'date_of_birth', 'country_of_residence', 'nationality', 'high_school_graduation_date',
            'gpa', 'english_proficiency', 'sat_score', 'act_score', 'soccer_experience_years',
            'soccer_team', 'soccer_position', 'soccer_achievements', 'soccer_level',
            'international_experience', 'coach_reference', 'commitment_to_study',
            'comply_with_rules', 'available_for_tryouts', 'scholarship_interest', 'motivation'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'high_school_graduation_date': forms.DateInput(attrs={'type': 'date'}),
            'gpa': forms.NumberInput(attrs={'step': 0.01}),
            'sat_score': forms.NumberInput(),
            'act_score': forms.NumberInput(),
            'soccer_experience_years': forms.NumberInput(),
            'soccer_achievements': forms.Textarea(attrs={'placeholder': 'Describe notable soccer achievements'}),
            'coach_reference': forms.Textarea(attrs={'placeholder': 'Provide coach references if available'}),
            'motivation': forms.Textarea(attrs={'placeholder': 'Describe your motivation for pursuing a soccer scholarship in the US'}),
        }
        labels = {
            'date_of_birth': 'Date of Birth',
            'high_school_graduation_date': 'High School Graduation Date',
            'gpa': 'Grade Point Average(GPA) on a 4.0 scale in High School',
            'english_proficiency': 'Have you taken any English Proficiency test(TOEFL,IELTS)?',
            'sat_score': 'SAT Score(if taken, if not put 0)',
            'act_score': 'ACT Score(if taken, if not put 0)',
            'soccer_experience_years': 'Years Playing Soccer',
            'soccer_team': 'Current Soccer Team/Club',
            'soccer_position': 'Position(s) Played',
            'soccer_achievements': 'Soccer Achievements',
            'soccer_level': 'Highest Level of Play',
            'international_experience': 'Played with national team?',
            'coach_reference': 'References (Coaches/Teammates)',
            'commitment_to_study': 'Commitment to a Full-Time College Schedule',
            'comply_with_rules': 'Agreement to Abide by Rules',
            'available_for_tryouts': 'Availability for Tryouts in the US',
            'scholarship_interest': 'Scholarship Interest(Academic/Athletic/Both)',
            'motivation': 'Motivation for Applying',
        }

class UploadDocumentsForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'soccer_video', 'highschool_transcript', 'sat_results', 'toefl_duolingo_results', 'passport'
        ]
        widgets = {
            'soccer_video': forms.ClearableFileInput(attrs={'multiple': False}),
            'highschool_transcript': forms.ClearableFileInput(attrs={'multiple': False}),
            'sat_results': forms.ClearableFileInput(attrs={'multiple': False}),
            'toefl_duolingo_results': forms.ClearableFileInput(attrs={'multiple': False}),
            'passport': forms.ClearableFileInput(attrs={'multiple': False}),
        }
        labels = {
            'soccer_video' : 'Soccer Highlights Video',
            'highschool_transcript' : 'High School Transcript',
            'sat_results' : 'SAT Results',
            'toefl_duolingo_results' : 'TOEFL/Duolingo Results',
            'passport' : 'Passport',
        }