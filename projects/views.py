from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects':projects})

def details(request, project_id):
    project_details = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/details.html', {'project': project_details})