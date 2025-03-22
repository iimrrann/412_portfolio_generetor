from django.urls import path
from django.contrib.auth.views import LogoutView  # Import the built-in logout view
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cv-form/', views.cv_form, name='cv_form'),
    path('select-template/', views.select_template, name='select_template'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)