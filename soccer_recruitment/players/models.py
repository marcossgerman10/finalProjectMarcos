# INF601 - Advanced Programming in Python
# Marcos German
# Final Project

from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    date_of_birth = models.DateField(null=True, blank=True)
    country_of_residence = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    high_school_graduation_date = models.DateField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    english_proficiency = models.CharField(max_length=100, null=True, blank=True)
    sat_score = models.IntegerField(null=True, blank=True)
    act_score = models.IntegerField(null=True, blank=True)
    soccer_experience_years = models.IntegerField(null=True, blank=True)
    soccer_team = models.CharField(max_length=100, null=True, blank=True)
    soccer_position = models.CharField(max_length=100, null=True, blank=True)
    soccer_achievements = models.TextField(null=True, blank=True)
    soccer_level = models.CharField(max_length=100, null=True, blank=True)
    international_experience = models.BooleanField(default=False)
    coach_reference = models.TextField(null=True, blank=True)
    commitment_to_study = models.BooleanField(default=False)
    comply_with_rules = models.BooleanField(default=False)
    available_for_tryouts = models.BooleanField(default=False)
    scholarship_interest = models.CharField(max_length=100, null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    submitted = models.BooleanField(default=False)

    # File upload fields
    soccer_video = models.FileField(upload_to='soccer_videos/', null=True, blank=True)
    highschool_transcript = models.FileField(upload_to='highschool_transcripts/', null=True, blank=True)
    sat_results = models.FileField(upload_to='sat_results/', null=True, blank=True)
    toefl_duolingo_results = models.FileField(upload_to='toefl_duolingo_results/', null=True, blank=True)
    passport = models.FileField(upload_to='passports/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
