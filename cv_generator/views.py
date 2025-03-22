from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Profile, Skill, Education, WorkExperience, Project
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def select_template(request):
    return render(request, 'select_template.html')

@login_required
def cv_form(request):
    user = request.user
    # Rest of the code...

@login_required
def generate_pdf(request):
    user = request.user
    
# Landing Page View
def landing(request):
    """
    Render the landing page.
    """
    return render(request, 'landing.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to the dashboard after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
def logout_view(request):
    logout(request)
    return redirect('landing')  # Redirect to the landing page after logout

# Dashboard View
def dashboard(request):
    return render(request, 'dashboard.html')

# Template Selection View
def select_template(request):
    return render(request, 'select_template.html')

# CV Form View
def cv_form(request):
    user = request.user

    # Check if a profile already exists for the user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        # Update the profile with the new data
        profile.full_name = request.POST.get('full_name', profile.full_name)
        profile.contact_info = request.POST.get('contact_info', profile.contact_info)
        profile.bio = request.POST.get('bio', profile.bio)
        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']
        profile.save()

        # Handle skills
        Skill.objects.filter(user=user).delete()  # Delete existing skills
        for skill_name in request.POST.getlist('skill_name'):
            if skill_name.strip():  # Ensure the skill name is not empty
                Skill.objects.create(user=user, skill_name=skill_name)

        # Handle education
        Education.objects.filter(user=user).delete()  # Delete existing education
        institutes = request.POST.getlist('institute')
        degrees = request.POST.getlist('degree')
        years = request.POST.getlist('year')
        grades = request.POST.getlist('grade')
        for i in range(len(institutes)):
            if institutes[i].strip():  # Ensure the institute is not empty
                Education.objects.create(
                    user=user,
                    institute=institutes[i],
                    degree=degrees[i],
                    year=years[i],
                    grade=grades[i]
                )

        # Handle work experience
        WorkExperience.objects.filter(user=user).delete()  # Delete existing work experience
        companies = request.POST.getlist('company_name')
        durations = request.POST.getlist('job_duration')
        responsibilities = request.POST.getlist('job_responsibilities')
        for i in range(len(companies)):
            if companies[i].strip():  # Ensure the company name is not empty
                WorkExperience.objects.create(
                    user=user,
                    company_name=companies[i],
                    job_duration=durations[i],
                    job_responsibilities=responsibilities[i]
                )

        # Handle projects
        Project.objects.filter(user=user).delete()  # Delete existing projects
        titles = request.POST.getlist('project_title')
        descriptions = request.POST.getlist('project_description')
        for i in range(len(titles)):
            if titles[i].strip():  # Ensure the project title is not empty
                Project.objects.create(
                    user=user,
                    project_title=titles[i],
                    project_description=descriptions[i]
                )

        # Check if the user clicked "Save" or "Save and Generate PDF"
        if 'save' in request.POST:
            return redirect('dashboard')  # Redirect to the dashboard after saving
        elif 'generate_pdf' in request.POST:
            return redirect('generate_pdf')  # Redirect to the PDF generation page

    # Pre-fill the form with existing data
    skills = Skill.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    work_experience = WorkExperience.objects.filter(user=user)
    projects = Project.objects.filter(user=user)

    return render(request, 'cv_form.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
        'work_experience': work_experience,
        'projects': projects,
    })

# Generate PDF View
def generate_pdf(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    skills = Skill.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    work_experience = WorkExperience.objects.filter(user=user)
    projects = Project.objects.filter(user=user)

    # Render the HTML template
    html_string = render_to_string('cv_template1.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
        'work_experience': work_experience,
        'projects': projects,
    })

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user.username}_cv.pdf"'

    # Generate PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(
        html_string,
        dest=response,
        link_callback=link_callback  # Handle static and media files
    )
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response

# Function to handle static and media files during PDF generation
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources.
    """
    # Handle static files
    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    # Handle media files
    elif uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    else:
        # Handle absolute URIs (e.g., http://example.com/image.jpg)
        return uri

    # Ensure the file exists
    if not os.path.isfile(path):
        raise Exception(f"File not found: {path}")

    return path