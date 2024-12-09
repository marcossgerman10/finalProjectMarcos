# models.py
from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    password_confirmation = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country_of_residence = models.CharField(max_length=100, default="USA")
    nationality = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    english_proficiency = models.CharField(max_length=100)
    sat_score = models.IntegerField(null=True, blank=True)
    act_score = models.IntegerField(null=True, blank=True)
    soccer_experience_years = models.IntegerField()
    soccer_team = models.CharField(max_length=100)
    soccer_position = models.CharField(max_length=100)
    soccer_achievements = models.TextField()
    soccer_level = models.CharField(max_length=100)
    international_experience = models.BooleanField(default=False)
    coach_reference = models.TextField(null=True, blank=True)
    commitment_to_study = models.BooleanField(default=False)
    comply_with_rules = models.BooleanField(default=False)
    available_for_tryouts = models.BooleanField(default=False)
    scholarship_interest = models.CharField(max_length=100)
    motivation = models.TextField()
    completed = models.BooleanField(default=False)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

