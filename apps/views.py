from django.shortcuts import render
from .models import Project, Skill

def home(request): 
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'index.html', {'projects': projects, 'skills': skills})


def single(request):
    return render(request, 'single.html')
