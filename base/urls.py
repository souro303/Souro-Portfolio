from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects/', views.projects, name='projects'), 
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('resume', views.resume, name='resume'),
    path('resume/download/', views.download_resume, name='download_resume'),
    path('contact', views.contact, name='contact'),
    path('contact_view/', views.contact_view, name='contact_view'),
]
