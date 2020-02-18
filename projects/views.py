from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import Detail
from .models import Comment

def home(request):
    return render(request, 'projects/home.html')

def about(request):
    return render(request, 'projects/about.html')

def work(request):
    projects = Project.objects
    return render(request, 'projects/work.html', {'projects':projects})

def details(request, project_id):
    project_details = get_object_or_404(Project, pk=project_id)
    # project_name = get_object_or_404(Project, pk=project_id)
    # details = get_object_or_404(Detail, pk=project_name)

    return render(request, 'projects/details.html', {'project': project_details})

def resume(request):
    return render(request, 'projects/resume.html')

def contact(request):
    return render(request, 'projects/contact.html')

def temp(request):
    return render(request, 'projects/temp.html')