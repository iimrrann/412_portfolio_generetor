from django.contrib import admin
from .models import Profile, Skill, Education, WorkExperience, Project

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Project)