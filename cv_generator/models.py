from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    grade = models.CharField(max_length=50, blank=True, null=True)

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    job_duration = models.CharField(max_length=100)
    job_responsibilities = models.TextField()

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()