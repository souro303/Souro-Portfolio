import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

# def projects(request):
#     return render(request, 'base/projects.html')

def resume(request):
    return render(request, 'base/resume.html')

def download_resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'Resume', 'SOURO RESUME.pdf')  # Replace with your actual file path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')

def contact(request):
    return render(request, 'base/contact.html')

def contact_view(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create the email content
        email_content = f"""
        Name: {name}
        Email: {email}
        
        Subject: {subject}
        
        Message:
        {message}
        """
        
        # Send email with form data
        send_mail(
            subject,
            email_content,
            email,  # Sender's email address
            ['souro.contact@gmail.com'],  # List of recipient(s)
            fail_silently=False,  # Set to True to suppress errors if email sending fails
        )
        
        return render(request, 'base/contactsuccess.html')
    
    return render(request, 'base/contact.html')


projects_data = [
    {
        'id': 1,
        'title': 'Project 1',
        'description': 'Description for project 1',
        'long_description': 'long_description for project 1',
        'image_url': '/static/images/profile.png',
        'detail_url': '/projects/1/',
        'tags': ['Python', 'Django'],
        'source_url': 'https://github.com/user/project1'
    },
    {
        'id': 2,
        'title': 'Project 2',
        'description': 'Description for project 2',
        'long_description': 'long_description for project 2',
        'image_url': 'https://via.placeholder.com/150',
        'detail_url': '/projects/2/',
        'tags': ['JavaScript', 'React'],
        'source_url': 'https://github.com/user/project2'
    },
    {
        'id': 3,
        'title': 'Project 3',
        'description': 'Description for project 3',
        'long_description': 'long_description for project 3',
        'image_url': 'https://via.placeholder.com/150',
        'detail_url': '/projects/3/',
        'tags': ['HTML', 'CSS', 'Bootstrap'],
        'source_url': 'https://github.com/user/project3'
    },
    {
        'id': 4,
        'title': 'Project 4',
        'description': 'Description for project 4',
        'long_description': 'long_description for project 4',
        'image_url': 'https://via.placeholder.com/150',
        'detail_url': '/projects/4/',
        'tags': ['HTML', 'CSS', 'Bootstrap'],
        'source_url': 'https://github.com/user/project4'
    },
]

def projects(request):
    context = {
        'projects': projects_data
    }
    return render(request, 'base/projects.html', context)

def project_detail(request, project_id):
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if not project:
        return render(request, '404.html', status=404)
    
    context = {
        'project': project
    }
    return render(request, 'base/project_detail.html', context)