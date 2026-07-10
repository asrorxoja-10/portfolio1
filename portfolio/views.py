from django.shortcuts import render
from .models import Skill, Project

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-created_at')
    
    context = {
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)