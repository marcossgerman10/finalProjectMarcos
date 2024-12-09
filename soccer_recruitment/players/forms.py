from django import forms
from .models import Player

class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email', 'password', 'password_confirmation']

    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data